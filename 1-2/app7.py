#Домашнее задание3
#Цена автомобиля
car = int(input("Введите стоимомть автомобиля без наценок: "))
tax = car * 0.15
print("Налог: ", tax)
collection = car * 0.10
print("Регистрационный сбор: ", collection)
fee = 1200
print("Агентский сбор: ", fee)
delivery = 2000
print("Доставка машины: ", delivery)
price = car + tax + collection + fee + delivery
print("Окончательная цена автомобиля: ", price)
input("\n\nНажмите Enter, чтобы выйти.")
