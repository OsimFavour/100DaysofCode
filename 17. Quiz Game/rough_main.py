from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# print(question_bank)
# print(question_bank[0].text)


def next_question(self, q_list):    # my own trial on the next_question method
    """retrieve the item at the current question_number from the question_list"""
    for item in q_list:
        question_num = q_list.index(item) + 1
        current_question = q_list[question_num]
        print(input(f"Q.{question_num}: {current_question.text} (True/False)"))


QuizBrain(question_bank)
