#Анализатор текста
#демонстрирует работу функции len() и оператора in
message = input("Введите текст: ")
print("\nДлина введенного вами текста составляет:", len(message))
print("\nСасмая частая слогласная, 'т',")
if "т" in message:
    print("встречается в нашем тексте.")
else:
    print("не встречается в нашем тексте.")
input("\n\nНажмите Enter, чтобы выйти.")