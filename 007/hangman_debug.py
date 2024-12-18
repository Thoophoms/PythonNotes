from HangmanWords import words
import random


def play_game():
    lives = 5
    user_already_guess = []
    hangman_list = []

    game_over = False
    print("Let's play Hangman!!!")

    word = random.choice(words)
    print(word)

    # Todo: Loop through the word and replace it with "_"
    for char in word:
        hangman_list += char.replace(char, "_")

    def update_list(l):
        if l not in user_already_guess:
            user_already_guess.append(l)
        else:
            print(f"You already guessed {l}. Try again")

    def play_game_again():
        play_again = (input("Do you want to play a gain? 'Y' for yes or 'N' for No: ")).lower()
        if play_again == 'y':
            play_game()
        else:
            nonlocal game_over
            print("Bye! 👋")
            game_over = True

    while not game_over:
        while lives > 0:
            # Todo: join Hangman list
            lets_guess = "".join(hangman_list)

            # Todo: Check if the user win
            if "_" not in hangman_list:
                print(f"You got it! 🎉 The word is {word}. Congrats! 🥳")
                play_game_again()

            else:
                print(lets_guess)
                # Todo: Ask user to guess a letter
                if lives == 1:
                    print(f"You have {lives} chance")
                else:
                    print(f"You have {lives} chances")

                user_guess = (input(f"\nGuess the letter!: ")).lower()
                update_list(user_guess)


                # Todo: Loop through the word and check if the letter user guess is in the word
                if user_guess in word:
                    for i, letter in enumerate(word):
                        if letter == user_guess:
                            hangman_list[i] = user_guess
                else:
                    lives -= 1


play_game()