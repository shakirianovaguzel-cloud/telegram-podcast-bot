import telebot


TOKEN = "8598682318:AAHBOvA8MS6Bk8dVYFwwIthBE4Sm_syWvb0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
    message.chat.id,
    """Сәлам! Мин — "Бер генә сәгатькә" подкастының ярдәмчесе.
Бирегә син үз фикерләреңне, сорауларыңны яки кызыклы тарихларыңны җибәрә аласың. 
Әйдә, сөйләшик!"""
)

@bot.message_handler(content_types=['text', 'voice'])
def collect_message(message):
    ADMIN_CHAT_ID = 437136631

    bot.forward_message(ADMIN_CHAT_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Рәхмәт! Фикерең безнең өчен бик кадерле 🙌")

bot.polling(none_stop=True)






