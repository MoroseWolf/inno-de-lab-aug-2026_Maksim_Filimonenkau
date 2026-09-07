from typing import Any
DEFAULT_RETURN_INDEX_BASE = 10.0

"""
1. Использовать константу DEFAULT_RETURN_INDEX_BASE = 10.0, 
объявленную на уровне модуля. 
2. Аннотировать типы: входящие параметры (с Any для сырых данных) и 
возвращаемый тип tuple[float, float] | None. 
3. Оформить подробный Docstring в стиле Google с разделами Args и Returns. В 
описании функции указать, какие ошибки входных данных обрабатываются 
функцией. 
4. Реализовать функцию calculate_overdue_fine: 
    ○ Блок try: 
        ■ Преобразовать days_overdue в float. 
        ■ Рассчитать total_fine = numeric_days * fine_rate. 
        ■ Рассчитать return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days. 
    ○ Блок except: 
        ■ TypeError — выписать сообщение об ошибке типа. 
        ■ ValueError — выписать сообщение о нерелевантной строке. 
        ■ ZeroDivisionError — выписать сообщение о нулевых днях просрочки. 
    ○ Блок finally: всегда выводит: --- Проверка транзакции возврата завершена ---. 
"""


def calculate_overdue_fine(film_title: Any, days_overdue: Any, fine_rate: Any) -> tuple[float, float] | None:
    """
    Отказоустойчивая функция расчета штрафа и технического индекса оборачиваемости.

    Функция обрабатывает следующие ошибки входных данных:
    TypeError: если тип данных дней просрочки несовместим с числовым преобразованием
    ValueError: если строковое значение дней просрочки не содержит корректного 
    ZeroDivisionError: если количество дней просрочки равно нулю, что делает невозможным расчет индекса оборачиваемости 
    (деление на ноль).

    Args:
    movie_title (Any): Название фильма (используется для логирования).
    days_overdue (Any): Сырые данные о количестве дней просрочки.
    fine_rate (Any): Сырые данные о ставке штрафа за один день.

    Returns:
    tuple[float, float] | None: Кортеж из (total_fine, return_index) в случае успешного расчета, 
    либо None в случае возникновения ошибки.
    """

    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        print(
            f"Фильм: {film_title} | Итоговый штраф: {total_fine} | Индекс: {return_index}")
        return total_fine, return_index
    except ValueError as e:
        print(
            f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для {film_title}: {e}")
    except ZeroDivisionError as e:
        print(
            f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для {film_title}: {e}")
    except TypeError as e:
        print(
            f"[ОШИБКА ТИПА] Некорректный тип данных для {film_title}: {e}")
    finally:
        print("--- Проверка транзакции возврата завершена ---.\n\n")

    return None


res1 = calculate_overdue_fine("Matrix", 5, 1.5)
res2 = calculate_overdue_fine("Inception", "пять", 2.0)
res3 = calculate_overdue_fine("Avatar", 0, 2.5)
res4 = calculate_overdue_fine("Interstellar", [3,], 3.0)
