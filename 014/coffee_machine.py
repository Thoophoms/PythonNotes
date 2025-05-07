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


# print(f"checking {MENU['espresso']['ingredients']['water']} and {resources['water']}")

# Todo 2: Check resources sufficient
def check_resources(order):
    missing = []
    ingredients = MENU[order]['ingredients']

    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            missing.append(item)

    if missing:
        return False, missing # for not enough resources
    else:
        return True, [] # all resources are sufficient



# Todo 3: Process coins
def process_coins ():
    print("Please insert coins.")
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

# Todo 5: Take out the resources
def process_resources(order):
    if order == 'espresso':
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
    else:
        resources['water'] -= MENU[order]['ingredients']['water']
        resources['milk'] -= MENU[order]['ingredients']['milk']
        resources['coffee'] -= MENU[order]['ingredients']['coffee']
    return resources



money = 0
print(MENU['espresso']['cost'], resources)

machine__not_off = True
# start while loop here!!

while machine__not_off:
    customer_choose = (input('What would you like? (espresso/latte/cappuccino): ')).lower()

    # Todo 1: Print the report
    if customer_choose == 'report':
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${money}")
    elif customer_choose == 'fill':
        resources['water'] = 300
        resources['milk'] = 200
        resources['coffee'] = 100
    elif customer_choose == 'off':
        print("Machine is now off!")
        machine__not_off = False
    elif customer_choose not in MENU:
        print(f"Sorry, there is no {customer_choose} in this coffee machine.")
    else:
        print(MENU[customer_choose])
        enough_resources, missing_items = check_resources(customer_choose)
        if enough_resources:
            customer_paid = process_coins()
            if customer_paid > MENU[customer_choose]['cost']:
                change = round(customer_paid - float(MENU[customer_choose]['cost']), 2)
                print(f"Here is ${change} in change. Coffee is ready Enjoy!")
                # process_resources(customer_choose)
                print(process_resources(customer_choose))
                money += MENU[customer_choose]['cost']
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough: {', '.join(missing_items)}.")





# Todo 4: Process order


# Todo 6: Add money
# Todo 7: Add resources