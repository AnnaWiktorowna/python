#Кортежи
#Удаление элемента
#Преобразуем кортеж в список, удаляем "apple" и преобразуем его обратно в кортеж 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)
