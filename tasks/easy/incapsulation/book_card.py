"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self, author: str, title: str, year: int):
        self.author = author
        self.title = title
        self.year = year

    def __eq__(self, other):
        return self.__year == other.__year

    def __gt__(self, other):
        return self.__year > other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @author.setter
    def author(self, author):
        if isinstance(author, str):
            self.__author = author
        else:
            raise ValueError

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self.__title = title
        else:
            raise ValueError

    @year.setter
    def year(self, year):
        if isinstance(year, int) and (0 < year <= CURRENT_YEAR):
            self.__year = year
        else:
            raise ValueError
