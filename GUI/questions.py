import requests

BASE_URL = "http://127.0.0.1:5000/questions"


def get_question():
    response = requests.get(BASE_URL)
    return response.json()


def post_question(json_question: dict):
    response = requests.post(BASE_URL, json=json_question)
    return response.status_code


if __name__ == "__main__":
    q = {
        "question": "What is the code for attendance?",
        "answer_1": "w1s929",
        "answer_2": "11111111",
        "answer_3": "222222",
        "answer_4": "23333333",
        "correct_answer": "w1s929"
    }

    # print(post_question(q))
    print(len(get_question()))
