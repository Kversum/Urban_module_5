"""
Цель: понять как работают базовые магические методы на практике.
Задача "Магические здания":
Для решения этой задачи будем пользоваться решением к предыдущей задаче.
Необходимо дополнить класс House следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

Пример результата выполнения программы:
Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
10
20
"""


def cases(number):
    if number == 1:
        return 'этаж'
    elif 5 > number > 1:
        return 'этажа'
    elif number > 5 or number == 0:
        return 'этажей'


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f'Нужно приехать на {new_floor} этаж')
        if self.number_of_floors >= new_floor >= 1:
           for i in range(new_floor):
                print(i + 1)
        else:
            print(f'В объекте {self.name, self.number_of_floors} такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        info = f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
        return info


obj_1 = House('ЖК Горский', 18)
obj_2 = House('Домик в деревне', 3)
obj_1.go_to(11)
obj_2.go_to(10)
print(f'В здании {len(obj_1)} {cases(len(obj_1))}')
print(str(obj_1))
print(f'В здании {len(obj_2)} {cases(len(obj_2))}')
print(str(obj_2))
