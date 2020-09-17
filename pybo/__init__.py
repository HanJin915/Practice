from flask import Flask

def create_app():
    app = Flask(__name__) #플라스크의 어플리케이션을 생성하는 문장
                          #여기에 사용된 __name__변수는 실행된 모듈명을 의미하므로
                          #pybo라는 문자열이 대입된다(set FLASK_APP=pybo)
    @app.route('/')       #특정 url(예:/)로 접속하면 해당함수를 호출하는
                          #플라스크의 데코레이터이다.
    def hello_pybo():
        return 'Hello, Pybo!'

    return app