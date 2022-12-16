from flask import render_template, url_for, redirect, \
    flash, session, request, make_response, jsonify
from werkzeug.security import generate_password_hash
import random
import string
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from sqlalchemy import or_
from functools import wraps
from decimal import *
from form import *


def rndColor():
    '''隨機顏色'''
    return (random.randint(32, 127),
            random.randint(32, 127),
            random.randint(32, 127))


def gene_text():
    '''生成4位驗證碼'''
    return ''.join(random.sample(string.ascii_letters + string.digits, 4))


def draw_lines(draw, num, width, height):
    '''劃線'''
    for num in range(num):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)


def get_verify_code():
    '''生成驗證碼圖形'''
    code = gene_text()
    # 圖片大小120×50
    width, height = 120, 50
    # 新圖片對象
    im = Image.new('RGB', (width, height), 'white')
    # 字體
    font = ImageFont.truetype('static/fonts/arial.ttf', 40)
    # draw對象
    draw = ImageDraw.Draw(im)
    # 繪制字符串
    for item in range(4):
        draw.text((5 + random.randint(-3, 3) + 23 * item, 5 + random.randint(-3, 3)),
                  text=code[item], fill=rndColor(), font=font)
    return im, code


@app.route('/code')
def get_code():
    image, code = get_verify_code()
    # 圖片以二進制形式寫入
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    # 把buf_str作為response返回前端，並設置首部字段
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    # 將驗證碼字符串儲存在session中
    session['image'] = code
    return response


