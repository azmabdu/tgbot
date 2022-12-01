import os
import telebot
from dotenv import load_dotenv
from Publication import *

load_dotenv()

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

button1 = telebot.types.KeyboardButton('Clothes👕')
button2 = telebot.types.KeyboardButton('Publish📤')

markup = telebot.types.ReplyKeyboardMarkup(
    row_width=1, one_time_keyboard=True, resize_keyboard=True)
markup.add(button1, button2)

jacket = telebot.types.InlineKeyboardButton('Jacket🧥', callback_data='jacket')
t_shirt = telebot.types.InlineKeyboardButton('Shirt👕', callback_data='t_shirt')
pants = telebot.types.InlineKeyboardButton('Pants👖', callback_data='pants')
dress = telebot.types.InlineKeyboardButton('Dress👗', callback_data='dress')
snickers = telebot.types.InlineKeyboardButton(
    'Snickers👟', callback_data='snickers')
high_heel = telebot.types.InlineKeyboardButton(
    'High-heel👠', callback_data='high_heel')
coat = telebot.types.InlineKeyboardButton('Coat🥼', callback_data='coat')
skirt = telebot.types.InlineKeyboardButton('Skirt👗', callback_data='skirt')

types_list = []

inlineMarkup = telebot.types.InlineKeyboardMarkup(
    row_width=2)
inlineMarkup.add(jacket, t_shirt, pants, dress,
                 snickers, high_heel, skirt, coat)
types_list.extend([jacket, t_shirt, pants, dress,
                  snickers, high_heel, skirt, coat])


new = telebot.types.InlineKeyboardButton('New', callback_data='new')
second_hand = telebot.types.InlineKeyboardButton(
    'Second Hand', callback_data='second_hand')
stateMarkup = telebot.types.InlineKeyboardMarkup(row_width=2)
stateMarkup.add(new, second_hand)


male = telebot.types.InlineKeyboardButton('Male', callback_data='male')
female = telebot.types.InlineKeyboardButton('Female', callback_data='female')
sexMarkup = telebot.types.InlineKeyboardMarkup(row_width=2)
sexMarkup.add(male, female)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Choose One: ', reply_markup=markup)


@bot.message_handler(regexp='^Clothes👕$')
def clothes(message):
    for object in all_objects:
        bot.send_message(message.chat.id, object)


@bot.message_handler(regexp='^Publish📤$')
def publish(message):
    bot.send_message(message.chat.id, 'Enter name: ')


@bot.callback_query_handler(func=lambda m: True)
def call_query_type(call):
    if call.data in types_list:
        type = call.data
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id, text='Enter Size: ', reply_markup=None)


@bot.message_handler(regexp='^[0-9]*$')
def get_size(message):
    size = message.text
    bot.send_message(message.chat.id, 'Choose State: ',
                     reply_markup=stateMarkup)


@bot.message_handler(regexp='^.+$')
def get_name(message):
    name = message.text
    bot.send_message(message.chat.id, 'Choose Type: ',
                     reply_markup=inlineMarkup)


bot.polling()
