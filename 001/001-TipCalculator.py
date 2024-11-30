print("Welcome to the tip calculator!")

totalBill = input("What was the total bill?: ")

tipPercentage = input("How much tip would you like to give? 15, 18, or 20?: ")
tipCal = f"1.{str(tipPercentage)}"
tip = float(tipCal)
print(tip)

splittingPeople = input("How many people to split the bill?: ")

eachPersonPay = round((float(totalBill) * tip / float(splittingPeople)), 2)

print(f"Each person should pay: ${eachPersonPay}")
