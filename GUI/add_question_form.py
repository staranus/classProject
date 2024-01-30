from GUI.questions import post_question
import sys
# from GUI.questions import post_question
import sys
from PySide6.QtWidgets import (QWidget, QApplication,
                               QLabel, QHBoxLayout, QVBoxLayout,
                               QLineEdit, QPushButton, QComboBox)


class AddQuestionForm(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        header = QLabel("Question Editor 😊")

        self.layout.addWidget(header)

        question_layout = QHBoxLayout()
        question_label = QLabel("Enter new question:")
        question_layout.addWidget(question_label)

        self.question_input = QLineEdit()
        question_layout.addWidget(self.question_input)

        answer_1_layout = QHBoxLayout()

        answer_1_label = QLabel("Enter first answer:")
        answer_1_layout.addWidget(answer_1_label)

        self.answer_1_input = QLineEdit()
        answer_1_layout.addWidget(self.answer_1_input)

        answer_2_layout = QHBoxLayout()

        answer_2_label = QLabel("Enter second answer:")
        answer_2_layout.addWidget(answer_2_label)

        self.answer_2_input = QLineEdit()
        answer_2_layout.addWidget(self.answer_2_input)

        answer_3_layout = QHBoxLayout()

        answer_3_label = QLabel("Enter third answer:")
        answer_3_layout.addWidget(answer_3_label)

        self.answer_3_input = QLineEdit()
        answer_3_layout.addWidget(self.answer_3_input)

        answer_4_layout = QHBoxLayout()

        answer_4_label = QLabel("Enter fourth answer:")
        answer_4_layout.addWidget(answer_4_label)

        self.answer_4_input = QLineEdit()
        answer_4_layout.addWidget(self.answer_4_input)

        self.correct_answer = QComboBox()
        self.correct_answer.addItems([
            self.answer_1_input.text(),
            self.answer_2_input.text(),
            self.answer_3_input.text(),
            self.answer_4_input.text()
        ])

        self.send_button = QPushButton("Send!")

        self.layout.addLayout(question_layout)
        self.layout.addLayout(answer_1_layout)
        self.layout.addLayout(answer_2_layout)
        self.layout.addLayout(answer_3_layout)
        self.layout.addLayout(answer_4_layout)
        self.layout.addWidget(self.correct_answer)
        self.layout.addWidget(self.send_button)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    window = AddQuestionForm()
    window.show()
    app.exec()
