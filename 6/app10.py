#Распределенные ссылки 
#делаем полный срез, чтобы изменения не были для всех переменных
mike = ["белая рубашка", "комбинезон цвета хаки", "пиджак"]
mr_dawson = mike
honey = mike[:]
honey[2] = "красный свитер"
print(mike)
print(mr_dawson)
print(honey)
