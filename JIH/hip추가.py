class EMOTION:
    def emotion(emotion):
        # 인디
        
        indiJoy = [
            # 완벽해 - 레터플로우
            'https://www.youtube.com/watch?v=56vTXXk5PSQ&pp=ygUZ66CI7YSw7ZSM66Gc7JqwIOyZhOuyve2VtA%3D%3D',
            # 예쁜 말 - 어나니머스 아티스트
            'https://www.youtube.com/watch?v=0Bk_8tEEYzA&pp=ygUZ7JiI7IGc66eQIOyWtOuCmOuLiOuouOyKpA%3D%3D',
            # UP DOWN - 어나니머스 아티스트
            'https://www.youtube.com/watch?v=nw_o_qymHoM&pp=ygUl7Ja064KY64uI66i47IqkIOyVhO2LsOyKpO2KuCB1cCBkb3duIA%3D%3D',
            # 뭘 믿고 그렇게 이쁜거니 - 레터플로우
            'https://www.youtube.com/watch?v=DnVm2LENTec&pp=ygUw662Y66-_6rOgIOq3uOugh-qyjCDsnbTsgZzqsbDri4gg66CI7YSw7ZSM66Gc7Jqw',
            # ocean view - 로시
            'https://www.youtube.com/watch?v=5wiW60inhgw&pp=ygUN66Gc7IucIOyYpOyFmA%3D%3D'
        ]
        indiSad = [
            # 내 맘이 어떻든 - 레터플로우
            'https://www.youtube.com/watch?v=0pg00YztwNI&pp=ygUk64K0IOunmOydtCDslrTrlrvrk6Ag66CI7YSw7ZSM66Gc7Jqw',
            # 꺼져 - 이민석
            'https://www.youtube.com/watch?v=XeR-_xlr608&pp=ygUQ7J2066-87ISdIOq6vOyguA%3D%3D',
            # 놓아 - 이민석
            'https://www.youtube.com/watch?v=CpBl_3LG8bI&pp=ygUQ7J2066-87ISdIOuGk-yVhA%3D%3D',
            # 무너져 - 바닐라 어쿠스틱
            'https://www.youtube.com/watch?v=xBY_9xf-u2A&pp=ygUg67CU64uQ6528IOyWtOy_oOyKpO2LsSDrrLTrhIjsoLg%3D',
            # 미안해 - 스웨덴 세탁소
            'https://www.youtube.com/watch?v=-CPQY3Qh1cE&pp=ygUd7Iqk7Juo6420IOyEuO2DgeyGjCDrr7jslYjtlbQ%3D'
        ]
        indiAnger = [
            # Hi Bully - 터치드
            'https://www.youtube.com/watch?v=tOI2K1CD_Ik&pp=ygUW7ZWY7J2067aI66asIO2EsOy5mOuTnA%3D%3D',
            # lovers in the night - seori
            'https://www.youtube.com/watch?v=RLPWiQKqi-I&pp=ygUTbG92ZXJzIGluIHRoZSBuaWdodA%3D%3D',
            # 여우별 - 어나니머스 아티스트
            'https://www.youtube.com/watch?v=suUzX5EErFw&pp=ygUm7Ja064KY64uI66i47IqkIOyVhO2LsOyKpO2KuCDsl6zsmrDrs4Q%3D',
            # 퇴사 - 이민석
            'https://www.youtube.com/watch?v=bJkhBZ1ZcuY&pp=ygUQ7Ye07IKsIOydtOuvvOyEnQ%3D%3D',
            # 무음모드 - 와인루프
            'https://www.youtube.com/watch?v=0orGwjKVjJ4&pp=ygUZ66y07J2M66qo65OcIOyZgOyduOujqO2UhA%3D%3D'
        ]
        indiUnrest = [
            # 아무도 그대를 바라지 않는 - 알레프
            'https://www.youtube.com/watch?v=2iczc21Czio&pp=ygUk7JWE66y064-EIOq3uOuMgOulvCDrsJTrnbzsp4Ag7JWK64qU',
            # 나는 왜 - O.O.O
            'https://www.youtube.com/watch?v=WtzwHG52v5Q&pp=ygUU64KY64qUIOyZnCDsmKTsmKTsmKQ%3D',
            # Abduvida - 맥거핀
            'https://www.youtube.com/watch?v=AacajtTL1Dk&pp=ygUIYWJkdXZpZGE%3D',
            # 자유 - 알레프
            'https://www.youtube.com/watch?v=uy2BlCSSLnA&pp=ygUQ7J6Q7JygIOyVjOugiO2UhA%3D%3D',
            # 두리번 - 맥거핀
            'https://www.youtube.com/watch?v=2i6CdoLIS5k&pp=ygUT65GQ66as67KIIOunpeqxsO2VgA%3D%3D'
        ]
        indiBoring = [
            # 너를 사랑한다는 말이 발음 안돼 - WET BOY
            'https://www.youtube.com/watch?v=_g8GMN9Rt3I&pp=ygUq64SI66W8IOyCrOueke2VnOuLpOuKlCDrp5DsnbQg67Cc7J2M7JWI64-8',
            # 긴밤 - 서리
            'https://www.youtube.com/watch?v=SaoCdRyN3b4&pp=ygUG6ri067Ck',
            # T - 맥거핀
            'https://www.youtube.com/watch?v=FwT88Uyhfo8&pp=ygULVCDrp6XqsbDtlYA%3D',
            # DISCO - 맥거핀
            'https://www.youtube.com/watch?v=ubh44nZQk4A&pp=ygUT65SU7Iqk7L2UIOunpeqxsO2VgA%3D%3D',
            # 춘곤 - 징고
            'https://www.youtube.com/watch?v=4mR-lzkizoc&pp=ygUN7LaY6rOkIOynleqzoA%3D%3D'
        ]

        # 힙합

        hipJoy = [
            #DPR LIVE - Martini Blue
            'https://www.youtube.com/watch?v=dGVWH6ojI0c',
            #Loopy - SAVE(feat.Paloalto)
            'https://www.youtube.com/watch?v=x7x0Agd5tjA',
            #lobonabeat! - 생일(feat.BILL STAX)
            'https://www.youtube.com/watch?v=C8BYNRR7V6k',
            #Crush - Ibiza
            'https://www.youtube.com/watch?v=E6OgcgFHFpc',
            #The Quiett - 귀감(feat.ZENE THE ZILLA)
            'https://www.youtube.com/watch?v=P1ijRTr2s_s'
        ]
        hipSad = [
            # PATEKO - Rainy day(feat.ASH ISLAND, Skinny Brown)
            'https://www.youtube.com/watch?v=R7L2QEm-BUY',
            # 미란이 - Daisy(feat.pH-1)
            'https://www.youtube.com/watch?v=co90cPpbcd8',
            # Crucial Star - I'm OK(생각보다)
            'https://www.youtube.com/watch?v=EWeEM7sNr0g',
            # Lil Boi - CREDIT(feat.염따,기리보이,Zion.T)
            'https://www.youtube.com/watch?v=UMWBdzQSr_I',
            # The Quiett - 한강 gang(feat.Byung Un,창모)
            'https://www.youtube.com/watch?v=O42lYtNTh50'
        ]
        hipAnger = [
            # nafla - 선빵(feat.Gaeko,기리보이)
            'https://www.youtube.com/watch?v=iG1wG86hywk',
            # Dynamic Duo - 길을막지마
            'https://www.youtube.com/watch?v=4X29jjIjqK8',
            # 이센스 - RADAR(feat.김심야)
            'https://www.youtube.com/watch?v=mZlQNwGJCio',
            # Sik-k - FIRE
            'https://www.youtube.com/watch?v=bKJxo-yIcg0',
            # Uneducated Kid - 어쩌라고(feat.Beenzino)
            'https://www.youtube.com/watch?v=bZmRG814CLQ'
        ]
        hipUnrest = [
            # ASH ISLAND - Paranoid
            'https://www.youtube.com/watch?v=USlZolbKXhg',
            # BLOO - Drama
            'https://www.youtube.com/watch?v=NBLvVhg5mpo',
            # Dok2 - On My Way(feat.Zion.T)
            'https://www.youtube.com/watch?v=QzLFcfCEm-I',
            # 창모 - S T A R T
            'https://www.youtube.com/watch?v=nZwu6fzXz7E',
            # 기리보이 - 호랑이소굴(feat.Jvcki Wai)
            'https://www.youtube.com/watch?v=xmXHQUAWLA8'
        ]
        hipBoring = [
            # 죠지 - Boat
            'https://www.youtube.com/watch?v=OWL1RNX7p90',
            # 릴러말즈 - Trip(feat.Hannah)
            'https://www.youtube.com/watch?v=5C-UzW1FLiA',
            # 기리보이 - Party People(feat.염따,Uneducated Kid)
            'https://www.youtube.com/watch?v=gsLQpBEC7QA',
            # Lil Moshpit - Yooooo(feat.Kid Milli,sokodomo,Polodared)
            'https://www.youtube.com/watch?v=xyTRjWvyahc',
            # 한요한 - 범퍼카(feat.NO:EL,Young B)
            'https://www.youtube.com/watch?v=medo8dj_-28'
        ]


        # 발라드

        balJoy = [
            # 걷자,집앞이야 - 스무살
            'https://www.youtube.com/watch?v=14hH4eSmRTo&pp=ygUW7Iqk66y07IK0IOynkeyVnuydtOyVvA%3D%3D',
            # 지그재그 - 맥거핀
            'https://www.youtube.com/watch?v=9yZMOVWiJ8c&pp=ygUW7KeA6re47J6s6re4IOunpeqxsO2VgA%3D%3D',
            # 케이윌 - Love Blossom
            'https://www.youtube.com/watch?v=WmCy7VJPPk4',
            # 에릭남,치즈 - 사랑인가요
            'https://www.youtube.com/watch?v=2-57ZGv7Deg'
        ]
        balSad = [
            # 환상 - 하현우
            'https://www.youtube.com/watch?v=l7N7DGHv7Qk&pp=ygUQ7ZmY7IOBIO2VmO2YhOyasA%3D%3D',
            # 너의 번호를 누르고 - #안녕
            'https://www.youtube.com/watch?v=URZaPnGp5rI&pp=ygUa64SI7J2YIOuyiO2YuOulvCDriITrpbTqs6A%3D',
            # 에일리 - 첫눈처럼 너에게 가겠다.
            'https://www.youtube.com/watch?v=2FhBGUkI4vs',
            # V.O.S - 울어
            'https://www.youtube.com/watch?v=mOov1C0_4kE'
        ]
        balAnger = [
            # 차가운 커피 - 먼데이 키즈
            'https://www.youtube.com/watch?v=DMSQwokMKpA&pp=ygUQ7LCo6rCA7Jq0IOy7pO2UvA%3D%3D',
            # Whiskey and Morphine - Alexander Jean
            'https://www.youtube.com/watch?v=ACDf9fhpuqo&pp=ygUV7JyE7Iqk7YKk7JWk66qo66W07ZWA',
            # 브라운아이드소울 - 비켜줄께
            'https://www.youtube.com/watch?v=4bKECOPvS2c',
            # 포맨 - 눈물
            'https://www.youtube.com/watch?v=hHIauY2P11A '

        ]
        balUnrest = [
            # 밤하늘의 별을 4 - 양정승
            'https://www.youtube.com/watch?v=aGP14gSVgIY&pp=ygUT67Ck7ZWY64qY7J2Y67OE7J2ENA%3D%3D',
            # Dangerously - 찰리 푸스
            'https://www.youtube.com/watch?v=qn-cSwgcXio&pp=ygUT7LCw66as7ZG47IqkIOuNtOyguA%3D%3D',
            # 케이윌 - 이러지마 제발
            'https://www.youtube.com/watch?v=3SaJeuwy1TY',
            # 버즈 - 겁쟁이
            'https://www.youtube.com/watch?v=G7eLG4Tnc9c'
        ]
        balBoring = [
            # 드라큘라 - 히미츠
            'https://www.youtube.com/watch?v=OPo5-e_XacE&pp=ygUW65Oc65287YGY6528IO2eiOuvuOy4oA%3D%3D',
            # SONATA - 피엘
            'https://www.youtube.com/watch?v=vB4XEupGHf4&pp=ygUQ7ZS87JeYIOyGjOuCmO2DgA%3D%3D',
            # 프라이머리 - ~42(feat.Sam Kim,eSNa)
            'https://www.youtube.com/watch?v=Ws9sG-6Eh68',
            # 폴킴 - 집돌이
            'https://www.youtube.com/watch?v=LrDCqP52SbE'

        ]
        return ''
