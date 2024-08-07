#Анаграммы (Word Jumble)
#Компьютер выберает какое либо слово и хаотически переставляет его буквы
#Задача игрока - востановить исходное слово
import random 
#Создадим последовательность слов, из которых компьютер будет выберать
WORDS = ("питон", "анаграма", "простая", "сложная", "ответ", "подстаканник")
#random.choice():
#случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)
#создадим переменную, с которой будет затем сопоставленна версия игрока
correct = word
#создадим анаграмму выбраного слова, в которой буквы будут расставлены хаотично
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
#начало игры
print(
    """Добро пожаловать в игру Анаграммы!
        Надо переставить буквы так, чтобы получилось осмысленное слово.
    (Для выхода нажмите Enter, не вводя своей версии.)"""
)
print("Вот анаграмма:", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != correct and guess != "":
    print("К сожалению вы неправы.")
    guess = input("Попробуйте отгадать исходное слово: ")
if guess == correct:
    print("Да, именно так! Вы отгадали!\n")
print("спасибо за игру.")
input("\n\nНажмите Enter, чтобы выйти.")    