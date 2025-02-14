import random

# Your cards: [2, 4]
# Computer's first card: 1
# Type 'y' to get another card, type 'n' to pass:
# You final hands: [2, 4]
# Computer's final hands: [1, 1]
# You win
# Get as close to 21 as possible
# Jack, Queen, and King count as 10
# A = 1 or 11
# If dealer score < 17, they must get another card

def start_blackjack():
    computer_card = []
    user_card = []
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    still_play = True

    while still_play:
        def play_more():
            user_pick = (input("Type 'y' to play again, type 'n' to end the game: ")).lower()
            return user_pick

        def pick_the_card(num_card, add_to):
            for i in range(num_card):
                random_pick = random.choice(cards)
                add_to.append(random_pick)

        def check_card(whose_cards):
            total = 0
            for card in whose_cards:
                if card == "A":
                    total += 11
                elif card == "J" or card == "Q" or card == "K":
                    total += 10
                else:
                    total += card
                    if "A" in whose_cards and total > 21:
                        total -= 10

            return total


        def final_hands(user_total, computer_total):
            # Check who wins
            if user_total == computer_total:
                print("It's a draw")
            elif user_total > computer_total:
                print("You win!")
            else:
                print("You lose!")

        def again_and_again():
            pick_to_play = play_more()
            if pick_to_play == 'y':
                start_blackjack()
            else:
                return 'n'

        # computer's part
        pick_the_card(num_card=2, add_to=computer_card)
        print(f"Computer's card: {computer_card[0]}")
        computer_total_result = check_card(whose_cards=computer_card)
        # print(computer_total_result)
        if computer_total_result < 17:
            pick_the_card(num_card=1, add_to=computer_card)
            # print(f"Computer's card: {computer_card}")
            computer_total_result = check_card(whose_cards=computer_card)


        # user's part
        pick_the_card(num_card=2, add_to=user_card)
        print(f"Your Card: {user_card}")
        user_total_result = check_card(whose_cards=user_card)
        # print(user_total_result)

        more_card = (input("Type 'y' to get another card, type 'n' to pass: ")).lower()
        if more_card == 'y':
            pick_the_card(num_card=1, add_to=user_card)
            # print(f"Your Card: {user_card}")
            user_total_result = check_card(whose_cards=user_card)
            # print(user_total_result)
            if computer_total_result > 21:
                print("You win!")
                another_play = again_and_again()
                if another_play == 'n':
                    still_play = False
            # print(computer_total_result)

            if user_total_result > 21:
                print(f"Your final hands: {user_card}\nYou lose!")
            else:
                print(f"Computer's final hands: {computer_card}")
                print(f"Your final hands: {user_card}")
                final_hands(user_total=user_total_result, computer_total=computer_total_result)
                another_play = again_and_again()
                if another_play == 'n':
                    still_play = False
        else:
            print(f"Computer's final hands: {computer_card}")
            print(f"Your final hands: {user_card}")
            final_hands(user_total=user_total_result, computer_total=computer_total_result)
            another_play = again_and_again()
            if another_play == 'n':
                still_play = False

# Start game here!
play_game = (input("Do you want to play Black Jack game?\nType 'y' for Yes or 'n' or No: ")).lower()
if play_game == 'y':
    start_blackjack()




