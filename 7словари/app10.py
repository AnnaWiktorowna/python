#Словари
#Добавление нового элемента в исходный словарь
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = car.keys()
print(x) #перед изменением
car["color"] = "white"
print(x) #после изменения
