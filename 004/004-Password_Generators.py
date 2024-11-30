import random

letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
    "-", "_", "=", "+", "[", "]", "{", "}", ";", ":",
    ".", "<", ">", "?", "|", "~", "`"
]

new_pick_list = []
print("Welcome to the PyPassword Generator!")
user_letters = int(input("How many letters would you like in your password?: "))
user_numbers = int(input("How many numbers would you link in your password?: "))
user_symbols = int(input("Hpw many symbols would you like in your password?: "))

for i in range(0, user_letters):
    new_letter = random.choice(letters)
    new_pick_list.append(new_letter)


for i in range(0, user_numbers):
    new_number = random.choice(numbers)
    new_pick_list.append(new_number)


for i in range(0, user_symbols):
    new_symbol = random.choice(symbols)
    new_pick_list.append(new_symbol)


print(new_pick_list)
random.shuffle(new_pick_list)
print(new_pick_list)

new_text = ''.join(new_pick_list)
print(f"Using ''.join(): {new_text}")


new_comma_text = ','.join(new_pick_list)
print(f"Using ','.join(): {new_comma_text}")


# Using For loop to combine them tgt
text = ""
for i in new_pick_list:
    text += i

print(f"Your password is {text}")
