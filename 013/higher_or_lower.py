from jinja2.compiler import generate

from art import logo, vs
from game_data import data
from random import randint, choice
print(logo)

# print(f"Compare A: {data[1]['name']}, a {data[1]['description']}, from {data[1]['country']}")
# print(vs)
# print(f"Compare B: {data[2]['name']}, a {data[2]['description']}, from {data[2]['country']}")


score = 0

# Todo 1: Generate 2 random number 2 for the comparison
# Todo 2: Check of the first number == second number, if so, regenerate the second one
# # Check if the there is a same person
# person1 = data[1]
# person2 = data[1]
#
# if person1 is person2:
#     print("same")
def generate_2_people():
    celebrity_1 = choice(data)
    celebrity_2 = choice(data)
    # if we check the follower counts, we dont need to check for the name because
    # 1. same person or 2. number of followers are the same
    # if celebrity_1 is celebrity_2:
    #     generate_2_people()
    if int(celebrity_1['follower_count']) == int(celebrity_2['follower_count']):
        return generate_2_people()
    else:
        return celebrity_1, celebrity_2

def check_answer(person1_follower, person2_follower, user_guess):
    if user_guess == "A":
        user_guess = person1_follower
    else:
        user_guess = person2_follower
    print(user_guess)

    if person1_follower > person2_follower:
        high_follower = person1_follower
    else:
        high_follower = person2_follower

    if user_guess == high_follower:
        return True
    else:
        return False


game_not_over = True

while game_not_over:
    # get the whole information of the celebrity
    person_1, person_2 = generate_2_people()
    # Get only the follower count of each person
    person_1_followers = int(person_1['follower_count'])
    person_2_followers = int(person_2['follower_count'])
    # check
    # print(f"1: {person_1_followers}, 2: {person_2_followers}")



    # Todo 3: Show the comparison on the screen
    print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}")
    print(vs)
    print(f"Compare B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}")

    # Todo 4: Ask the user to guess A or B
    user_answer = input("Who has more follower? Type 'A' or 'B': ").upper()

    # Todo 5: Check if the answer is correct

    # Todo 6: Count the score when the user's guess correctly

    # Todo 5: End game when it user's guess is wrong and show the final score
    if check_answer(person1_follower=person_1_followers, person2_follower=person_2_followers, user_guess=user_answer):
        score +=1
        print(f"You are right!! Current score: {score}")
    else:
        print(f"Sorry that's wrong! Final score: {score}")
        game_not_over = False