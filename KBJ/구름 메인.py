from flask import Flask, request, jsonify, abort
import requests
import json
import sys
import urllib.request

application = Flask(__name__)


@application.route("/")
def hello():
    return "<h1 style='color:red'>☆WATER MELON☆</h1>"

@application.route("/WM", methods=["POST"])
def hello2():
    req = request.get_json()
    print(req)
    print(req["userRequest"]["utterance"])
    myreq = req["userRequest"]["utterance"]

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText":
                        {
                            "text": "머"
                        }
                }
            ]
        }
    }
    return jsonify(res)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)
