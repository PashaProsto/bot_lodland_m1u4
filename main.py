import telebot
import random
from telebot.types import ReactionTypeEmoji

bot = telebot.TeleBot("СВОЙ ТОКЕН")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! Напиши команду /help и начни работу со мной!')

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['calc'])
def calc(message):
    words = message.text.split()
    if len(words) > 2:
        if words[1] == 'summa' or words[1] == 'сумма':
            number = int(words[2])
            summa = 0
            if number < 0:
                for i in range (0, number - 1, -1):
                    summa += 1
            elif number > 0:
                for i in range (0, number + 1):
                    summa += i    
            else:
                summa = 0
            bot.reply_to(message, f'Сумма всех чисел от {number} до 0: {summa}')
        else:
            if len(words) == 4:
                number1 = int(words[1])
                number2 = int(words[3])
                simbol = words[2]
                result = 0
                if simbol == '+':
                    result = number1 + number2
                elif simbol == '*':
                    result = number1 * number2
                elif simbol == '-':
                    result = number1 - number2
                elif simbol == '/':
                    if number2 != 0:
                        result = number1 / number2
                    else:
                        result = 'Ошибка!!  На ноль делить нельзя!!!'
                bot.reply_to(message, f'Результат: {result}')
    else:
        result = 'Ошибка!!  Вы не дописали команду!!!!'
        bot.reply_to(message, f'{result}')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Команды для работы со мной: /help - показывает все функции бота, /calc summa (number) - если написать эту команду и вместо скобок число, то бот сложит все числа от введённого до нуля, /calc (число) (арифметиический знак) (число) - если написать эту команду и вместо скобок (число) поставить числа, а вместо (арифметиический знак) знак сложения/вычитания/умножения/деления, то бот как калькулятор решит пример, /heh или /heh (число) - если ввести без числа, то бот 5 раз выведет he, если с числом то выведет he определённое кол-во раз')


bot.polling()
