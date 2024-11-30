import random

rock_paper_scissors = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]


def rps():
    print("What do you choose?")
    user_pick = input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
    print(user_pick)
    print(rock_paper_scissors[int(user_pick)])

    print("Computer chose:")
    computer_pick = random.choice(rock_paper_scissors)
    computer_pick_number = rock_paper_scissors.index(computer_pick)
    print(computer_pick_number)
    print(computer_pick)

    if int(user_pick) == 0 and computer_pick_number == 2:
        print("You win!!")
    elif int(user_pick) == computer_pick_number:
        print("It's a draw")
    elif int(user_pick) > computer_pick_number:
        print("You win!!")
    else:
        print("You lose!!")

    play_more = (input("\nPlay again??? 'y' for Yes or 'n' for No: ")).lower()
    if play_more == "y":
        rps()


rps()