def user_login(f):
    """
    登錄裝飾器
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/login/", methods=["GET", "POST"])
def login():
    """
    登錄
    """
    if "user_id" in session:  # 如果已經登錄，則直接跳轉到首頁
        return redirect(url_for("index"))
    form = LoginForm()  # 實例化LoginForm類
    if form.validate_on_submit():  # 如果提交
        data = form.data  # 接收表單數據
        # 判斷驗證碼
        # if session.get('image').lower() != form.verify_code.data.lower():
        #     flash('驗證碼錯誤', "err")
        #     return render_template("home/login.html", form=form)  # 返回登錄頁
        # 判斷用戶名是否存在
        user = User.query.filter_by(username=data["username"]).first()  # 獲取用戶信息
        if not user:
            flash("用戶名不存在！", "err")  # 輸出錯誤信息
            return render_template("home/login.html", form=form)  # 返回登錄頁
        # 判斷用戶名和密碼是否匹配
        # if not user.check_password(data["password"]):  # 調用check_password()方法，檢測用戶名密碼是否匹配
        #     flash("密碼錯誤！", "err")  # 輸出錯誤信息
        #     return render_template("home/login.html", form=form)  # 返回登錄頁

        session["user_id"] = user.id  # 將user_id寫入session, 後面用戶判斷用戶是否登錄
        session["username"] = user.username  # 將user_id寫入session, 後面用戶判斷用戶是否登錄
        return redirect(url_for("index"))  # 登錄成功，跳轉到首頁

    return render_template("home/login.html", form=form)  # 渲染登錄頁面模板


@app.route("/register/", methods=["GET", "POST"])
def register():
    """
    註冊功能
    """
    if "user_id" in session:
        return redirect(url_for("index"))
    form = RegisterForm()  # 導入註冊表單
    if form.validate_on_submit():  # 提交註冊表單
        data = form.data  # 接收表單數據
        # 為User類屬性賦值
        user = User(
            username=data["username"],  # 用戶名
            email=data["email"],  # 郵箱
            password=generate_password_hash(data["password"]),  # 對密碼加密
        )
        db.session.add(user)  # 添加數據
        db.session.commit()  # 提交數據
        return redirect(url_for("login"))  # 登錄成功，跳轉到首頁
    return render_template("home/register.html", form=form)  # 渲染模板


@app.route("/logout/")
def logout():
    """
    退出登錄
    """
    # 重定向到home模塊下的登錄。
    session.pop("user_id", None)
    session.pop("username", None)
    return redirect(url_for('index'))


@app.route("/modify_password/", methods=["GET", "POST"])
@user_login
def modify_password():
    """
    修改密碼
    """
    form = PasswordForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(username=session["username"]).first()
        from werkzeug.security import generate_password_hash
        user.password = generate_password_hash(data["password"])
        db.session.add(user)
        db.session.commit()
        return "<script>alert('密碼修改成功');location.href='/';</script>"
    return render_template("home/modify_password.html", form=form)

@app.route("/")
@app.route("/index/")
def index():
    """
    首頁
    """
    # 獲取2個熱門商品
    hot_goods = Goods.query.order_by(Goods.views_count.desc()).limit(2).all()
    # 獲取12個新品
    new_goods = Goods.query.filter_by(is_new=1).order_by(
        Goods.addtime.desc()
    ).limit(12).all()
    # 獲取12個打折商品
    sale_goods = Goods.query.filter_by(is_sale=1).order_by(
        Goods.addtime.desc()
    ).limit(12).all()
    return render_template('home/index.html', new_goods=new_goods, sale_goods=sale_goods, hot_goods=hot_goods)  # 渲染模板

@app.route('/user/')
@user_login
def user():
    user_id=session.get('user_id,0')
    return render_template('home/user.html')

@app.route('/recommand/')
def recommand():
    return render_template('home/recommand.html')


@app.route('/knowledge/')
def knowledge():
    return render_template('home/knowledge.html')

@app.route("/goods_list/<int:supercat_id>/")
def goods_list(supercat_id=None):  # supercat_id 為商品大分類ID
    """
    商品頁
    """
    page = request.args.get('page', 1, type=int)  # 獲取page參數值
    page_data = Goods.query.filter_by(supercat_id=supercat_id).paginate(page=page, per_page=12)
    hot_goods = Goods.query.filter_by(supercat_id=supercat_id).order_by(Goods.views_count.desc()).limit(7).all()
    return render_template('home/goods_list.html', page_data=page_data, hot_goods=hot_goods, supercat_id=supercat_id)


@app.route("/goods_detail/<int:id>/")
def goods_detail(id=None):  # id 為商品ID
    """
    詳情頁
    """
    user_id = session.get('user_id', 0)  # 獲取用戶ID,判斷用戶是否登錄
    goods = Goods.query.get_or_404(id)  # 根據景區ID獲取景區數據，如果不存在返回404
    # 瀏覽量加1
    goods.views_count += 1
    db.session.add(goods)  # 添加數據
    db.session.commit()  # 提交數據
    # 獲取左側熱門商品
    hot_goods = Goods.query.filter_by(subcat_id=goods.subcat_id).order_by(Goods.views_count.desc()).limit(5).all()
    # 獲取底部相關商品
    similar_goods = Goods.query.filter_by(subcat_id=goods.subcat_id).order_by(Goods.addtime.desc()).limit(5).all()
    return render_template('home/goods_detail.html', goods=goods, hot_goods=hot_goods, similar_goods=similar_goods,
                           user_id=user_id)  # 渲染模板


@app.route("/search/")
def goods_search():
    """
    搜素功能
    """
    page = request.args.get('page', 1, type=int)  # 獲取page參數值
    keywords = request.args.get('keywords', '', type=str)

    if keywords:
        # 使用like實現模糊查詢
        page_data = Goods.query.filter(Goods.name.like("%" + keywords + "%")).order_by(
            Goods.addtime.desc()
        ).paginate(page=page, per_page=12)
    else:
        page_data = Goods.query.order_by(
            Goods.addtime.desc()
        ).paginate(page=page, per_page=12)
    hot_goods = Goods.query.order_by(Goods.views_count.desc()).limit(7).all()
    return render_template("home/goods_search.html", page_data=page_data, keywords=keywords, hot_goods=hot_goods)


@app.route("/cart_add/")
@user_login
def cart_add():
    """
    添加購物車
    """
    cart = Cart(
        goods_id=request.args.get('goods_id'),
        number=request.args.get('number'),
        user_id=session.get('user_id', 0)  # 獲取用戶ID,判斷用戶是否登錄
    )
    db.session.add(cart)  # 添加數據
    db.session.commit()  # 提交數據
    return redirect(url_for('shopping_cart'))


@app.route("/cart_clear/")
@user_login
def cart_clear():
    """
    清空購物車
    """
    user_id = session.get('user_id', 0)  # 獲取用戶ID,判斷用戶是否登錄
    Cart.query.filter_by(user_id=user_id).update({'user_id': 0})
    db.session.commit()
    return redirect(url_for('shopping_cart'))


@app.route("/shopping_cart/")
@user_login
def shopping_cart():
    user_id = session.get('user_id', 0)
    cart = Cart.query.filter_by(user_id=int(user_id)).order_by(Cart.addtime.desc()).all()
    if cart:
        return render_template('home/shopping_cart.html', cart=cart)
    else:
        return render_template('home/empty_cart.html')


@app.route("/cart_order/", methods=['GET', 'POST'])
@user_login
def cart_order():
    if request.method == 'POST':
        user_id = session.get('user_id', 0)  # 獲取用戶id
        # 添加訂單
        orders = Orders(
            user_id=user_id,
            recevie_name=request.form.get('recevie_name'),
            recevie_tel=request.form.get('recevie_tel'),
            recevie_address=request.form.get('recevie_address'),
            remark=request.form.get('remark')
        )
        db.session.add(orders)  # 添加數據
        db.session.commit()  # 提交數據
        # 添加訂單詳情
        cart = Cart.query.filter_by(user_id=user_id).all()
        object = []
        for item in cart:
            object.append(
                OrdersDetail(
                    order_id=orders.id,
                    goods_id=item.goods_id,
                    number=item.number, )
            )
        db.session.add_all(object)
        # 更改購物車狀態
        Cart.query.filter_by(user_id=user_id).update({'user_id': 0})
        db.session.commit()
    return redirect(url_for('index'))


@app.route("/order_list/", methods=['GET', 'POST'])
@user_login
def order_list():
    """"
    我的訂單
    """
    user_id = session.get('user_id', 0)
    orders = OrdersDetail.query.join(Orders).filter(Orders.user_id == user_id).order_by(Orders.addtime.desc()).all()
    return render_template('home/order_list.html', orders=orders)


# -------------------------------------------------------------------
def admin_login(f):
    """
    登錄裝飾器
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("a_login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/admin/")
@admin_login
def a_index():
    page = request.args.get('page', 1, type=int)  # 獲取page參數值
    page_data = Goods.query.order_by(
        Goods.addtime.desc()
    ).paginate(page=page, per_page=10)
    return render_template("admin/index.html", page_data=page_data)


