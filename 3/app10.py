#домашнее задание3
#отгадай число
import random
print("\tДобро пожаловать в игру Отгадай число!")
print("Я загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за минимальное число попыток. Всего попыток 10")
tossing = 10
answer = 0
damege = 1
number = random.randint(1, 100)
while number != 100:
    answer = int(input("Ваше предположение: "))
    if answer == number:
        tossing -= damege
        print("вам удалось отгадать число! Это в самом деле", number, "осталось попыток", tossing)
        break
    elif answer >= number:
        tossing -= damege
        print("Меньше")
    elif answer <= number:
        tossing -= damege
        print("Больше")
    elif tossing == 0:
        tossing -= damege
        print("К сожалению у вас закончились попытки")
        break
input("/n/nНажмите Enter чтобы выйти")