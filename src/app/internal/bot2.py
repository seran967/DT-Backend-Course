
#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
#updater = Updater(token='5292815147:AAHtRZbacBuVDCP8Y2S-lwhXgX7ugyKHRYc', use_context=True)
import telebot

bot = telebot.TeleBot("")

# Подключаем базу
import sqlite3

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()




def db_table_val(user_id: int, name: str, user_name: str, tel: str):
    cursor.execute('INSERT INTO for_bot (user_id, name, '
                   'user_name, tel) VALUES (?, ?, ?, ?)', (user_id, name, user_name, tel))
    conn.commit()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')

        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        tel_n = message.from_user.phone
        db_table_val(user_id=us_id, name=us_name + ' '+ us_sname, user_name=username, tel=tel_n)


bot.polling(none_stop=True)