@app.route("/admin/goods/add/", methods=["GET", "POST"])
@admin_login
def a_goods_add():
    """
    添加商品
    """
    form = GoodsForm()  # 實例化form表單
    supercat_list = [(v.id, v.cat_name) for v in SuperCat.query.all()]  # 為super_cat_id添加屬性
    form.supercat_id.choices = supercat_list  # 為super_cat_id添加屬性
    form.subcat_id.choices = [(v.id, v.cat_name) for v in
                              SubCat.query.filter_by(super_cat_id=supercat_list[0][0]).all()]  # 為super_cat_id添加屬性
    form.current_price.data = form.data['original_price']  # 為current_pirce 賦值
    if form.validate_on_submit():  # 添加商品情況
        data = form.data
        goods = Goods(
            name=data["name"],
            supercat_id=int(data['supercat_id']),
            subcat_id=int(data['subcat_id']),
            picture=data["picture"],
            original_price=Decimal(data["original_price"]).quantize(Decimal('0.00')),  # 轉化為包含2位小數的形式
            current_price=Decimal(data["original_price"]).quantize(Decimal('0.00')),  # 轉化為包含2位小數的形式
            is_new=int(data["is_new"]),
            is_sale=int(data["is_sale"]),
            introduction=data["introduction"],
        )
        db.session.add(goods)  # 添加數據
        db.session.commit()  # 提交數據
        return redirect(url_for('a_index'))  # 頁面跳轉
    return render_template("admin/goods_add.html", form=form)  # 渲染模板


@app.route("/admin/goods/detail/", methods=["GET", "POST"])
@admin_login
def a_goods_detail():
    goods_id = request.args.get('goods_id')
    goods = Goods.query.filter_by(id=goods_id).first_or_404()
    return render_template('admin/goods_detail.html', goods=goods)


@app.route("/admin/goods/edit/<int:id>", methods=["GET", "POST"])
@admin_login
def a_goods_edit(id=None):
    """
    編輯商品
    """
    goods = Goods.query.get_or_404(id)
    form = GoodsForm()  # 實例化form表單
    form.supercat_id.choices = [(v.id, v.cat_name) for v in SuperCat.query.all()]  # 為super_cat_id添加屬性
    form.subcat_id.choices = [(v.id, v.cat_name) for v in
                              SubCat.query.filter_by(super_cat_id=goods.supercat_id).all()]  # 為super_cat_id添加屬性

    if request.method == "GET":
        form.name.data = goods.name
        form.picture.data = goods.picture
        form.current_price.data = goods.current_price
        form.original_price.data = goods.original_price
        form.supercat_id.data = goods.supercat_id
        form.subcat_id.data = goods.subcat_id
        form.is_new.data = goods.is_new
        form.is_sale.data = goods.is_sale
        form.introduction.data = goods.introduction
    elif form.validate_on_submit():
        goods.name = form.data["name"]
        goods.supercat_id = int(form.data['supercat_id'])
        goods.subcat_id = int(form.data['subcat_id'])
        goods.picture = form.data["picture"]
        goods.original_price = Decimal(form.data["original_price"]).quantize(Decimal('0.00'))
        goods.current_price = Decimal(form.data["current_price"]).quantize(Decimal('0.00'))
        goods.is_new = int(form.data["is_new"])
        goods.is_sale = int(form.data["is_sale"])
        goods.introduction = form.data["introduction"]
        db.session.add(goods)  # 添加數據
        db.session.commit()  # 提交數據
        return redirect(url_for('a_index'))  # 頁面跳轉

    return render_template("admin/goods_edit.html", form=form)  # 渲染模板


