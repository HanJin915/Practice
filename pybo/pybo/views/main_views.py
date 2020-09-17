from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

                            #pybo/__init__.py에 있던 내용을 여기로 옮김
@bp.route('/hello')         #단, @app.route가 아닌 bp.route로 변경됨
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return 'Pybo index'