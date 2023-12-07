from flask import Flask, request, jsonify, abort
import requests
import requests, json
import urllib.request

app = Flask(__name__)
# 합치기 전 myreq3만들고 2,3 각각 장르,감정 저장하기
@application.route("/youtube",methods=["POST"])
def kakaochatbot():
    global myreq2
    global myreq3
    req = request.get_json()
    rm = req["userRequest"]["utterance"]
    #rm이 검색어 검색어를 입력받아서 할거면 이전에 검색어를 입력하게끔 유도해야함
    #이전 내용 ex) 장르 - 아이돌, 감정 - 기쁨으로 선택햇던걸 이용하려면 위의 global변수를 사용해서
    #ex) search = myreq2+myreq3로 또는 rm = (전과 동일)과 같이 저장 해서 사용하게끔 해줘야함
    if rm['content'].startswith('/youtube '):
        search = rm['content'].replace('/youtube ', '')
        youtube_api_key = 'AIzaSyCMcHB5M_2ywcz44iob-cTniG3iHkk_low'

        try:
            response = requests.get('https://www.googleapis.com/youtube/v3/search', params={
                'part': 'snippet',
                'q': search,
                'key': youtube_api_key
            })

            search_results = response.json()['items']
            if search_results:
                video_titles = '\n'.join(item['snippet']['title'] for item in search_results)
                return jsonify({'message': f'검색 결과:\n{video_titles}'})
            else:
                return jsonify({'message': '검색 결과가 없습니다.'})
        except Exception as e:
            print('검색엔진 호출 중 오류:', e)
            return jsonify({'message': '검색엔진 호출 중 오류가 발생했습니다.'}), 500

    return jsonify({'message': '허허'})
    
if __name__ == '__main__':
    app.run(debug=True)
