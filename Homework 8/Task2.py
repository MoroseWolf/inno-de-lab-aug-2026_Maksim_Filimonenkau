from time import perf_counter
from typing import Any, Callable

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8

"""
1. Использовать константы PERFORMANCE_LOG_PREFIX = "[PERF_LOG]" и
TIME_DECIMALS = 8, объявленные на уровне модуля.
2. Использовать Type Hints: аннотировать декоратор с помощью Callable и Any, а
данные о выручке жанров — как list[dict[str, str | float]].
3. Оформить подробный Docstring в стиле Google для декоратора и целевой
функции.
4. Написать кастомный декоратор performance_logger:
    ○ Принимает целевую функцию func.
    ○ Сохраняет время начала выполнения (используя time.perf_counter()).
    ○ Выполняет оригинальную функцию с любыми переданными аргументами
(*args, **kwargs).
    ○ Вычисляет время работы и выводит сообщение в формате:
<PERFORMANCE_LOG_PREFIX> Функция '<func.__name__>' выполнена
за <время> сек.
    ○ Возвращает результат работы оригинальной функции.
5. Написать основную функцию get_sorted_report, обернутую декоратором
@performance_logger:
    ○ Принимает список словарей (данные по выручке жанров).
    ○ Сортирует список по убыванию ключа total_sales с использованием
встроенной функции sorted() и lambda-выражения.
    ○ Возвращает отсортированный список.
"""


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Декоратор для логирования времени выполнения функции.
    Замеряет время работы целевой функции с и выводит результат в консоль.

    Args:
    func (Callable[..., Any]): Целевая функция для декорирования.

    Returns:
    Callable[..., Any]: Обернутая функция с логированием времени выполнения.
"""
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        print(
            f"{PERFORMANCE_LOG_PREFIX} Функция {func.__name__} выполнена за {end_time-start_time:.{TIME_DECIMALS}f} сек.")
        return result
    return wrapper


@performance_logger
def get_sorted_report(data: list[dict[str, str | float]]) -> list[dict[str, str | float]]:
    """
    Сортирует данные о выручке по убыванию общей выручки.

    Args:
    data (list[dict[str, str | float]]): Список словарей с данными о выручке.
    Каждый словарь должен содержать ключи 'category' (str) и 'total_sales' (float).

    Returns:
    list[dict[str, str | float]]: Новый список словарей, отсортированный по 
    убыванию значения 'total_sales'.
    """
    return sorted(data, key=lambda item: item["total_sales"], reverse=True)


# Набор 1 (Стандартный)
set_1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55}
]
# Набор 2 (С одинаковой выручкой)
set_2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00}
]
# Набор 3 (Единичный элемент)
set_3 = [
    {"category": "Drama", "total_sales": 500.00}
]

result_1 = get_sorted_report(set_1)
result_2 = get_sorted_report(set_2)
result_3 = get_sorted_report(set_3)


print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")
print(f"--- ТЕСТ 1 ---\nТоп категорий по выручке:")
for i, item in enumerate(result_1, start=1):
    print(f"{i}. {item['category']}: {item['total_sales']}")

print(f"\n--- ТЕСТ 2 ---\nТоп категорий по выручке:")
for i, item in enumerate(result_2, start=1):
    print(f"{i}. {item['category']}: {item['total_sales']}")

print(f"\n--- ТЕСТ 3 ---\nТоп категорий по выручке:")
for i, item in enumerate(result_3, start=1):
    print(f"{i}. {item['category']}: {item['total_sales']}")
