#Словари
#Добавление нового элемента в исходный словарь
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

x = car.values()
print(x) #перед изменением

car["color"] = "red"
print(x) #после изменения
