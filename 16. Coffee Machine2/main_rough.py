from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_choice = Menu()
choice_of_item = menu_choice.get_items()  # the get_items method prints --> latte/espresso/cappuccino/
choice = input(f"What would you like? ({choice_of_item}): ")

if choice == "off":
    is_on = False
elif choice == "report":
    maker_of_coffee = CoffeeMaker().report()
    print(maker_of_coffee)
    monies = MoneyMachine().report()
    print(monies)
else:
    menu_choice = Menu()
    drink_item = menu_choice.find_drink(choice)  # confirms the drink's location if it exists
    # print(drink_item)
    in_coffee_made = CoffeeMaker()
    resource_is_sufficient = in_coffee_made.is_resource_sufficient(drink_item)
    # print(resource_is_sufficient)  # True if resource is sufficient
    if resource_is_sufficient:
        money = MoneyMachine()
        payment = money.process_coins()
        print(payment)
    # items_in_menu = MenuItem()
    # price = items_in_menu.cost

    price = ""
    for item in Menu().menu:
        if item.name == choice:
            price += f"{item.cost}"
    print(price)

    if money.make_payment(float(price)):
        in_coffee_made.make_coffee(drink_item)
