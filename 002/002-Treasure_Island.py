def play_game():
    def island():
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        mission_3 = (input("One red, one yellow and one blue. Which color do you choose?: ")).lower()
        if mission_3 == "red":
            print("Oopsie!! There is full of blood. Sorry you choose the wrong one.")
            play_again()
        elif mission_3 == "blue":
            print("Congratulation, you chose the right one! YOU WIN yay!!")
            play_again()
        else:
            print("Sorry!! There are so many rocks in here")
            play_again()

    def play_again():
        play_more = input("Do you want to play again?\n Type 'y' for 'Yes' or 'n' for 'No': ")
        if play_more == "y":
            play_game()
    print("Your mission is to find the treasure.")
    mission_1 = (input("You're at a cross road. Where do you want to go?\nType 'l' for left or 'r' for right: ")).lower()

    if mission_1 == "l":
        print("You have come to the lake. There is an island in the middle of the lake")
        mission_2 = (input("Type 'wait' to wait for the boat or 'swim' to swim across: ")).lower()

        if mission_2 == "wait":
            print("The boat have taken you")
            island()

        else:
            print('Oh!!! There are many crocodiles in the lake! You got eaten by those crocodiles. GAME OVER!!')
            play_again()

    else:
        desert = input("There is a long walk on this desert.\nThere are 2 bottle for the drinks you have to take with "
                       "you on this long walk.\nDo you want the pink bottle or yellow bottle: ").lower()
        if desert == "pink":
            print("Good choice!! This bottle's filled with energy to keep you up for this long walk. Let's go!!")
            island()
        else:
            print("Oh OOO!!! No you don't want to drink from this bottle. Sorry, you won't be able to survive without "
                  "water. TRY AGAIN!!!")
            play_again()


print("Welcome to Treasure Island.")
play_game()
