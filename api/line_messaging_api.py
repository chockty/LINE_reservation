from django.http import HttpRequest, request
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import json
import os

REPLY_ENDPOINT_URL = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = os.environ.get(['LINE_ACCESS_TOKEN'])
HEADER = {
  'Content-Type' : 'application/json',
  'Authorization' : 'Bearer ' + ACCESS_TOKEN
}

class LineMessage():
  def __init__(self, messages):
    self.messages = messages
  
  # 返信処理
  def reply(self, reply_token):
    body = {
      'replyToken' : reply_token,
      'messages' : self.messages,
    }

    http_request = urllib.request.Request(REPLY_ENDPOINT_URL, json.dumps(body).encode(), HEADER)

    try:
      with urllib.request.urlopen(http_request) as req:
        req_body = req.read()
    except urllib.error.HTTPError as err:
       print(err)
    except urllib.error.URLError as err:
       print(err.reason)

  # 応答メッセージの編集
  def create_original_messages(message):
    original_messages = {
      'type': 'text',
      'text' : 'テストです。'
    }

    return original_messages
