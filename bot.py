from datetime import datetime
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
markup.add(button2, button1)

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

list = []

inlineMarkup = InlineKeyboardMarkup(row_width=2)
inlineMarkup.add(jacket, t_shirt, pants, dress,
                 snickers, high_heel, skirt, coat)
list.extend([jacket.callback_data, t_shirt.callback_data, pants.callback_data, dress.callback_data,
             snickers.callback_data, high_heel.callback_data, skirt.callback_data, coat.callback_data])


new = InlineKeyboardButton('New', callback_data='new')
second_hand = InlineKeyboardButton(
    'Second Hand', callback_data='second_hand')
stateMarkup = InlineKeyboardMarkup(row_width=2)
stateMarkup.add(new, second_hand)


male = InlineKeyboardButton('Male', callback_data='male')
female = InlineKeyboardButton('Female', callback_data='female')
genderMarkup = InlineKeyboardMarkup(row_width=2)
genderMarkup.add(male, female)


@bot.message_handler(regexp='^Publish📤$')
def publish(message):
    global obj
    obj = Product()
    obj.name = message.from_user.first_name

    bot.send_message(message.chat.id, 'Choose One 👀: ',
                     reply_markup=inlineMarkup)


@bot.message_handler(commands=['start'])
def hello(message):
    print(message.from_user.first_name, '-', message.from_user.username)
    bot.send_message(message.chat.id, 'Hello, ' +
                     message.from_user.first_name, reply_markup=markup)


@bot.message_handler(regexp='^Clothes👕$')
def clothes(message):
    print(message.from_user.first_name, '-', message.from_user.username)
    if len(all_objects) != 0:
        print(*all_objects)
        try:
            for object in all_objects:
                if object.photo_url:
                    img = object.photo_url
                else:
                    img = 'recources/no-photo.jpg'
                bot.send_photo(message.chat.id, photo=open(img, 'rb'),
                               caption=f'Name 👤: {object.name}\nType 👔: {object.type}\nSize📎: {object.size}\nGender 🙋🏻: {object.gender}\nState ⭐️: {object.state}')
        except Exception:
            bot.send_message(message.chat.id, Exception, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'No Products Yet',
                         reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def call_query_type(call):
    if call.data in list:
        obj.type = call.data
        bot.send_message(chat_id=call.message.chat.id, text='Enter Size: ')

    elif call.data in ['new', 'second_hand']:
        state = call.data
        obj.state = state
        bot.send_message(chat_id=call.message.chat.id,
                         text='Choose Gender: ', reply_markup=genderMarkup)

    elif call.data in ['male', 'female']:
        gender = call.data
        obj.gender = gender
        bot.send_message(chat_id=call.message.chat.id, text='🌄 Send Photo: ')


@bot.message_handler(regexp='^[0-9]*$')
def get_size(message):
    size = message.text
    obj.size = size
    bot.send_message(message.chat.id, 'Choose State 👀: ',
                     reply_markup=stateMarkup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    time = datetime.now().strftime("%H-%M-%S")
    with open(f"recources/image-{time}.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
        photo_url = f"recources/image-{time}.jpg"
        obj.photo_url = photo_url
    bot.send_message(message.chat.id, '✅ Done!')


bot.infinity_polling()
