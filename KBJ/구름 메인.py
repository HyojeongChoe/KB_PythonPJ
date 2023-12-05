import EMOTION
import requests, json
from flask import Flask, request, jsonify, abort
import sys
import urllib.request

application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:red'>☆WATER MELON☆</h1>"

@application.route("/WM", methods=["POST"])
def hello2():
    req = request.get_json()
    
    print(req["userRequest"]["utterance"])
    myreq = req["userRequest"]["utterance"]
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                   'basicCard': {
                      'title': '카드 제목',
                      'description': '카드 설명',
                      'buttons': [
                         {
                           'action': 'webLink',
                           'label': '추천 노래',
                           'webLinkUrl': result
                         }
                      ]
                   }
                }
            ]
        }
    }
    return jsonify(res)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)
