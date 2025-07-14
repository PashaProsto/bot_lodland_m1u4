import telebot
import random
import os

# Инициализация бота с использованием его токена
bot = telebot.TeleBot("Bot_Token")
memes_prog = os.listdir('./images_prog')
memes_animal = os.listdir('./images_animal')
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! Напиши команду /help и начни работу со мной!')

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
            if number >= 0:
                summa = number * (number + 1) // 2
            else:
                summa = number * (number - 1) // 2 * -1
            bot.reply_to(message, f'Сумма всех чисел от 0 до {number}: {summa}')
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
def send_help(message):
    bot.reply_to(message, ''' Команды для работы со мной: /help - показывает все функции бота,
 /calc summa (number) - если написать эту команду и вместо скобок число, то бот сложит все числа от введённого до нуля,
 /calc (число) (арифметический знак) (число) - если написать эту команду и вместо скобок (число) поставить числа, а вместо (арифметиический знак) знак сложения/вычитания/умножения/деления, то бот как калькулятор решит пример,
 /heh или /heh (число) - если ввести без числа, то бот 5 раз выведет he, если с числом то выведет he определённое кол-во раз,
 /mem или /mem (число) - если ввести без числа, то вм выдастся рандомный мем, если с числом, то определённый мем под числом, которое вы написали (эту же функцию делает /animals),
 /ecology - выдаст вам инстуркцию по использованию команды''')

@bot.message_handler(commands=['mem'])
def mem(message):
    memes_prog = os.listdir('./images_prog')
    meme = message.text.split()
    if len(meme) > 1:
        number_name = int(meme[1]) - 1
        if 0 <= number_name < len(memes_prog):
            with open(f'images_prog/{memes_prog[number_name]}', 'rb') as f:
                return bot.send_photo(message.chat.id, f)
        else:
            return bot.reply_to(message, f'Мема с таким номером нету')

    r_mem = random.choice(memes_prog)
    with open(f'images_prog/{r_mem}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    memes_prog.remove(r_mem)
    if memes_prog == []:
        memes_prog = os.listdir('./images_prog')

@bot.message_handler(commands=['animals'])
def mem(message):
    global memes_animal
    meme = message.text.split()
    if len(meme) > 1:
        number_name = int(meme[1]) - 1
        if 0 <= number_name < len(memes_animal):
            with open(f'images_animal/{memes_animal[number_name]}', 'rb') as f:
                return bot.send_photo(message.chat.id, f)
        else:
            return bot.reply_to(message, f'Мема с таким номером нету')

    r_mem = random.choice(memes_animal)
    with open(f'images_animal/{r_mem}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    memes_animal.remove(r_mem)
    if memes_animal == []:
        memes_animal = os.listdir('./images_animal')

@bot.message_handler(commands=['ecology'])
def ecology(message):
    eco = message.text.split()

    podelka_1 = 'Подделки из пластиковых тарелок: мордашки животных, аппликации, кукольный театр.'
    podelka_2 = 'Подделки из пластиковых бутылок: декор для сада, цветы, кашпо.'
    podelka_3 = 'Подделки из втулок и яичных лотков: развивающие игрушки, аппликации, открытки, шляпка для куклы, объемные портреты животных.'
    podelki = [podelka_1, podelka_2, podelka_3]

    info_1 = (''' Сортировка отходов — это важный шаг к сохранению окружающей среды. 
 Правильное выбрасывание мусора помогает переработать материалы и уменьшить количество отходов, попадающих на свалки. 

 Вот несколько простых правил
 1. Разделяйте отходы: Используйте разные контейнеры для бумаги, пластика, стекла и органических отходов.
 2. Мойте контейнеры: Перед утилизацией пластиковых и стеклянных бутылок ополаскивайте их, чтобы избежать загрязнения.
 3. Не смешивайте: Не выбрасывайте в один контейнер перерабатываемые и неперерабатываемые отходы.
 4. Утилизируйте опасные материалы отдельно: Батарейки, лампы и химикаты требуют специальной утилизации.
 5. Сокращайте количество отходов: Переходите на многоразовые пакеты, бутылки и контейнеры.
 Соблюдая эти простые правила, вы можете внести свой вклад в защиту планеты!''')

    info_2 = (''' Вот немного примеров времени разложения различных бытовых предметов:

 1. Бумажные полотенца: 2-4 недели.
 2. Стеклянные бутылки: 1 миллион лет (не разлагаются, но могут перерабатываться).
 3. Пластиковые бутылки: 450 лет.
 4. Металлические банки: 200-500 лет.
 5. Обычные пластиковые пакеты: 10-1000 лет.
 6. Картонные коробки: 2-3 месяца.
 7. Органические отходы (например, пищевые остатки): 1-3 месяца.

 Эти сроки могут варьироваться в зависимости от условий окружающей среды.
 Правильная утилизация и переработка помогут сократить негативное воздействие на природу! ''')
    informations = [info_1, info_2]

    podelka = random.choice(podelki)
    info = random.choice(informations)
    if len(eco) >= 2:
        if eco[1] == 'заработок':
            bot.reply_to(message, f''' Хотите узнать, как зарабатывать на экологии? Вот интересный варианты для поделок из ненужных материалов:
 {podelka}
 После того, как вы сделаете подделки, вы можете их выставить на сайте Avito (или на любом другом сайте где можно продавать что-то) с небольшой ценой, примерно 300 рублей/3 доллара''')
           
        elif eco[1] == 'информация':
            bot.reply_to(message, f'Может быть, вас заинтересует это: {info}')
    
    else:
        bot.reply_to(message, ''' Какая у вас цель?
 Если вы хотите узнать, как заработать на боте, допишите к команде "заработок".
 Если хотите узнать что-то новое, введите "информация"''')

bot.remove_webhook()
bot.polling(none_stop=True)
