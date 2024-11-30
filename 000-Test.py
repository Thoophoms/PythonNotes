print("Welcome to Python Pizza Deliveries!")

size = (input("What size pizza do you want? S, M, or L: ")).upper()
pepperoni = (input("Do you want pepperoni on your pizza? Y or N: ")).upper()
extra_cheese = (input("Do you want extra cheese? Y or N: ")).upper()

total = 0

if size == "S":
    total += 15
elif size == "M":
    total += 20
elif size == "L":
    total += 25
else:
    print("Try again")

if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "Y":
    total += 1


print(f"The total is ${total}. Thank you so much")
