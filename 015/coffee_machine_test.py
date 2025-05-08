from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
order.find_drink("espresso")
order.get_items()

coffee_machine = CoffeeMaker()

# print(order.find_drink("espresso"))
print(order.get_items())

customer_pay = MoneyMachine()
# process_coin.process_coins()

# Check if resource sufficient
print(coffee_machine.is_resource_sufficient(order.find_drink("espresso")))


print(order.find_drink("latte").cost)

# cost_1 = order.find_drink(customer_choose).cost
# print(cost_1)
# print(f"We have {customer_choose}")
# # print(f"customer paid {customer_pay.process_coins()}")
# # if customer_pay.process_coins() >=
print(coffee_machine.report())

# Get resource
print(coffee_machine.resources["water"])
# get ingredient
print(order.find_drink("latte").ingredients["water"])

# Print current resource
print(coffee_machine.resources)

# call function report from the coffee_maker.py
# this will print in the function if user print(coffee_machine.report()) <-- it will print None in the end
coffee_machine.report()

# call function report from the money_maker.py
# this will print in the function if user print(customer_pay.report()) <-- it will print None in the end
customer_pay.report()