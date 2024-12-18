from HangmanWords import words
import random


def play_game():
    lives = 5
    user_already_guess = []
    hangman_list = []

    print("Let's play Hangman!!!")

    word = random.choice(words)
    # print(word)

    # Todo: Loop through the word and replace it with "_"
    for char in word:
        hangman_list += char.replace(char, "_")

    # Todo: Check if the user already guess the letter
    def update_list(l):
        if l not in user_already_guess:
            user_already_guess.append(l)
        else:
            print(f"You already guessed {l}. Try again")


    # Todo: Function check if user wants to play game again
    # this function will return only if user answer is yes
    def play_game_again():
        play_again = (input("\nDo you want to play a gain? 'Y' for yes or 'N' for No: ")).lower()
        return play_again == 'y'


    # Todo: Check if play_game_again() function return anything?
    def play_more():
        # if play_game_again() function return, means that the user wants to play more
        # so we call play_game() function to start again
        if play_game_again():
            play_game()
        # if play_game_again() function did not return anything,
        # the program will print out bye! and return to the loop where it's left off
        else:
            print("bye! 👋")
            return


    while lives > 0:
        # Todo: join Hangman list
        lets_guess = "".join(hangman_list)

        # Todo: Check if the user win
        if "_" not in hangman_list:
            print(f"\nYou got it! 🎉 The word is {word}. Congrats! 🥳")

            # Todo: Call the play_more() function to ask user when there is not life left if they wants to play more
            # If the user answer 'y', it the function will call to play again
            play_more()
            # else the function will return to this line and this return will kick our of the loop. So the game is ended
            return

        # Todo: If the user is not yet win, continue guessing
        else:
            # Todo: Ask user to guess a letter (if and else conditions in one line)
            print(f"\nYou have {lives} {'chance' if lives == 1 else 'chances'}")

            print(lets_guess)

            user_guess = (input(f"Guess the letter!: ")).lower()
            update_list(user_guess)


            # Todo: Loop through the word and check if the letter user guess is in the word
            if user_guess in word:
                for i, letter in enumerate(word):
                    if letter == user_guess:
                        hangman_list[i] = user_guess
            else:
                lives -= 1


    print(f"Oopsie! You're screw!! 🤦🏻🤦🏼‍♀️ The word is {word}. Good Try!")
    # Todo: call play_more() function to ask user when there is not life left if they wants to play more
    # If the user answer 'y', it the function will call to play again
    play_more()
    # else the function will return to this line and this return will kick our of the loop. So the game is ended
    return


play_game()
