from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
order.find_drink("espresso")
order.get_items()

coffee_machine = CoffeeMaker()
customer_pay = MoneyMachine()


is_on = True

while is_on:
    # Ask what customer wants
    customer_choose = (input(f'What would you like? {order.get_items()}: ')).lower()
    if customer_choose == "report":
        coffee_machine.report()
        customer_pay.report()
    elif customer_choose == 'off':
        is_on = False
    else:
        # Todo: Check if there is an order in this machine
        order_on_menu = order.find_drink(customer_choose)
        if order_on_menu:
            # Todo: Check for the resources sufficient
            enough_resources = coffee_machine.is_resource_sufficient(order.find_drink("espresso"))
            if enough_resources:
                # Todo: check of the customer have enough money to pay for the drink
                # find the menu cost
                order_cost = order.find_drink(customer_choose).cost
                enough_money = customer_pay.make_payment(order_cost)
                if enough_money:
                    coffee_machine.make_coffee(order_on_menu)


