from flask import Flask, jsonify, render_template,request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

# 這裡設定 DEBUG 為 TRUE 的話，更新程式碼就不用一直重啟 flask 伺服器了
# 更新 python 程式碼存檔之後，直接重新整理網頁即可。
app.config['DEBUG']=True

CORS(app, resources={r"./*":{"origins":["*"]}})

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='',
    database='shop',
    charset='utf8mb4'
)

cursor = db.cursor()

@app.route('/', methods=['POST','GET'])
def home():
    return render_template("recommand.html")

# @app.route('/feature', methods=['POST','GET'])
# def feature():
#     if request.method == "POST":
#         # income=request.values.get('income')
#         # sex=request.values.get('sex')
#         # material=request.values.get('material')
#         # brand=request.values.get('brand')
#         # color=request.values.get('color')
#         # price=request.values.get('price')
#         # age=request.values.get('age')
        
#         sql = f'SELECT * FROM `custom_feature`'
#         cursor.execute(sql)
#         feature = []
#         if cursor.rowcount > 0:
#             result = cursor.fetchall()
#             for i in result:
#                 income = i[0]
#                 sex = i[1]
#                 material = i[2]
#                 brand = i[3]
#                 color = i[4]
#                 price = i[5]
#                 age = i[6]
#                 feature.append({'income':income, 'sex':sex, 'brand':brand,'material':material, 'color':color, 'price':price, 'age':age})
#         print('ok')
#         print(feature)
#         return render_template('rec.html', feature=feature)

#     else:
#         return render_template("recommand.html")

@app.route('/newfeature',methods=['POST'])
def newfeature():
    res = {"success":False, "info":"寫入失敗"}
    try:
        sql = 'INSERT INTO `custom_feature` (`income`, `sex`, `brand`, `material`, `color`, `price`, `age`) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (request.
        json['income'], request.json['sex'],request.json['brand'],request.json['material'],request.json['color'],request.json['price'],request.json['age']))

        if cursor.rowcount > 0:

            res['success'] = True
            res['info'] = '新增成功'

        else:
            res['info'] = '新增失敗'

        db.commit()

    except Exception as e:
        db.rollback()
        res['info']= f'SQL 寫入失敗: {e}'

    return jsonify(res)
        

@app.route('/shop/read',methods=['GET'])
def shopread():
    res = {"success":False, "info":"查詢失敗"}
    whereSqlString = ' WHERE ';

    for key, value in list(request.args.lists()):
        if value[0] :
            whereSqlString += f'`{key}`="{value[0]}" OR '

    finalSQL = whereSqlString[:-3]

    try:
        sql = f'SELECT * FROM `custom_feature` {finalSQL}'
        cursor.execute(sql)

        if cursor.rowcount > 0:
            result = cursor.fetchall()

            res['success'] = True
            res['info'] = '查詢成功'
            res['result'] = result
        else:
            res['info'] = '查無資料'

        db.commit()

    except Exception as e:
        db.rollback()
        res['info']= f'SQL 執行失敗: {e}'

    return jsonify(res)

app.run()