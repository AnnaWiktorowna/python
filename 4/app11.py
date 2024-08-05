#Домашнее задание
#Перевертыш
text = input("Введите текст, который вернется написанный в обратном порядке")
dlina = len(text)
text_new = ""
while text:
    text_new += text[dlina-1]
    text = text[:dlina-1]
    dlina = len(text)
print(text_new)
input("\n\nНажмите Enter, чтобы выйти")