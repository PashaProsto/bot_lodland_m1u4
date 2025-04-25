import telebot
    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("7692841918:AAE6NQ2HidheurNs0f0ALcM-AaiVPBVdcRU")

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
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
            

# Запуск бота
bot.polling()
