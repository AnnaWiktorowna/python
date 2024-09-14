#Словари
#Внесение элемента в исходный словарь
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

x = car.values()
print(x) #перед изменением

car["year"] = 2020
print(x) #после изменения
