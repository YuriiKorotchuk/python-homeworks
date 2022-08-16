from enum import Enum


def supplements(cls):
    def wrapper():
        def cinnamon(self):
            self.price += 20
        cls.cinnamon = cinnamon

        def liquer(self):
            self.price += 50
        cls.liquer = liquer

        def syrop(self):
            self.price += 30
        cls.syrop = syrop
        return cls
    return wrapper()


class Discounts_levels(Enum):
    STANDART = (0.5, 50)
    MEDIUM = (1.5, 100)
    HIGH = (2.0, 250)
    HIGHEST = (3.0, 300)

    def __init__(self, discount, price):
        self.discount = discount
        self.price = price


@supplements
class Espresso:
    def __init__(self):
        self.name = Espresso
        self.price = 40


@supplements
class Latte:
    def __init__(self):
        self.name = Latte
        self.price = 50


@supplements
class Cappuccino:
    def __init__(self):
        self.name = Cappuccino
        self.price = 55


class CoffeeMachine:
    def __init__(self):
        self.money = 0

    @staticmethod
    def discount_calculation(coffee_price):
        if coffee_price >= tuple(Discounts_levels.__members__.values())[3].price:
            return tuple(Discounts_levels.__members__.values())[3].discount
        if coffee_price >= tuple(Discounts_levels.__members__.values())[2].price:
            return tuple(Discounts_levels.__members__.values())[2].discount
        if coffee_price >= tuple(Discounts_levels.__members__.values())[1].price:
            return tuple(Discounts_levels.__members__.values())[1].discount
        if coffee_price >= tuple(Discounts_levels.__members__.values())[0].price:
            return tuple(Discounts_levels.__members__.values())[0].discount
        return 0

    def change_calculation(self, coffee_type, buyer):
        if coffee_type.price <= self.money:
            discount = coffee_type.price * CoffeeMachine.discount_calculation(coffee_type.price)/100
            change = self.money - (coffee_type.price - discount)
            self.money = 0
            buyer.money += change
            return f"Done, withdrew is {coffee_type.price - discount} UAH. Discount value is {discount} UAH"


class Buyer:
    def __init__(self, name: str, surname: str, money: int):
        self.name = name
        self.surname = surname
        self.money = money

    def depositing_money(self, coffee_machine: CoffeeMachine):
        money_value = input("Enter the money value: ")
        try:
            money = int(money_value)
        except ValueError:
            raise ValueError(f"Entered wrong data ( should be int )")
        else:
            if self.money < money:
                raise ValueError("Don't have enough funds")
            coffee_machine.money += money
            self.money -= money
            return f"You deposited UAH {money} into the account"

    def coffee_creation(self, coffee_machine: CoffeeMachine):
        coffee_type = input("Enter the coffee type that you want (example: latte, cappuccino, espresso): ")
        if coffee_type != "latte" and coffee_type != "cappuccino" and coffee_type != "espresso":
            return "You entered the wrong data (example: latte, cappuccino, espresso)"
        else:
            if coffee_type == "espresso":
                coffee_type = Espresso()
            elif coffee_type == "latte":
                coffee_type = Latte()
            elif coffee_type == "cappuccino":
                coffee_type = Cappuccino()
            supplement_type = input("Enter the type of supplements that you want (example: cinnamon, liquer, syrop): ")
            if supplement_type == "cinnamon":
                coffee_type.cinnamon()
            elif supplement_type == "liquer":
                coffee_type.liquer()
            elif supplement_type == "syrop":
                coffee_type.syrop()
            return coffee_machine.change_calculation(coffee_type, self)


if __name__ == "__main__":
    buyer_1 = Buyer("Johny", "Depp", 3000)
    coffee_machine = CoffeeMachine()
    print(f"The value of buyer money before: {buyer_1.money} UAH")
    print(buyer_1.depositing_money(coffee_machine))
    print(buyer_1.coffee_creation(coffee_machine))
    print(f"The value of buyer money after: {buyer_1.money} UAH")