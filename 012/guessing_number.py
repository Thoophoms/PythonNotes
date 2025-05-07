import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

number = random.randint(1,100)
print(number)

user_choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
life = 0

# Hard = 5 attempts Easy = 10 attempts
if user_choose == "hard":
    life = 5
else:
    life = 10

def guess_number():
    user_guess = int(input("Make a guess!: "))
    return user_guess

game_not_over = True

while game_not_over:
    if life > 0:
        check_answer = guess_number()
        if check_answer == number:
            game_not_over = False
            print("Hooray!! you win!!!")
        elif check_answer > number:
            print("Too high")
        elif check_answer < number:
            print("Too Low")
        else:
            print("Invalid answer! Try again!")
        life -= 1
        print(f"You have {life} guess(es)")
    else:
        print("You've run out of guess. you lose.")
        game_not_over = False



