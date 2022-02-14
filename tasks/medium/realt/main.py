"""
## Задача. Файл main.py

В блоке
```python
if __name__ == '__main__':
    pass
```
выполнить следующие задания:
1. Создать несколько объектов классов House и Townhouse
2. Создайте объект Person
3. Используя объект класса Person, увеличить количество денег
4. Попробуйте купить дома
5. Если денег не достаточно, то продолжить увеличивать количество денег
"""

from house import House
from townhouse import Townhouse
from person import Person

if __name__ == '__main__':
    house_1 = House('Минск', 32, 87000)
    house_2 = House('Гомель', 47, 72000)
    house_3 = Townhouse('Заславль', 55000)
    house_4 = Townhouse('Смолевичи', 50600)
    house_list = [house_1, house_2, house_3, house_4]
    person_1 = Person('Somepersone', 25)
    person_1.earn_money(10000)
    person_1.make_deal(house_3)
    person_1.earn_money(100000)
    person_1.earn_money(25000)
    person_1.earn_money(15000)
    person_1.make_deal(house_1)
