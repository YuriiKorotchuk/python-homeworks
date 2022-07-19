"""
Завдання №1

Розробити клас Людина. Людина має:

Ім'я
Прізвище
Вік (атрибут але ж змінний)
Стать
Люди можуть:

Їсти
Спати
Говорити
Ходити
Стояти
Лежати
Також ми хочемо контролювати популяцію людства. Змінювати популяцію можемо в __init__.
Треба сказати, що доступ до статичних полів класу з __init__ не можу іти через НазваКласу.статичий_атрибут,
позаяк ми не може бачити імені класу. Але натомість ми можемо сказати self.__class__.static_attribute.

"""
import datetime


class People:
    population = 0

    def __init__(self, name, surname, sex, age):
        self.name = name
        self.surname = surname
        self.__age = age
        self.sex = sex
        self.__class__.population += 1

    @property
    def age(self):
        return (datetime.date.today() - self.__age).days // 365

    def eat(self):
        if self.sex == "жінка":
            return f"{self.name} пішла погамати в львівські круасани"
        elif self.sex == "чоловік":
            return f"{self.name} пішов погамати в львівські круасани"
        else:
            return f"{self.name} пішло погамати в львівські круасани"

    def sleep(self):
        if self.sex == "жінка":
            return f"{self.name} пішла дрихнути"
        elif self.sex == "чоловік":
            return f"{self.name} пішов дрихнути"
        else:
            return f"{self.name} пішло дрихнути"

    def talk(self):
        return f"{self.name} балакає на закарпатському акценті"

    def stand(self):
        if self.sex == "жінка":
            return f"{self.name} завмерла на місці"
        elif self.sex == "чоловік":
            return f"{self.name} завмер на місці"
        else:
            return f"{self.name} завмерло"

    def lie_down(self):
        if self.sex == "жінка":
            return f"{self.name} прилягла"
        elif self.sex == "чоловік":
            return f"{self.name} приліг"
        else:
            return f"{self.name} прилягнуло"


Person_1 = People("Анджеліна", "Джолі", "жінка", datetime.date(1975, 10, 12))
Person_2 = People("Джоні", "Депп", "чоловік", datetime.date(1963, 11, 25))
print(Person_1.eat())
print(Person_2.eat())
print(Person_1.sleep())
print(Person_2.sleep())
print(Person_1.talk())
print(Person_2.talk())
print(Person_1.stand())
print(Person_2.stand())
print(Person_1.lie_down())
print(Person_2.lie_down())
print(People.population)
print(Person_1.age)
print(Person_2.age)
