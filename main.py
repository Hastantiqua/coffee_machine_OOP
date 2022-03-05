from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    options = menu.get_items()
    order = input(f'What would you like? ({options}): ').lower()

    if order == 'off':
        print('Shutting down...')
        return
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)

        if drink is None:
            coffee_machine()

        if (coffee_maker.is_resource_sufficient(drink)
                and money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)

    coffee_machine()


if __name__ == '__main__':
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    coffee_machine()
