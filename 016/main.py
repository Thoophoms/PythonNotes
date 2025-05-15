from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Loop through the question_data
# for i in range(0, len(question_data)):
#     q = question_data[i]["text"]
#     a = question_data[i]["answer"]
#
#     new_question = Question(q_text=q, q_answer=a)
#     print(new_question.text)
#     print(new_question.answer)


# store question_data in the new list
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]

    new_question = Question(q_text = question_text, q_answer = question_answer)
    question_bank.append(new_question)

# print out question from quiz_brain
quiz = QuizBrain(question_bank)
# quiz.next_question()


while quiz.still_has_question():
    question = quiz.next_question()
    quiz.check_answer(q_answer=question[0], u_answer=question[1])

print("\nYou've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")







