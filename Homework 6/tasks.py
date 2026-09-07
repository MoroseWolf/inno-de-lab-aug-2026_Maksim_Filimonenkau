from random import randint

print("------------------------------------\nЗадание 1:Приветствие")
# Задание 1:Приветствие
name = input("Как тебя зовут? ")
print(f"Привет, {name}! Приятно познакомиться")

print("------------------------------------\nЗадание 2:Площадь прямоугольника")
# Задание 2:Площадь прямоугольника
width = input("Введите ширину прямоугольника: ")
length = input("Введите длину прямоугольника: ")
print(f"Площадь прямоугольника: {int(width)*int(length)}")

print("------------------------------------\nЗадание 3:Конвертер температур")
# Задание 3:Конвертер температур
temperatureC = input("Введите температуру в градусах Цельсия: ")
temperatureF = float(temperatureC) *9/5+32
print(f"{temperatureC}°C это {temperatureF}°F")

print("------------------------------------\nЗадание 4:Проверка на чётность")
# Задание 4:Проверка на чётность
number = input("Введите целое число: ")
if (int(number) % 2 == 0):
    print(f"Число {number} -- четное")
else:
    print(f"Число {number} -- нечетное")

print("------------------------------------\nЗадание 5:Игра «Угадай число»")
# Задание 4:Игра «Угадай число»
print("Я загадал число от 1 до 20. У тебя 5 попыток!")
attempts = 5
isFind = False
attemptNum = 1
hiddenNumber = randint(1, 20)
while attempts > 0:
    attempts -= 1
    userChoice = input(f"Попытка {attemptNum}. Введите число: ")
    if int(userChoice) == hiddenNumber:
        isFind = True
        break
    if int(userChoice) < hiddenNumber:
        print(f"Слишком мало! Осталось попыток: {attempts}")
        attemptNum+= 1
        continue
    if int(userChoice) > hiddenNumber:
        print(f"Слишком много! Осталось попыток: {attempts}")
        attemptNum += 1
        continue

if isFind == True:
    print("Ты угадал! Отличная работа")
else:
     print("Тебе не удалось угадать число :( Повезет в следующий раз!")
