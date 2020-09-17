import os

BASE_DIR = os.path.dirname(__file__)        #루트디렉토리 C:\Users\hanji\projects\myproject 의미

#데이터베이스의 접속 주소를 의미하며, BASE_DIR 하위의 pybo.db파일에 저장한다고 정의함
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR,'pybo.db'))

#SQLAlchemy의 이벤트들을 처리하기 위한 옵션이나, 추가적인 메모리를 사용하고
#실습에서 활용하지 않으므로 비활성화 시킴
SQLALCHEMY_TRACK_MODIFICATIONS = False
