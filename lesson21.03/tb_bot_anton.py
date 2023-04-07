import telebot
from telebot import types

# bot = telebot.TeleBot("5808749828:AAHy1LWZJqmezvp_LAO46t-NbltTFcT9Ucc")
bot = telebot.TeleBot('6154066069:AAGwSP7Pdg4M8NqwWJA8lzsWXs38CKHtzFo')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привяу")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Привет, я бот-помощник", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Привяу':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Новости')
        btn2 = types.KeyboardButton('Расписание')
        btn3 = types.KeyboardButton('Курсы')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота

    elif message.text == "Какие новости?":
        bot.send_message(message.from_user.id, "Да нормально все, остальные новости по " + "[ссылке](https://levelp.ru/news/)", parse_mode="Markdown")
    elif message.text == "Какое расписание?":
        bot.send_message(message.from_user.id, "Расписание доступно по [ссылке](https://levelp.ru/courses/schedule/)", parse_mode="Markdown")
    elif message.text == "Какие есть курсы?":
        bot.send_message(message.from_user.id, "Список курсов находится по [ссылке](https://levelp.ru/courses/)", parse_mode="Markdown")

bot.polling(none_stop=True, interval=0)

