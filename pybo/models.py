from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)

    #Question모델의 id값을 의미하며, 이를 나타내기 위해 db.ForeignKey를 사용한다
    #ForeignKey는 다른 모델과의 연결을 의미하며, ondelete=CACADE의 의미는 이 답변과 연결된 질문(Question)이 삭제될 경우
    #답변(Answer)도 함께 삭제된다는 의미이다.
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))

    #답변모델에서 질문모델을 참조하기 위한 속성 db.relationship을 이용하여 속성을 추가해 주어야 한다.
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)