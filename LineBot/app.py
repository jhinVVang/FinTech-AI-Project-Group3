from __future__ import unicode_literals
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
import json
import configparser
import os
from urllib import parse
app = Flask(__name__, static_url_path='/static')
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])


config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))
my_line_id = config.get('line-bot', 'my_line_id')
end_point = config.get('line-bot', 'end_point')
line_login_id = config.get('line-bot', 'line_login_id')
line_login_secret = config.get('line-bot', 'line_login_secret')
my_phone = config.get('line-bot', 'my_phone')
HEADER = {
    'Content-type': 'application/json',
    'Authorization': F'Bearer {config.get("line-bot", "channel_access_token")}'
}


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return 'ok'
    body = request.json
    events = body["events"]
    print(body)
    if "replyToken" in events[0]:
        payload = dict()
        replyToken = events[0]["replyToken"]
        payload["replyToken"] = replyToken
        if events[0]["type"] == "message":
            if events[0]["message"]["type"] == "text":
                text = events[0]["message"]["text"]

                if text == "我的名字":
                    payload["messages"] = [getNameEmojiMessage()]
                elif text == "出去玩囉":
                    payload["messages"] = [getPlayStickerMessage()]
                elif text == "quota":
                    payload["messages"] = [
                            {
                                "type": "text",
                                "text": getTotalSentMessageCount()
                            }
                        ]
                elif text == "送禮推薦":
                    payload["messages"] = [getfestivalproductMessage()]
                elif text == "優惠活動":
                    payload["messages"] = [getbonusImageMessage(),
                                           getbonus2ImageMessage()]
                elif text == "新品介紹":
                    payload["messages"] = [getnewproductMessage()]
                elif text == "製作者名單":
                    payload["messages"] = [getproducerCarouselMessage()]
                elif text == "預約鑑賞":
                    data = {
                            "action" : 'reserve'
                        }
                    payload["messages"] = [getReservedConfirmMessage(data)]
                else:
                    payload["messages"] = [
                            {
                                "type": "text",
                                "text": text
                            }
                        ]
                replyMessage(payload)
        elif events[0]["type"] == "postback":
            if "params" in events[0]["postback"]:
                reservedTime = events[0]["postback"]["params"]["datetime"].replace("T", " ")
                payload["messages"] = [
                        {
                            "type": "text",
                            "text": F"已預約於{reservedTime}的鑑賞服務。"
                        }
                    ]
                replyMessage(payload)
            else:
                data = json.loads(events[0]["postback"]["data"])
                action = data["action"]
                if action == "reserve":
                    data["action"] = "get_detail"
                    payload["messages"] = [getReserveMessage(data)]
                elif action == "get_detail":
                    del data["action"]
                    payload["messages"] = [getCallCarMessage(data)]
                replyMessage(payload)

    return 'OK'


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    line_bot_api.reply_message( #呼叫回傳訊息功能
        event.reply_token, #呼叫回傳訊息功能
        TextSendMessage(text=event.message.text) #將輸入的訊息回傳
        )


@app.route("/sendTextMessageToMe", methods=['POST'])
def sendTextMessageToMe():
    pushMessage({}) #傳遞訊息
    return 'OK'


def getNameEmojiMessage():
    lookUpStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    productId = "5ac21a8c040ab15980c9b43f" 
    name = "Sylvia"
    message = dict()
    message['type'] = 'text'
    message['text'] = "".join('$' for _ in range(len(name)))
    emoji_list = list()
    for n_char_index in range(len(name)):
        emoji_list.append({
            "index":n_char_index,
            "productId":productId,
            "emojiId":f"{lookUpStr.index(name[n_char_index]) + 1:03d}"
            })
    message['emojis'] = emoji_list
    print(message)
    return message


def getnewproductMessage():
    message = {
        "type": "template",
        "altText": "this is a carousel template",
        "template": {
            "type": "carousel",
            "columns": [
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/47.jpg",
                "imageBackgroundColor": "#000000",
                "title": "Bracelet",
                "text": "鑽石手環帶來亮眼璀璨與雅緻風格，體現經典華麗魅力。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/222"
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/5.jpg",
                "imageBackgroundColor": "#000000",
                "title": "Ring",
                "text": "採用時尚的混合切割方式，將階梯式切割的冠部與明亮式切割的底部相結合。十分適合追求現代感戒指款式者。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/222"
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/35.jpg",
                "imageBackgroundColor": "#000000",
                "title": "Earrings",
                "text": "使用精緻優質的鑽石，優美細膩的設計，最適合送給甜美可愛的她。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/222"
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/23.jpg",
                "imageBackgroundColor": "#FFFFFF",
                "title": "Necklace",
                "text": "獨特的高級鑽石珠寶作品融匯了女性優雅與性感的元素演繹您對生活品味的璀璨的想望。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/123"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=111"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/111"
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/3.jpg",
                "imageBackgroundColor": "#000000",
                "title": "Ring",
                "text": "18K金戒指鑲嵌天然鑽石，在簡單中營造獨特。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/222"
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/49.jpg",
                "imageBackgroundColor": "#000000",
                "title": "Link",
                "text": "在一年四季中，隨意搭配一件簡單亮眼的配件，立刻帶出時尚氣息。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/222"
                }
                ]
            }
            ],
            "imageAspectRatio": "rectangle",
            "imageSize": "cover"
        }
    }
    return message


