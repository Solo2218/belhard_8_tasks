"""
Садовник. Класс Gardener

Садовник, который может:
1. Ухаживать за растением
2. Собирать с него урожай

Атрибуты:
- name - имя садовника
- lants - список с растениями, за которыми ухаживает садовник

Методы:
- инициализатор __init__, который принимает name - имя садовника
  и args - произвольное количество кустов томата
- метод work(), который заставляет садовника работать, что позволяет всем растениям расти
- метод harvest(), который проверяет, все ли плоды созрели.
  Если созрели все плоды - садовник собирает урожай (метод возвращает список всех томатов),
  если нет - метод печатает предупреждение, что томаты не созрели и возвращает None.
"""

from tomato_bush import TomatoBush


class Gardener:
    name: str
    plants: list

    def __init__(self, name: str, *args):
        self.name = name
        self.plants = list(args)

    def work(self):
        for bush in self.plants:
            TomatoBush.grow_all(bush)

    def harvest(self):
        all_bush_are_ripe = 0
        all_tomato_list = []
        for bush in self.plants:
            if TomatoBush.all_are_ripe(bush):
                all_bush_are_ripe += 1
                all_tomato_list.append(TomatoBush.give_away_all(bush))
        if all_bush_are_ripe == len(self.plants):
            return all_tomato_list
        else:
            print("Томаты еще не созрели")
