#Кортежи
#Преобразовать кортеж в список, добавить элемент с помощью append() "orange" 
#Преобразовать назад в кортеж
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)
