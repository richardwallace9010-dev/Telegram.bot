from telegram.ext import Updater, CommandHandler

8200356722:AAGNgAbK4wxMnY6o6rim6ldJWgjLhTjUSbk
# your token from bot father 
TOKEN = 8200356722:AAGNgAbK4wxMnY6o6rim6ldJWgjLhTjUSbk

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
