from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ✅ Paste your bot token here
TOKEN = "8200356722:AAGNqAbk4wxMnY6o6rim61dJWjghLtJUSbk"

# Example command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 🎉 Your bot is working on Render!")

# Main function
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
