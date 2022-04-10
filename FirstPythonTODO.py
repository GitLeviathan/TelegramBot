# Всякая обязательная хрень
import telebot
token = '5200547318:AAFdu_ZtAUuD-YTERH9cvFCQU10QsIVtgYY'
bot = telebot.TeleBot(token)

HELP = """
/help - показывает возможности
/add - добавляет задачу на какой-то день
/show - показывает, что уже записано"""

tasks = {}

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date]=[]
        tasks[date].append(task)

# Здороваемся
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Ку! Что записать?")

# Задаём функции
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    task_len=len(task)
    if task_len < 3:
        bot.send_message(message.chat.id, "Не, слишком коротко. Давай что-то посерьёзнее")
    else:
        add_todo(date, task)
        text = "Задача " + task + " добавлена на дату " + date
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[]" + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

# Просто нужно, чтобы стояло в конце
bot.polling(none_stop=True)