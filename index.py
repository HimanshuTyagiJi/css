import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")  # Render me environment variable set karna hoga
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "🔥 Welcome to *AllCodeHub* 🚀\n\n"
        "Yahan tumhe milega: step-by-step programming solutions, demos aur projects!",
        parse_mode="Markdown"
    )

bot.polling()