@app.route("/admin/goods/select_sub_cat/", methods=["GET"])
@admin_login
def a_select_sub_cat():
    """
    查找子分類
    """
    super_id = request.args.get("super_id", "")  # 接收傳遞的參數super_id
    subcat = SubCat.query.filter_by(super_cat_id=super_id).all()
    result = {}
    if subcat:
        data = []
        for item in subcat:
            data.append({'id': item.id, 'cat_name': item.cat_name})
        result['status'] = 1
        result['message'] = 'ok'
        result['data'] = data
    else:
        result['status'] = 0
        result['message'] = 'error'
    return jsonify(result)  # 返回json數據


@app.route("/admin/goods/del_confirm/")
@admin_login
def a_goods_del_confirm():
    '''確認刪除商品'''
    goods_id = request.args.get('goods_id')
    goods = Goods.query.filter_by(id=goods_id).first_or_404()
    return render_template('admin/goods_del_confirm.html', goods=goods)


@app.route("/admin/goods/del/<int:id>/", methods=["GET"])
@admin_login
def a_goods_del(id=None):
    """
    刪除商品
    """
    goods = Goods.query.get_or_404(id)  # 根據景區ID查找數據
    db.session.delete(goods)  # 刪除數據
    db.session.commit()  # 提交數據
    return redirect(url_for('a_index', page=1))  # 渲染模板


@app.route("/admin/login/", methods=["GET", "POST"])
def a_login():
    """
    登錄功能
    """
    # 判斷是否已經登錄
    if "admin" in session:
        return redirect(url_for("a_index"))
    form = MLoginForm()  # 實例化登錄表單
    if form.validate_on_submit():  # 驗證提交表單
        data = form.data  # 接收數據
        admin = Admin.query.filter_by(manager=data["manager"]).first()  # 查找Admin表數據
        # 密碼錯誤時，check_password,則此時not check_password(data["pwd"])為真。
        # if not admin.check_password(data["password"]):
        #     flash("密碼錯誤!", "err")  # 閃存錯誤信息
        #     return redirect(url_for("a_login"))  # 跳轉到後台登錄頁
        # 如果是正確的，就要定義session的會話進行保存。
        session["admin"] = data["manager"]  # 存入session
        session["admin_id"] = admin.id  # 存入session
        return redirect(url_for("a_index"))  # 返回後台主頁
    return render_template("admin/login.html", form=form)


@app.route('/logout/')
@admin_login
def a_logout():
    """
    後台註銷登錄
    """
    session.pop("admin", None)
    session.pop("admin_id", None)
    return redirect(url_for("a_login"))


@app.route("/user/list/", methods=["GET"])
@admin_login
def a_user_list():
    """
    會員列表
    """
    page = request.args.get('page', 1, type=int)  # 獲取page參數值
    keyword = request.args.get('keyword', '', type=str)
    if keyword:
        # 根據姓名或者郵箱查詢
        filters = or_(User.username == keyword, User.email == keyword)
        page_data = User.query.filter(filters).order_by(
            User.addtime.desc()
        ).paginate(page=page, per_page=5)
    else:
        page_data = User.query.order_by(
            User.addtime.desc()
        ).paginate(page=page, per_page=5)

    return render_template("admin/user_list.html", page_data=page_data)


@app.route("/user/view/<int:id>/", methods=["GET"])
@admin_login
def a_user_view(id=None):
    """
    查看會員詳情
    """
    from_page = request.args.get('fp')
    if not from_page:
        from_page = 1
    user = User.query.get_or_404(int(id))
    return render_template("admin/user_view.html", user=user, from_page=from_page)


@app.route('/supercat/add/', methods=["GET", "POST"])
@admin_login
def a_supercat_add():
    """
    添加大分類
    """
    if request.method == 'POST':
        cat_name = request.form['cat_name']
        supercat = SuperCat.query.filter_by(cat_name=cat_name).count()
        if supercat:
            flash("大分類已存在", "err")
            return redirect(url_for("a_supercat_add"))
        data = SuperCat(
            cat_name=cat_name,
        )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for("a_supercat_list"))
    return render_template("admin/supercat_add.html")


