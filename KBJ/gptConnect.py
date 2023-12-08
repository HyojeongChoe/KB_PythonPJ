# 유튜브는 저정도로 두고 두분이 다 하셨으니 gpt랑 연결하는거라도....
from flask import Flask, jsonify, request
import requests, sys, json
application = Flask(__name__)
a = {}

@application.route("/webhook/", methods=["POST"])
def webhook():
    global a
    request_data = json.loads(request.get_data(), encoding='utf-8')
    a[request_data['user']] = request_data['result']['choices'][0]['message']['content']
    return 'OK'

@application.route("/question", methods=["POST"])
def get_question():
    global a
    request_data = json.loads(request.get_data(), encoding='utf-8')
    response = { "version": "2.0", "template": { "outputs": [{
        "simpleText": {"text": f"GPT에게 물어보는 중입니다.: {request_data['action']['params']['question']}"}
    }]}}
    a[request_data['userRequest']['user']['id']] = '아직 GPT가 처리중입니다.'
    try:
        api = requests.post('https://api.asyncia.com/v1/api/request/', json={
            "apikey": "<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>",
            "messages" :[{"role": "user", "content": request_data['action']['params']['question']}],
            "userdata": [["user", request_data['userRequest']['user']['id']]]},
            headers={"apikey":"<Asyncia API KEY>"}, timeout=0.3) #asyncia : 웹훅 사용하려면 필요
            # 어센시아 홈페이지에서 api신청 - 구름컨테이너 주소 필요함 - api키 재확인 불가하니 메모든 카카오톡이든 저장해두기 / 터미널에서 파일명 입력 필요 *사용중에 터미널 열어둬야함 / 용량 제한 있으니 용량 부족 시 증가신청 필요
            # 스킬 추가 해야줘야함 / 시나리오 질문블럭, 답변블럭 ai는 파라미터도 추가해줘야함 / 되묻기 최대횟수 지정 필요 / question<<질문블럭 / ans<<답변블럭
            # 답변블럭 호출을 안하면 웹훅한걸 안보여줌...
    except requests.exceptions.ReadTimeout:
        pass
    return jsonify(response)

@application.route("/ans", methods=["POST"])
def hello2():
    request_data = json.loads(request.get_data(), encoding='utf-8')
    response = { "version": "2.0", "template": { "outputs": [{
        "simpleText": {"text": f"답변: {a.get(request_data['userRequest']['user']['id'], '질문을 하신적이 없어보여요. 질문부터 해주세요')}"}
    }]}}
    return jsonify(response)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)
