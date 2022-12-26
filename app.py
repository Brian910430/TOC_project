import os
import crawler
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(
    'JLEfTZ+WZ0CfxaAMq4VAnaWzEqCAzKfS1mLeCeVOfVps2b+os2cSux+4vFmNePQf7M3gU5B7h+rIjCJzRWdFfcsRQbPvFapDRNp1+W8fi9JcXkLhvMm8A3Y8dYM3XhlkeacoXFD8OnsO/HElUNqs0QdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('fea35d4ffea5fd69d20030a4f526bb9f')

button_template_message = TemplateSendMessage(
    alt_text='Menu template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://i.kym-cdn.com/entries/icons/facebook/000/026/029/n.jpg',
        title='找漫畫',
        text='選單功能',
        actions=[
            MessageAction(label='我要挑標籤', text='搜尋標籤'),
            MessageAction(label='我要挑語言', text='搜尋語言'),
            MessageAction(label='直接搜尋', text='直接搜尋'),
            MessageAction(label='隨機推薦', text='隨機推薦'),
        ])
)
# line_bot_api.push_message('U3fc79e7cc361e785f794bc8ea5cdcfe3', TextSendMessage('你可以開始了'))
line_bot_api.push_message(
    'U3fc79e7cc361e785f794bc8ea5cdcfe3', button_template_message)
state = 0

# 監聽所有來自 /callback 的 Post Request


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    global state
    if state == 0:
        if re.match('搜尋標籤', message):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage('請輸入要找的標籤(英文)'))
            state = 1
        elif re.match('搜尋語言', message):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage('請輸入要找的語言(英文)'))
            state = 2
        elif re.match('直接搜尋', message):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage('請使用關鍵字搜尋(中英皆可)'))
            state = 3
        elif re.match('隨機推薦', message):
            url, img, title = crawler.craw_random()
            button_message = TemplateSendMessage(
                alt_text='隨機推薦',
                template=ButtonsTemplate(
                    thumbnail_image_url=img,
                    title=title,
                    text='隨機推薦',
                    actions=[
                        URIAction(label='現在看', uri=url+'/')
                    ]
                )
            )
            try:
                line_bot_api.reply_message(event.reply_token, button_message)
            except:
                line_bot_api.reply_message(
                    event.reply_token, TextSendMessage('找不到這本漫畫'))
            state = 0
        else:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage('我不懂你在說什麼'))
            line_bot_api.push_message(
                'U3fc79e7cc361e785f794bc8ea5cdcfe3', button_template_message)
    elif state == 1:
        url, img = crawler.craw_tags(message)
        carousel_template_message = TemplateSendMessage(
            alt_text='找標籤',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=img[0],
                        title='Number1',
                        text='標籤搜尋',
                        actions=[URIAction(label='現在看', uri=url[0]+'/')]),
                    CarouselColumn(
                        thumbnail_image_url=img[1],
                        title='Number2',
                        text='標籤搜尋',
                        actions=[URIAction(label='現在看', uri=url[1]+'/')]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=img[2],
                        title='Number3',
                        text='標籤搜尋',
                        actions=[URIAction(label='現在看', uri=url[2]+'/')]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=img[3],
                        title='Number4',
                        text='標籤搜尋',
                        actions=[URIAction(label='現在看', uri=url[3]+'/')]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=img[4],
                        title='Number5',
                        text='標籤搜尋',
                        actions=[URIAction(label='現在看', uri=url[4]+'/')]
                    )
                ]
            )
        )
        try:
            line_bot_api.reply_message(event.reply_token, carousel_template_message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage('找不到這個標籤的漫畫'))
        state = 0
        line_bot_api.push_message(
            'U3fc79e7cc361e785f794bc8ea5cdcfe3', button_template_message)
    elif state == 2:
        url, img = crawler.craw_language(message)
        carousel_template_message = TemplateSendMessage(
            alt_text='找語言',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=img[0],
                        title='Number1',
                        text='語言搜尋',
                        actions=[URIAction(label='現在看', uri=url[0]+'/')]),
                    CarouselColumn(
                        thumbnail_image_url=img[1],
                        title='Number2',
                        text='語言搜尋',
                        actions=[URIAction(label='現在看', uri=url[1]+'/')]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=img[2],
                        title='Number3',
                        text='語言搜尋',
                        actions=[URIAction(label='現在看', uri=url[2]+'/')]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=img[3],
                        title='Number4',
                        text='語言搜尋',
                        actions=[URIAction(label='現在看', uri=url[3]+'/')]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=img[4],
                        title='Number5',
                        text='語言搜尋',
                        actions=[URIAction(label='現在看', uri=url[4]+'/')]
                    )
                ]
            )
        )
        try:
            line_bot_api.reply_message(event.reply_token, carousel_template_message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage('找不到這個語言的漫畫'))
        state = 0
        line_bot_api.push_message(
            'U3fc79e7cc361e785f794bc8ea5cdcfe3', button_template_message)
    elif state == 3:
        url, img = crawler.craw_search(message)
        
        carousel_template_message = TemplateSendMessage(
            alt_text='搜尋',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=img[0],
                        title='Number1',
                        text='直接搜尋',
                        actions=[URIAction(label='現在看', uri=url[0]+'/')]),
                    CarouselColumn(
                        thumbnail_image_url=img[1],
                        title='Number2',
                        text='直接搜尋',
                        actions=[URIAction(label='現在看', uri=url[1]+'/')]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=img[2],
                        title='Number3',
                        text='直接搜尋',
                        actions=[URIAction(label='現在看', uri=url[2]+'/')]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=img[3],
                        title='Number4',
                        text='直接搜尋',
                        actions=[URIAction(label='現在看', uri=url[3]+'/')]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=img[4],
                        title='Number5',
                        text='直接搜尋',
                        actions=[URIAction(label='現在看', uri=url[4]+'/')]
                    )
                ]
            )
        )
        try:
            line_bot_api.reply_message(event.reply_token, carousel_template_message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage('找不到這種漫畫'))
        state = 0
        line_bot_api.push_message(
            'U3fc79e7cc361e785f794bc8ea5cdcfe3', button_template_message)


# 主程式
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
