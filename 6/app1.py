#Арсенал героя  3.0
#Демонстрирует работу со списками
#создадим список с несколькими элементами и выведем его с помощью цыкла for
inventory = ["меч", "кольчуга", "щит", "целебное снадобье"]
print("\nИтак, в нашем арсенале:")
for item in inventory:
    print(item)
input("\nНажмите Enter, чтобы продолжить.")

#найдем длину списка
print("Сейчас в вашем распоряжении", len(inventory), "предмета/-ов.")
input("\nНажмите Enter, чтобы продолжить.")

#проверка на принадлежность списку с помощью in
if "целебное снадобье" in inventory:
    print("Вы еще поживете и повоюете.")

#вывод одного элемента с определенным индексом
index = int(input("\nВведите индекс одного из предметов арсенала: "))
print("Под индексом", index, "в арсенале находится", inventory[index])

#отобразим срез
start =  int(input("\nВведите начальный индекс среза: "))
finish =  int(input("\nВведите конечный индекс среза: "))

print("Срез в списке[", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])
input("\n\nНажмите Enter, чтобы продолжить.")

#Соединяем два списка
chest = ["золото", "драгоценные камни"]
print("\nВы нашли ларец. Вот что в нем есть:")
print(chest)
print("Вы приобщили содержимое ларца к своему арсеналу.")
inventory += chest
print("\nТеперь в вашем распоряжении:")
print(inventory)
input("\n\nНажмите Enter, чтобы продолжить")

#присваиваем значение элементу по индексу
print("Вы обменяли меч на арбалет.")
inventory[0] = "арбалет"
print("Теперь ваш арсенал содержит следующие элементы:")
print(inventory)
input("\n\nНажмите Enter, чтобы продолжить")

#присваиваем значения элементам по срезу индексов
print("За золото и драгоценные камни вы купили магический кристалл, способный предсказывать будущее.")
inventory[4:6] = ["магтческий кристалл"]
print("Теперь в вашем распоряжении:")
print(inventory)
input("\n\nНажмите Enter, чтобы продолжить")

#удаляем элемент
print("В тяжелом бою был раздроблен ваш щит.")
del inventory[2]
print("Вот что осталось в вашем арсенале:")
print(inventory)
input("\n\nНажмите Enter, чтобы продолжить")

#удаляем срез
print("Воры лишили вас арбалета и кольчуги.")
del inventory[:2]
print("В арсенале теперь только:")
print(inventory)
input("\n\nНажмите Enter, чтобы выйти")

