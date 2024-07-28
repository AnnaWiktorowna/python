#домашнее задание3
#отгадай число
import random
print("\tДобро пожаловать в игру Отгадай число!")
print("Загадай натуральное число из диапазона от 1 до 100.")
print("А компьютер отгадает его")
number = int(input("Ваше число: "))
answer = random.randint(1, 100)
tossing = 1
while number != answer:
    if number > answer:
        print("Меньше")
    else:
        print("Больше")
    answer = random.randint(1, 100)
    tossing += 1
    #if tossing == 20:
     #   print("К сожалению у вас закончились попытки")
      #  break
    if answer == number:
        print("вам удалось отгадать число! Это в самом деле", number, "потрачено попыток", tossing)
        break
input("/n/nНажмите Enter чтобы выйти")