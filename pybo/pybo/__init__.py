from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

#전역변수로 DB관련된 객체를 만들고 다른모듈에서 활용할 수 있도록 create_app() 내에서 init_app함수를
#이용하여 초기화해주는 패턴
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__) #플라스크의 어플리케이션을 생성하는 문장
                          #여기에 사용된 __name__변수는 실행된 모듈명을 의미하므로
                          #pybo라는 문자열이 대입된다(set FLASK_APP=pybo)
    app.config.from_object(config)  #config.py에 작성된 항목을 app.config의 환경변수로 읽음

    #ORM
    #DB 객체는 전역변수로 만들고 초기화는 각 함수 안에서 수행한다
    #블루프린트와 같은 다른 모듈에서 db객체를 import하여 사용할 수 있도록 하기 위함
    db.init_app(app)
    migrate.init_app(app,db)

    from .views import main_views

    app.register_blueprint(main_views.bp)   #main_views.py에 생성된 블루프린트 객체 bp 등록


    return app