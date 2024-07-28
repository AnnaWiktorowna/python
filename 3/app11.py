#домашнее задание3
#отгадай число
import random
print("\tДобро пожаловать в игру Отгадай число!")
print("Я загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за минимальное число попыток. Всего попыток 10")
number = random.randint(1, 100)
answer = int(input("Ваше предположение: "))
tossing = 1
while answer != number:
    if answer > number:
        print("Меньше")
    else:
        print("Больше")
    answer = int(input("Ваше предположение: "))
    tossing += 1
    if tossing == 10:
        print("К сожалению у вас закончились попытки")
        break
    elif answer == number:
        print("вам удалось отгадать число! Это в самом деле", number, "потрачено попыток", tossing)
        break
input("/n/nНажмите Enter чтобы выйти")