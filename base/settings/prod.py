from .common import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'site7',  # db에 데이터베이스가 생성되어있는지 먼저 체크
        'USER': 'whdrnal',  # 유저가 제대로 추가되어있는지 먼저 체크
        'PASSWORD': 'dudwls85',
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # 추가, 만약에 이 부분 때문에 오류가 난다면, 이 라인을 지우고 다시 시도해주세요.
        },
    }
}
# 그 지금여기 db랑 common에있는 db랑 무슨 차이에용 ?
# 만약 여기서 DATABASE 정보를 덮어씌운다면 여기있는 DB가 앞으로 서버에 올려서 사용하게 될 DB에여 지금 종구님 컴에있는 DB를 쓰는게 아니라
# 서버에 설치되어있는 DB나 다른 서버에 설치되어있는 DB를 여기에 적혀있는 정보로 사용 할 것이란거에여
# 그러면 여기가 본사고 저기 common은 가짜네요 ?우선
# 일단 prod는 배포용이고 dev가 개발용이자나여?
# prod에서 database를 덮어씌운다면 prod에있는 정보로 배포용 DB에 연결 할것이고
# dev에서 database를 덮어씌운다면 배포할때는 그대로 common에 있는 정보로 DB에 연결할것이구여
# 이거 글읽으면서 조금씩더 이해해봐야겠어요 그럼 우선 prod 이녀석이 서버 배포용 common 이녀석이 common 이녀석에 있는 정보를 db에 연결 그리고 배포할때는 prod 에연결??인가요
# 우리가 지금 이 장고를 실행하는데 두가지 방식이 있어여 settings를 실행하는 방식이
# prod -> common
# dev -> common 이두가지 방식인데 common은 prod나 dev 둘 모두에서 쓰이는 공통적인 정보를 담고있어여 그래서
# 이렇게 해도 작동에 무리가 없어요 이렇게 하면 오히려 더 직관적일거에여 ok 2개 다 어차피 똑같이
# 사용하는거네요 근데 배포용과 이제 2가의 그게있는거고 common 이녀석은 계속 dev 로주고 prod  로주고
# 맞아여 클래스 상속과 같은 느낌으로 이해하시면 대여 오! 살짝 이해했습니다! 감사합니다!


#쟤는 ssh주소란거에여, 저걸로 통신하기위해서는 private key와 public key가 필요해여. 네이버 서버 올릴때 봤져? 네네