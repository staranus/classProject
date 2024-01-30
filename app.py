from flask import Flask, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
app.config['SECRET_KEY'] = '1234'
db = SQLAlchemy(app)


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer_1 = db.Column(db.Text, nullable=False)
    answer_2 = db.Column(db.Text, nullable=False)
    answer_3 = db.Column(db.Text, nullable=False)
    answer_4 = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer_1': self.answer_1,
            'answer_2': self.answer_2,
            'answer_3': self.answer_3,
            'answer_4': self.answer_4,
            'correct_answer': self.correct_answer
        }


with app.app_context():
    db.create_all()
    question_instances = [
        Questions(
            question="What is the capital of France?",
            answer_1="Paris",
            answer_2="Berlin",
            answer_3="Rome",
            answer_4="Madrid",
            correct_answer="Paris"
        ),
        Questions(
            question="What is the highest mountain in the world?",
            answer_1="K2",
            answer_2="Everest",
            answer_3="Kilimanjaro",
            answer_4="Mont Blanc",
            correct_answer="Everest"
        )
    ]
db.session.add_all(question_instances)
db.session.commit()


@app.route('/cquestions', methods=['GET'])
def get_questions():
    questions = Questions.query.all()
    return jsonify([item.to_dict() for item in questions])


@app.route('/questions', methods=['POST'])
def add_question():
    data = request.get_json()  # dict / list
    # if it's a list
    for question_data in data:
        new_question = Questions(
            question=question_data['question'],
            answer_1=question_data['answer_1'],
            answer_2=question_data['answer_2'],
            answer_3=question_data['answer_3'],
            answer_4=question_data['answer_4'],
            correct_answer=question_data['correct_answer']
        )
        db.session.add(new_question)
    db.session.commit()
    return jsonify({'message': 'Questions added successfully'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
