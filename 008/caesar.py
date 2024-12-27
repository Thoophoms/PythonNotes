from operator import truediv

from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)



# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.


def ceasar(original_text, shift_amount, direction):
    encrypted_text = ""
    for each_letter in original_text:
        if each_letter in alphabet:
            original_index = alphabet.index(each_letter)
            if direction == "encode":
                new_index = (original_index + shift_amount) % 26
            else:
                new_index = (original_index - shift_amount) % 26
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += each_letter
    print(encrypted_text)


def start_caesar():
    continue_caesar_cipher = True

    while continue_caesar_cipher:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == "encode":
            ceasar(text, shift, "encode")
        elif direction == "decode":
            ceasar(text, shift, "decode")
        else:
            print("Invalid input. Good bye!")
            continue_caesar_cipher = False


start_caesar()