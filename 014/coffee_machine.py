from symbol import return_stmt

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# separate
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Todo 3: Process coins
def process_coins ():
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    quarters *= 0.25
    dimes *= 0.10
    nickles *= 0.05
    pennies *= 0.01
    total = quarters + dimes + nickles + pennies
    return total


money = 0
print(MENU['espresso']['cost'], resources)

customer_choose = (input('What would you like? (espresso/latte/cappuccino): ')).lower()


# Todo 1: Print the report
if customer_choose == 'report':
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${money}")
elif customer_choose not in MENU:
    print(f"Sorry, there is no {customer_choose} in this coffee machine.")
else:
    print(MENU[customer_choose])
    customer_paid = process_coins()
    if customer_paid > MENU[customer_choose]['cost']:
        change = customer_paid - float(MENU[customer_choose]['cost'])

    print("Please insert coins.")

# Todo 2: Check resources sufficient

# Todo 4: Process order
# Todo 5: Take out the resources
# Todo 6: Add money
# Todo 7: Add resources