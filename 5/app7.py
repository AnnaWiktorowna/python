#Демонстрирует добавление в список кортежа с помощью метода extend(). 
#Элемент будет добавлен в конец списка  
thislist = ["apple", "banana", "cherry"] #список
thistuple = ("mango", "pineapple", "papaya") #кортеж
thislist.extend(thistuple) #добавление кортежа в список
print(thislist)
input("\n\nНажмите Enter, чтобы выйти")