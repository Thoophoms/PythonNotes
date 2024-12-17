from HangmanWords import words
import random


print("Let's play Hangman!!!")



def play_game():
    game_over = False
    word = random.choice(words)
    print(word)

    lives = 5
    user_already_guess = []
    hangman_list = []
    for char in word:
        hangman_list += char.replace(char, "_")

    while not game_over:
        while lives > 0:
            if "_" not in hangman_list:
                print(f"Wow! You are so smart. You win!!!")
                game_over = True

                play_again = input("Do you want to play again? 'y' for yes or 'n' for No: ")

                if play_again.lower() == 'y':
                    play_game()

            else:
                guess = "".join(hangman_list)
                print(guess)

                print(f"You have {lives} chances")
                user_guess = (input(f"\nGuess the letter!: ")).lower()

                if user_guess in user_already_guess:
                    print(f"You have guessed '{user_guess}' try again!")
                else:
                    user_already_guess += user_guess
                    if user_guess in word:
                        # Check if the guess is in the word and replace in bulk
                        print(f"Good guess! '{user_guess}' is in the word.")
                        for i, letter in enumerate(word):
                            if letter == user_guess:
                                hangman_list[i] = user_guess
                    else:
                        print(f"Good try but {user_guess} is not in it! Try again")
                        lives -= 1

    print(f"\nOh no!! Sorry! you lose! the word is {word}")
    play_again = input("\nDo you want to play again? 'y' for yes or 'n' for No: ")

    if play_again.lower() == 'y':
        play_game()


play_game()
