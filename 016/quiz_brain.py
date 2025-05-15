# Todo: Asking the questions
# Todo: Checking if the answer was correct
# Todo: Checking if the user is at the end of the quiz


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        current_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        return current_answer, user_answer

    def check_answer(self, q_answer, u_answer):
        # print(f"user answer {u_answer}")
        if q_answer == u_answer:
            self.score += 1
            print(f"You got it right!")
        else:
            print("That's wrong!")
            print(f"The correct answer was: {q_answer}")

        print(f"Your current score is: {self.score}/{self.question_number}\n")
