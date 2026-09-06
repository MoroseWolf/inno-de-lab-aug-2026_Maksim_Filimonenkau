MAX_RENTAL_BATCH_LIMIT = 150.0

"""
1. Использовать константу MAX_RENTAL_BATCH_LIMIT = 150.0, объявленную на 
уровне модуля.  
2. Добавить Type Hints для всех входящих аргументов и возвращаемого кортежа 
tuple[float, bool]. 
3. Оформить подробный Docstring в стиле Google (разделы Args и Returns). 
4. Написать функцию calculate_rental_batch: 
○ Обязательные параметры: quantity (int), rental_rate (float). 
○ Опциональный параметр: discount (float, по умолчанию 0.0). 
○ Логика: рассчитать final_sum = quantity * rental_rate * (1 - 
discount) (округлить до 2 знаков) и проверить превышение 
MAX_RENTAL_BATCH_LIMIT. 
○ Возврат: кортеж (final_sum, is_limit_exceeded).
"""


def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    """Hасчет стоимости партии дисков с учетом жанровой скидки.

    Args: 
    quantity (int): количество дисков
    rental_rate (float): стоимость одного экземпляра
    discount (float, optional): скидка на диск данного жанра

    Return:
    tuple[float, bool]: кортеж с стоимостью партии дисков и информацией превышает ли она лимит
    """

    final_sum = round(quantity * rental_rate * (1-discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return (final_sum, is_limit_exceeded)


"""
● Партия 1 («Academy Dinosaur»): 30 дисков по 2.99 $ (без скидки). 
● Партия 2 («Affair Prejudice»): 40 дисков по 4.99 $ (скидка 10%). 
● Партия 3 («Agent Truman»): 10 дисков по 1.99 $ (без скидки). 
● Партия 4 («African Egg»): 50 дисков по 3.50 $ (скидка 20%). 
"""

print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ === ")
test_1 = calculate_rental_batch(30, 2.99)
test_2 = calculate_rental_batch(40, 4.99, 0.1)
test_3 = calculate_rental_batch(10, 1.99)
test_4 = calculate_rental_batch(50, 3.50, 0.2)
print(
    f"""Партия 1 (Academy Dinosaur): Сумма {test_1[0]}$. Превышение лимита: {test_1[1]}
Партия 2 (Affair Prejudice): Сумма {test_2[0]}$. Превышение лимита: {test_2[1]}
Партия 3 (Agent Truman): Сумма {test_3[0]}$. Превышение лимита: {test_3[1]}
Партия 4 (African Egg): Сумма {test_4[0]}$. Превышение лимита: {test_4[1]}
""")
