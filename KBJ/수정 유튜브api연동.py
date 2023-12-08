@application.route("/youtube", methods=["POST"])
def youtube_search():
    req = request.get_json()
    search_query = req["userRequest"]["utterance"]

    if search_query.startswith('/youtube '):
        search_term = search_query.replace('/youtube_search ', '')
        youtube_api_key = '여기에_당신의_YouTube_API_키를_입력하세요'

        try:
            response = requests.get('https://www.googleapis.com/youtube/v3/search', params={
                'part': 'snippet',
                'q': search_term,
                'key': 'AIzaSyCMcHB5M_2ywcz44iob-cTniG3iHkk_low'
            })

            search_results = response.json()['items']
            if search_results:
                cards = []
                for item in search_results:
                    video_title = item['snippet']['title']
                    video_thumbnail = item['snippet']['thumbnails']['default']['url']
                    video_id = item['id']['videoId']
                    
                    card = {
                        'title': video_title,
                        'description': 'YouTube Video',
                        'thumbnail': {
                            'imageUrl': video_thumbnail
                        },
                        'buttons': [
                            {
                                'action': 'webLink',
                                'label': '시청하기',
                                'webLinkUrl': f'https://www.youtube.com/watch?v={video_id}'
                            }
                        ]
                    }
                    cards.append(card)

                res = {
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "listCard": {
                                    "header": {
                                        "title": f"\"{search_term}\" 검색 결과"
                                    },
                                    "items": cards
                                }
                            }
                        ]
                    }
                }
                return jsonify(res)
            else:
                return jsonify({'message': '검색 결과가 없습니다.'})
        except Exception as e:
            print('검색엔진 호출 중 오류:', e)
            return jsonify({'message': '검색엔진 호출 중 오류가 발생했습니다.'}), 500

    return jsonify({'message': ''})
