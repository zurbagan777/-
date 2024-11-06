#pip install pytelegrambotapi
import telebot
from requests.compat import builtin_str

list123=['Привет']
#Объект бота
bot = telebot.TeleBot('7912331129:AAEBrZAfsiWZPm-6zHyW7KZzKS0pOgRPsRI')

#обработка сообщений при помощи ф-ии-декоратора



@bot.message_handler(commands=['start'])
def send_welcome(message):

    chat_id =message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_support = telebot.types.KeyboardButton(text='ПАМАГИТЕ МНЕ')
    keyboard.add(button_support)
    bot.send_message(chat_id, "я еще новенький! Поможешь мне освоиться на новом месте", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.from_user.id, 'Я тебя не понимаю, напиши /help')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in list123:
        bot.send_message(message.from_user.id, 'Привет, чем я могу тебе помочь?')
    else:
        bot.send_message(message.from_user.id, 'Не понял вас')
#запуск бота
bot.polling(none_stop=True, interval=0)
