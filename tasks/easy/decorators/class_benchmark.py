"""
Написать декоратор класса class_benchmark, который будет проводить
бенчмарк (замер времени выполнения) всех публичных методов класса
(те, которые не начинаются с _).

Чтобы у методов класса изменить поведение - дополнительно написать
декоратор функции def_benchmark.

До выполнения метода должен быть вывод в консоль:
Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}
Время начала: {start_time}

После выполнения метода должен быть вывод в консоль:
Выполнено {func.__name__}
Время окончания: {end_time}
Всего затрачено времени на выполнение: {end_time - start_time}
"""
import time


def def_benchmark(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}")
        print(f"Время начала: {start_time}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Выполнено {func.__name__}")
        print(f"Время окончания: {end_time}")
        print(f"Всего затрачено времени на выполнение: {end_time - start_time}")
        return result

    return wrapper


def class_benchmark(cls):
    functions = {
        name: value for name, value
        in cls.__dict__.items()
        if callable(value) and not name.startswith("_")
    }
    for name, func in functions.items():
        func_with_decor = def_benchmark(func)
        setattr(cls, name, func_with_decor)
    return cls
