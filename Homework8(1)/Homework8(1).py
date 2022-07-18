"""""
Створити клас Vehicle (транспортний засіб):

ні від чого не наслідується
в ініціалізатор класу (__init__ метод) передати
producer: str
model: str
year: int
tank_capacity: float # обєм паливного баку
tank_level: float = 0 # початковий параметр рівня паливного баку дорівнює 0, параметр в аргументах не передавати
max_speed: int
fuel_consumption: float # litres/100km споживання пального
odometer_value: int = 0 # при сході з конвеєра пробіг нульовий, параметр в аргументах не передавати

визначити метод __repr__, яким повертати інформаційну стрічку (наповнення на ваш вибір, проте параметри model
and year and odometer_value мають бути передані

написати метод refueling, який не приймає жодного аргумента, заправляє автомобіль на уявній автозаправці
до максимума (tank_level = tank_capacity), після чого виводить на екран повідомлення, скільки літрів було заправлено
(перша заправка буде повного баку, а в інших випадках величина буде залежати від залишку пального в баку)

написати метод race, який приймає один аргумент (не враховуючи self) - відстань, яку потрібно проїхати,
а повертає словник, в якому вказано, скільки авто проїхало, з огляду на заповнення паливного баку перед поїздкою,
залишок пального (при малому кілометражі все пальне не використається), та час, за який відбулася дана поїздка,
з урахування, що середня швидкість складає 80% від максимальної (витрата пального рівномірна незалежно від швидкості)

за результатами роботи метода в атрибуті tank_level екземпляра класа має зберігатися
залишок пального після поїздки (зрозуміло, що не менше 0)

збільшити на величину поїздки показники odometer_value

написати метод lend_fuel, який приймає окрім self ще й other обєкт, в результаті роботи якого паливний бак обєкта,
на якому було викликано відповідний метод, наповнюється до максимального рівня за рахунок відповідного зменшення
рівня пального у баку дружнього транспортного засобу

вивести на екран повідомлення з текстом типу "Дякую, бро, виручив. Ти залив мені *** літрів пального"

у випадку, якщо бак першого обєкта повний або у другого обєкта немає пального,
вивести повідомлення "Нічого страшного, якось розберуся"

написати метод get_tank_level, для отримання інформації про залишок пального конкретного інсттанса

написати метод get_mileage, який поверне значення пробігу odometer_value

написати метод __eq__, який приймає окрім self ще й other обєкт
(реалізація магічного методу для оператора порівняння ==)

даний метод має повернути True у випадку, якщо 2 обєкта, які порівнюються, однакові за показниками року випуску
та пробігу (значення відповідних атрибутів однакові, моделі можуть бути різними)

створіть не менше 2-х обєктів класу, порівняйте їх до інших операцій, заправте їх, покатайтесь на них на
різну відстань, перевірте пробіг, позичте один в одного пальне, знову порівняйте
"""


class Vehicle:
    def __init__(self,
                 producer: str,
                 model: str,
                 year: int,
                 tank_capacity: float,
                 max_speed: int,
                 fuel_consumption: float,
                 tank_level: float = 0,
                 odometer_value: int = 0):

        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.fuel_consumption = fuel_consumption
        self.tank_level = tank_level
        self.odometer_value = odometer_value
        self.max_speed = max_speed

    def __repr__(self):
        return f"Характеристики автомобіля(модель, рік, пробіг): {self.model}, {self.year}, {self.odometer_value}."

    def refueling(self):
        if self.tank_level == self.tank_capacity:
            print(f"У вас повний бак")
        else:
            print(f"Ви залили {self.tank_capacity - self.tank_level} літрів пального")
            self.tank_level = self.tank_capacity

    def lend_fuel(self, other):
        gas_filled = self.tank_level
        if self.tank_level == self.tank_capacity or other.tank_level == 0:
            print("Нічого страшного, якось розберуся")
        else:
            while self.tank_level < self.tank_capacity and other.tank_level > 0:
                self.tank_level += 1
                other.tank_level -= 1
            print(f"Дякую, бро, виручив. Ти залив мені {self.tank_level - gas_filled} літрів пального")

    def get_tank_level(self):
        return f"У вас {self.tank_level} літрів пального в баці"

    def get_mileage(self):
        return f"У вас {self.odometer_value} пробігу на машині"

    def __eq__(self, other):
        return self.year == other.year and self.odometer_value == other.odometer_value

    def race(self, distance):
        time_of_trip = distance / self.max_speed * 0.8
        self.tank_level -= distance / 100 * self.fuel_consumption
        self.odometer_value = self.odometer_value + distance
        if self.tank_level < 0:
            self.tank_level += distance / 100 * self.fuel_consumption  # аби не був від'ємний бак
            self.odometer_value = self.odometer_value - distance  # аби не додавався лишній пробіг
            return "Пального на данну відстань не хватає"
        else:
            return dict(your_distance=distance, time=time_of_trip, gas=self.tank_level, odometer=self.odometer_value)


Super_car_1 = Vehicle("USA", "Chevrolet Impala", 1967, 75, 150, 26, 22)
Super_car_2 = Vehicle("USA", "Ford Mustang", 1987, 83, 250, 18, 24)
print(Super_car_1.__eq__(Super_car_2))
Super_car_1.refueling()
Super_car_2.refueling()
print(Super_car_1.race(50))
print(Super_car_2.race(400))
print(Super_car_1.get_mileage())
print(Super_car_2.get_mileage())
Super_car_1.lend_fuel(Super_car_2)
print(Super_car_1.__eq__(Super_car_2))
