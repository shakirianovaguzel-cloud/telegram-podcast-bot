import os
import telebot


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID", "0"))

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")

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
    bot.forward_message(ADMIN_CHAT_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Рәхмәт! Фикерең безнең өчен бик кадерле 🙌")

bot.polling(none_stop=True)
