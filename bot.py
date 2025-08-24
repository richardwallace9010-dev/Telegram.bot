import os
# Get your bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello 👋! Your bot is running successfully.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    bot.polling()
from telegram.ext import Updater, CommandHandler

#BotFather8200356722:AAGNgAbK4wxMnY6o6rim6ldJWgjLhTjUSbk
TOKEN = "YOUR_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("🚀 Hello! The bot is alive and running on Render.")

def help_command(update, context):
    update.message.reply_text("Here are the available commands:\n/start - check bot\n/help - this message")

def main():
    # Create the updater and dispatcher
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Start polling
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
