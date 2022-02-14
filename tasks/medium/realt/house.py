"""
Дом. Класс House
Дом может:
1. Предоставлять информацию о себе
2. Изменять свою стоимость

Атрибуты:
- address - адрес дома
- area - площадь дома
- cost - стоимость дома

Методы:
- инициализатор __init__, который принимает адрес, площадь и начальную стоимость дома
- метод increase_cost(), который принимает значение, на которое нужно увеличить self.cost
- метод *ecrease_cost(), который принимает значение, на которое нужно уменьшить self.cost
"""


class House:
    address: str
    area: int
    cost: int

    def __init__(self, address: str, area: int, cost: int):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, increase: int):
        self.cost += increase

    def decrease_cost(self, decrease: int):
        self.cost -= decrease
