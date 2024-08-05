#Домашнее задание
#Считалка
start_number = int(input("Введите начало счета\n"))
finish_number = int(input("Введите конец счета\n"))
interval = int(input("Введите интервал счета\n\n"))
for i in range(start_number, finish_number, interval):
    print(i)
input("\n\nНажмите Enter, чтобы выйти")