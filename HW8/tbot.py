# 6154066069:AAGwSP7Pdg4M8NqwWJA8lzsWXs38CKHtzFo

import  telebot
from telebot import types
bot = telebot.TeleBot('6154066069:AAGwSP7Pdg4M8NqwWJA8lzsWXs38CKHtzFo')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет, я умею считать, начнем /input")
@bot.message_handler(commands=['input'])
def first_input(message):
    bot.send_message(message.chat.id, "Введите пожалуйста значение ")
    bot.register_next_step_handler(message, second_input)

def second_input(message):
    first_number = int(message.text)
    bot.send_message(message.chat.id, "Введите пожалуйста знак ")
    bot.register_next_step_handler(message, third_input,first_number)


def third_input(message,first_number):
    first_number=first_number
    sign1 = message.text
    bot.send_message(message.chat.id, "Введите пожалуйста значение ")
    bot.register_next_step_handler(message, calculator, first_number,sign1)

def calculator(message,first_number,sign1):
    second_number = int(message.text)
    if sign1 == '+':
        resultt = first_number + second_number
    elif sign1 == '-':
        resultt = first_number - second_number
    elif sign1 == '*':
        resultt = first_number * second_number
    elif sign1 == '/':
        if second_number ==0:
            resultt = "На 0 делить нелзя"
        else:
            resultt = first_number / second_number
    bot.send_message(message.chat.id, f"Результат вычисления {resultt}")

bot.infinity_polling()