@app.route("/supercat/list/", methods=["GET"])
@admin_login
def a_supercat_list():
    """
    大分類列表
    """
    data = SuperCat.query.order_by(
        SuperCat.addtime.desc()
    ).all()
    return render_template("admin/supercat.html", data=data)  # 渲染模板


@app.route("/supercat/del/", methods=["POST"])
@admin_login
def a_supercat_del():
    """
    大分類刪除
    """
    if request.method == 'POST':
        cat_ids = request.form.getlist("delid")  # cat_ids 是一個列表
        # 判斷是否有子類
        for id in cat_ids:
            count = SubCat.query.filter_by(super_cat_id=id).count()
            if count:
                return "大分類下有小分類，請先刪除小分類"
        # 使用in_ 方式批量刪除，需要設置synchronize_session為False,而 in 操作估計還不支持
        # 解決辦法就是刪除時不進行同步，然後再讓 session 里的所有實體都過期
        db.session.query(SuperCat).filter(SuperCat.id.in_(cat_ids)).delete(synchronize_session=False)
        db.session.commit()
        return redirect(url_for("a_supercat_list"))


@app.route("/subcat/list/", methods=["GET"])
@admin_login
def a_subcat_list():
    """
    小分類
    """
    data = SubCat.query.order_by(
        SubCat.addtime.desc()
    ).all()
    return render_template("admin/subcat.html", data=data)  # 渲染模板


@app.route('/subcat/add/', methods=["GET", "POST"])
@admin_login
def a_subcat_add():
    """
    添加小分類
    """
    if request.method == 'POST':
        cat_name = request.form['cat_name']
        super_cat_id = request.form['super_cat_id']
        # 檢測名稱是否存在
        subcat = SubCat.query.filter_by(cat_name=cat_name).count()
        if subcat:
            return "<script>alert('該小分類已經存在');history.go(-1);</script>"
        # 組織數據
        data = SubCat(
            super_cat_id=super_cat_id,
            cat_name=cat_name,
        )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for("a_subcat_list"))

    supercat = SuperCat.query.all()  # 獲取大分類信息
    return render_template("admin/subcat_add.html", supercat=supercat)


@app.route("/subcat/del/", methods=["POST"])
@admin_login
def a_subcat_del():
    """
    刪除小分類
    """
    if request.method == 'POST':
        cat_ids = request.form.getlist("delid")  # cat_ids 是一個列表
        # 判斷子類下是否有商品
        for id in cat_ids:
            count = Goods.query.filter_by(cat_id=id).count()
            if count:
                return "<script>alert('該分類下有商品，請先刪除分類下的商品');history.go(-1);</script>"
        # 使用in_ 方式批量刪除，需要設置synchronize_session為False,而 in 操作估計還不支持
        # 解決辦法就是刪除時不進行同步，然後再讓 session 里的所有實體都過期
        db.session.query(SubCat).filter(SubCat.id.in_(cat_ids)).delete(synchronize_session=False)
        db.session.commit()
        return redirect(url_for("a_subcat_list"))



@app.route("/orders/list/", methods=["GET"])
@admin_login
def a_orders_list():
    """
    訂單列表頁面
    """
    keywords = request.args.get('keywords', '', type=str)
    page = request.args.get('page', 1, type=int)  # 獲取page參數值
    if keywords:
        page_data = Orders.query.filter_by(id=keywords).order_by(
            Orders.addtime.desc()
        ).paginate(page=page, per_page=10)
    else:
        page_data = Orders.query.order_by(
            Orders.addtime.desc()
        ).paginate(page=page, per_page=10)
    return render_template("admin/orders_list.html", page_data=page_data)


@app.route("/orders/detail/", methods=["GET"])
@admin_login
def a_orders_detail():
    """
    訂單詳情
    """
    order_id = request.args.get('order_id')
    orders = OrdersDetail.query.join(Orders).filter(OrdersDetail.order_id == order_id).all()
    return render_template('admin/orders_detail.html', data=orders)


@app.route('/topgoods/', methods=['GET'])
@admin_login
def a_topgoods():
    """
    銷量排行榜(前10位)
    """
    orders = OrdersDetail.query.order_by(OrdersDetail.number.desc()).limit(10).all()
    return render_template("admin/topgoods.html", data=orders)


if __name__ == '__main__':
    app.run(debug=True)
