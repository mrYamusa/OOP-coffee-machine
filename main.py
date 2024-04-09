from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
mymenu = Menu()
availableDrinks = mymenu.get_items()

goOn = True
while goOn:
    choice = input(f"What would you like to order? \n{availableDrinks}\nType 'quit' to quit and 'report' for a report ").lower()
    if choice == "report":
        print(coffeemaker.report())
    elif choice == "quit":
        goOn = False
    else:
        orderdetails = mymenu.find_drink(choice)
        print(orderdetails)
        if coffeemaker.is_resource_sufficient(orderdetails):
            if moneymachine.make_payment(orderdetails.cost):
                coffeemaker.make_coffee(orderdetails)
                print(coffeemaker.report())
                print(moneymachine.report())