def getfestivalproductMessage():
    message = {
        "type": "template",
        "altText": "this is a carousel template",
        "template": {
            "type": "carousel",
            "columns": [
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/23.jpg",
                "imageBackgroundColor": "#FFFFFF",
                "title": "Necklace",
                "text": "獨特的高級鑽石珠寶作品融匯了女性優雅與性感的元素演繹您對生活品味的璀璨的想望。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/123"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=111"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/111"
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/35.jpg",
                "imageBackgroundColor": "#000000",
                "title": "Earrings",
                "text": "使用精緻優質的鑽石，優美細膩的設計，最適合送給甜美可愛的她。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/222"
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/47.jpg",
                "imageBackgroundColor": "#000000",
                "title": "Bracelet",
                "text": "鑽石手環帶來亮眼璀璨與雅緻風格，體現經典華麗魅力。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/222"
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/3.jpg",
                "imageBackgroundColor": "#000000",
                "title": "Ring",
                "text": "18K金戒指鑲嵌天然鑽石，在簡單中營造獨特。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/222"
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/49.jpg",
                "imageBackgroundColor": "#000000",
                "title": "Link",
                "text": "在一年四季中，隨意搭配一件簡單亮眼的配件，立刻帶出時尚氣息。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/222"
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/jewelry/5.jpg",
                "imageBackgroundColor": "#000000",
                "title": "Ring",
                "text": "採用時尚的混合切割方式，將階梯式切割的冠部與明亮式切割的底部相結合。十分適合追求現代感戒指款式者。",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "立即購買",
                    "data": "action=buy&itemid=222"
                },
                {
                    "type": "uri",
                    "label": "查看更多",
                    "uri": "http://example.com/page/222"
                }
                ]
            }
            ],
            "imageAspectRatio": "rectangle",
            "imageSize": "cover"
        }
    }
    return message

def getproducerCarouselMessage():
    message = {
  "type": "template",
  "altText": "this is a image carousel template",
  "template": {
    "type": "image_carousel",
    "columns": [
      {
        "imageUrl": F"{end_point}/static/producer/1.jpg",
        "action": {
          "type": "message",    
          "label": "組長:王浩晉",
          "text": "王浩晉"
        }
      },
      {
        "imageUrl": F"{end_point}/static/producer/2.jpg",
        "action": {
          "type": "message",
          "label": "譚逸翔",
          "text": "譚逸翔"
        }
      },
      {
        "imageUrl": F"{end_point}/static/producer/3.jpg",
        "action": {
          "type": "message",
          "label": "鄭筑馨",
          "text": "鄭筑馨"
        }
      },
      {
        "imageUrl": F"{end_point}/static/producer/4.jpg",
        "action": {
          "type": "message",
          "label": "李伊淇",
          "text": "李伊淇"
        }
      },
      {
        "imageUrl": F"{end_point}/static/producer/5.jpg",
        "action": {
          "type": "message",
          "label": "鄒蕙安",
          "text": "鄒蕙安"
        }
      }
    ]
  }
}
    return message


# def getCarouselMessage(data):
#     message = {
#   "type": "template",
#   "altText": "this is a image carousel template",
#   "template": {
#     "type": "image_carousel",
#     "columns": [
#       {
#         "imageUrl": F"{end_point}/static/shop/1.jpg",
#         "action": {
#           "type": "postback",
#           "label": "1號店",
#           "data": json.dumps(data)
#         }
#       },
#       {
#         "imageUrl": F"{end_point}/static/shop/2.jpg",
#         "action": {
#           "type": "postback",
#           "label": "2號店",
#           "data": json.dumps(data)
#         }
#       }
#     ]
#   }
# }
#     return message

