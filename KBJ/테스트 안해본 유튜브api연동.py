from flask import Flask, request, jsonify, abort
import requests
import requests, json
import urllib.request

app = Flask(__name__)

@application.route("/WM",methods=["POST"])
def kakaochatbot():
    req = request.get_json()
    rm = req["userRequest"]["utterance"]
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
