from HangmanWords import words
import random

print("Let's play Hangman!!!")

game_over = False
word = random.choice(words)
print(word)

lives = 5
user_already_guess = []
hangman_list = []

for char in word:
    hangman_list += char.replace(char, "_")

lets_guess = "".join(hangman_list)
print(lets_guess)