def getReserveMessage(data):
    message = {
        "type": "template",
        "altText": "this is a carousel template",
        "template": {
            "type": "carousel",
            "columns": [
            {
                "thumbnailImageUrl": F"{end_point}/static/shop/1.jpg",
                "imageBackgroundColor": "#FFFFFF",
                "title": "1號店",
                "text": "地址：台北市大安區復興南路二段237號4樓",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/123"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "預約鑑賞",
                    "data": json.dumps(data)
                }
                ]
            },
            {
                "thumbnailImageUrl": F"{end_point}/static/shop/2.jpg",
                "imageBackgroundColor": "#000000",
                "title": "2號店",
                "text": "地址：台北市大安區和平東路二段106號",
                "defaultAction": {
                "type": "uri",
                "label": "查看更多",
                "uri": "http://example.com/page/222"
                },
                "actions": [
                {
                    "type": "postback",
                    "label": "預約鑑賞",
                    "data": json.dumps(data)
                }
                ]
            }
            ],
            "imageAspectRatio": "rectangle",
            "imageSize": "cover"
        }
    }
    return message

def getReservedConfirmMessage(data):
    data = {
        "action" : 'reserve'
    }
    message = {
      "type": "template",
      "altText": "確認預約",
      "template": {
        "type": "confirm",
        "text": f'是否要預約鑑賞服務？',
        "actions": [
            {
                "type": "postback",
                "label": "是",
                "data": json.dumps(data),
            },
            {
                "type": "message",
                "label": "否",
                "text": "否"
            }
        ]
    }
    }
    return message


def getCallCarMessage(data):
    message = {
    "type": "template",
    "altText": "This is a buttons template",
    "template": {
        "type": "buttons",
        "text": f"請選擇預約鑑賞時間",
        "actions": [
           {
            "type": "datetimepicker",
            "label": "預約",
            "data": json.dumps(data),
            "mode": "datetime"
            }
        ]
    }
}
    return message


def getPlayStickerMessage():
    message = {
    "type": "sticker",
    "packageId": "446",
    "stickerId": "1988"
    }
    return message



def getbonusImageMessage(originalContentUrl=F"{end_point}/static/bonus/1.png"):
    return getImageMessage(originalContentUrl)

def getbonus2ImageMessage(originalContentUrl=F"{end_point}/static/bonus/3.png"):
    return getImageMessage(originalContentUrl)

def getImageMessage(originalContentUrl):
    message = dict()
    message["type"] = "image"
    message["originalContentUrl"] = originalContentUrl
    message["previewImageUrl"] = originalContentUrl
    return message


def replyMessage(payload):
    r = requests.post('https://api.line.me/v2/bot/message/reply', data=json.dumps(payload), headers=HEADER)
    print(r.content)
    return 'OK'

def pushMessage(payload):
    r = requests.post('https://api.line.me/v2/bot/message/push', data=json.dumps(payload), headers=HEADER)
    print(r.content)
    return 'OK'


def getTotalSentMessageCount():
    response = requests.get('https://api.line.me/v2/bot/message/quota/consumption', headers=HEADER)
    return F"總共使用了{response.json()['totalUsage']}則"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload_file', methods=['POST'])
def upload_file():
    payload = dict()
    if request.method == 'POST':
        file = request.files['file']
        print("json:", request.json)
        form = request.form
        age = form['age']
        gender = ("男" if form['gender'] == "M" else "女") + "性"
        if file:
            filename = file.filename
            img_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(img_path)
            print(img_path)
            payload["to"] = my_line_id
            payload["messages"] = [getImageMessage(F"{end_point}/{img_path}"),
                {
                    "type": "text",
                    "text": F"年紀：{age}\n性別：{gender}"
                }
            ]
            pushMessage(payload)
    return 'OK'


@app.route('/line_login', methods=['GET'])
def line_login():
    if request.method == 'GET':
        code = request.args.get("code", None)
        state = request.args.get("state", None)

        if code and state:
            HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
            url = "https://api.line.me/oauth2/v2.1/token"
            FormData = {"grant_type": 'authorization_code', "code": code, "redirect_uri": F"{end_point}/line_login", "client_id": line_login_id, "client_secret":line_login_secret}
            data = parse.urlencode(FormData)
            content = requests.post(url=url, headers=HEADERS, data=data).text
            content = json.loads(content)
            url = "https://api.line.me/v2/profile"
            HEADERS = {'Authorization': content["token_type"]+" "+content["access_token"]}
            content = requests.get(url=url, headers=HEADERS).text
            content = json.loads(content)
            name = content["displayName"]
            userID = content["userId"]
            pictureURL = content["pictureUrl"]
            statusMessage = content.get("statusMessage","")
            print(content)
            return render_template('profile.html', name=name, pictureURL=
                                   pictureURL, userID=userID, statusMessage=
                                   statusMessage)
        else:
            return render_template('login.html', client_id=line_login_id,
                                   end_point=end_point)


if __name__ == "__main__":
    app.debug = True
    app.run()
