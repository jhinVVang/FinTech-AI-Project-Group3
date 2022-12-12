from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from datetime import datetime
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/shop'
# 設置自動追蹤
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 自動提交數據到數據庫
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config["SECRET_KEY"] = "12345678"

db = SQLAlchemy(app)


# 會員數據模型
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 編號
    username = db.Column(db.String(100))  # 用戶名
    password = db.Column(db.String(100))  # 密碼
    email = db.Column(db.String(100), unique=True)  # 郵箱
    consumption = db.Column(db.DECIMAL(10, 2), default=0)  # 消費額
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 註冊時間
    orders = db.relationship('Orders', backref='user')  # 訂單外鍵關系關聯

    def __repr__(self):
        return '<User %r>' % self.name

    def check_password(self, password):
        """
        檢測密碼是否正確
        :param password: 密碼
        :return: 返回布爾值
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)


# 管理員
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 編號
    manager = db.Column(db.String(100), unique=True)  # 管理員帳號
    password = db.Column(db.String(100))  # 管理員密碼

    def __repr__(self):
        return "<Admin %r>" % self.manager

    def check_password(self, password):
        """
        檢測密碼是否正確
        :param password: 密碼
        :return: 返回布爾值
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)


# 大分類
class SuperCat(db.Model):
    __tablename__ = "supercat"
    id = db.Column(db.Integer, primary_key=True)  # 編號
    cat_name = db.Column(db.String(100))  # 大分類名稱
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加時間
    subcat = db.relationship("SubCat", backref='supercat')  # 外鍵關系關聯
    goods = db.relationship("Goods", backref='supercat')  # 外鍵關系關聯

    def __repr__(self):
        return "<SuperCat %r>" % self.cat_name


# 子分類
class SubCat(db.Model):
    __tablename__ = "subcat"
    id = db.Column(db.Integer, primary_key=True)  # 編號
    cat_name = db.Column(db.String(100))  # 子分類名稱
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加時間
    super_cat_id = db.Column(db.Integer, db.ForeignKey('supercat.id'))  # 所屬大分類
    goods = db.relationship("Goods", backref='subcat')  # 外鍵關系關聯

    def __repr__(self):
        return "<SubCat %r>" % self.cat_name


# 商品
class Goods(db.Model):
    __tablename__ = "goods"
    id = db.Column(db.Integer, primary_key=True)  # 編號
    name = db.Column(db.String(255))  # 名稱
    original_price = db.Column(db.DECIMAL(10, 2))  # 原價
    current_price = db.Column(db.DECIMAL(10, 2))  # 現價
    picture = db.Column(db.String(255))  # 圖片
    introduction = db.Column(db.Text)  # 商品簡介
    views_count = db.Column(db.Integer, default=0)  # 瀏覽次數
    is_sale = db.Column(db.Boolean(), default=0)  # 是否特價
    is_new = db.Column(db.Boolean(), default=0)  # 是否新品

    # 設置外鍵
    supercat_id = db.Column(db.Integer, db.ForeignKey('supercat.id'))  # 所屬大分類
    subcat_id = db.Column(db.Integer, db.ForeignKey('subcat.id'))  # 所屬小分類
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加時間
    cart = db.relationship("Cart", backref='goods')  # 訂單外鍵關系關聯
    orders_detail = db.relationship("OrdersDetail", backref='goods')  # 訂單外鍵關系關聯

    def __repr__(self):
        return "<Goods %r>" % self.name


# 購物車
class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)  # 編號
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'))  # 所屬商品
    user_id = db.Column(db.Integer)  # 所屬用戶
    number = db.Column(db.Integer, default=0)  # 購買數量
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加時間

    def __repr__(self):
        return "<Cart %r>" % self.id


# 訂單
class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)  # 編號
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所屬用戶
    recevie_name = db.Column(db.String(255))  # 收款人姓名
    recevie_address = db.Column(db.String(255))  # 收款人地址
    recevie_tel = db.Column(db.String(255))  # 收款人電話
    remark = db.Column(db.String(255))  # 備注信息
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加時間
    orders_detail = db.relationship("OrdersDetail", backref='orders')  # 外鍵關系關聯

    def __repr__(self):
        return "<Orders %r>" % self.id


# 訂單詳情
class OrdersDetail(db.Model):
    __tablename__ = 'orders_detail'
    id = db.Column(db.Integer, primary_key=True)  # 編號
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'))  # 所屬商品
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))  # 所屬訂單
    number = db.Column(db.Integer, default=0)  # 購買數量


