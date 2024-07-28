#Домашнее задание1
#Пирожок с сюрпризом
import random
print("Ваш пирожок с сюрпризом это: ")
pie = random.randint(1, 5)
if pie == 1:
    print("с мясом")
elif pie == 2:
    print("с грибами")
elif pie == 3:
    print("с яблоком")
elif pie == 4:
    print("с маком")
elif pie == 5:
    print("с клубникой")
else:
    print("без начинки")
input("\n\nНажмите Enter чтобы выйти")