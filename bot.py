import os
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telebot import TeleBot
from dotenv import load_dotenv
from Publication import *

load_dotenv()

API_KEY = os.getenv('API_KEY')
bot = TeleBot(API_KEY)

button1 = KeyboardButton('Clothes👕')
button2 = KeyboardButton('Publish📤')

markup = ReplyKeyboardMarkup(
    row_width=1, one_time_keyboard=True, resize_keyboard=True)
markup.add(button1, button2)

jacket = InlineKeyboardButton('Jacket🧥', callback_data='jacket')
t_shirt = InlineKeyboardButton('Shirt👕', callback_data='t_shirt')
pants = InlineKeyboardButton('Pants👖', callback_data='pants')
dress = InlineKeyboardButton('Dress👗', callback_data='dress')
snickers = InlineKeyboardButton(
    'Snickers👟', callback_data='snickers')
high_heel = InlineKeyboardButton(
    'High-heel👠', callback_data='high_heel')
coat = InlineKeyboardButton('Coat🥼', callback_data='coat')
skirt = InlineKeyboardButton('Skirt👗', callback_data='skirt')

types_list = []

inlineMarkup = InlineKeyboardMarkup(row_width=2)
inlineMarkup.add(jacket, t_shirt, pants, dress,
                 snickers, high_heel, skirt, coat)
types_list.extend([jacket, t_shirt, pants, dress,
                  snickers, high_heel, skirt, coat])


new = InlineKeyboardButton('New', callback_data='new')
second_hand = InlineKeyboardButton(
    'Second Hand', callback_data='second_hand')
stateMarkup = InlineKeyboardMarkup(row_width=2)
stateMarkup.add(new, second_hand)


male = InlineKeyboardButton('Male', callback_data='male')
female = InlineKeyboardButton('Female', callback_data='female')
sexMarkup = InlineKeyboardMarkup(row_width=2)
sexMarkup.add(male, female)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Hello, ' +
                     message.from_user.first_name, reply_markup=markup)
    bot.send_message(message.chat.id, 'Choose One: ',
                     reply_markup=inlineMarkup)


@bot.message_handler(regexp='^Clothes👕$')
def clothes(message):
    for object in all_objects:
        bot.send_message(message.chat.id, object)


@bot.message_handler(regexp='^Publish📤$')
def publish(message):
    bot.send_message(message.chat.id, 'Enter name: ')


@bot.callback_query_handler(func=lambda m: True)
def call_query_type(call):
    if call.data in list:
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


@bot.message_handler(regex='^New$|^Second Hand$')
def get_sex(message):
    state = message.text
    bot.send_message(message.chat.id, 'Choose One: ', reply_markup=sexMarkup)


@bot.message_handler(regex='^Male$|^Female$')
def get_photo(message):
    sex = message.text
    bot.send_message(message.chat.id, 'Send Photo: ')


bot.polling()
