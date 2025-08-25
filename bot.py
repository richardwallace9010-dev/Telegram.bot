from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Your bot token
TOKEN = "8200356722:AAGNqAbk4wxMnY6o6rim61dJWjghLtJUSbk"

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! 👋 I'm alive and working!")

# Main function
def main():
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))

    print("Bot is running... 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
