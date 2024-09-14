#Словари
#Доступ к элементам, можно получить с помощью метода get()
#Получить значение ключа "модель"
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = thisdict.get("model")
print(x)
