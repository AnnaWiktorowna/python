#Домашнее задание2
#Орел или решка
import random
print("Это игра Орел и Решка. Сейчас мы посмотрим сколько выпало орлов, а сколько решек")
heads = 0
tails = 0
tossing = 0
while tossing != 100:
    heads_or_tails = random.randint(1, 100)
    if heads_or_tails == 1:
        heads += 1
        tossing += 1
    elif heads_or_tails == 2:
        tails += 1
        tossing += 1
print("решек выпало", tails, "орлов выпало", heads)
input("/n/nНажмите Enter, чтобы выйти.")