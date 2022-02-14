"""
## Задача. Файл main.py

В блоке
```python
if __name__ == '__main__':
    pass
```
выполнить следующие задания:
1. Создать несколько объектов класса TomatoBush,
   в каждом из которых будет минимум по 2 помидора
2. Создайте объект Gardener, в который передать объекты, созданные в п.1
3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
4. Попробуйте собрать урожай
5. Если томаты еще не дозрели, продолжайте ухаживать за ними
6. Соберите урожай
7. Вывести сообщение о том, сколько томатов собрали
"""

from tomato import Tomato
from tomato_bush import TomatoBush
from gardener import Gardener

if __name__ == '__main__':
    tomato_1 = Tomato(1)
    tomato_2 = Tomato(2)
    tomato_3 = Tomato(3)
    tomato_4 = Tomato(5)
    tomato_5 = Tomato(4)
    tomato_6 = Tomato(6)
    bush_1 = TomatoBush(tomato_1, tomato_2)
    bush_2 = TomatoBush(tomato_3, tomato_4)
    bush_3 = TomatoBush(tomato_5, tomato_6)
    gardener = Gardener("Sumname", bush_1, bush_2, bush_3)
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.work()
    tomato = gardener.harvest()
    summa = 0
    for i in range(len(tomato)):
        for y in range(len(tomato[i])):
            summa += 1
    print(f"Собрано {summa} томатов")
