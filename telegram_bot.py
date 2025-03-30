from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Функция, реагирующая на команду /start"""
    await update.message.reply_text(f"Привет, {update.effective_user.first_name}! Это Telegram Simulator!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Функция для повторения сообщения"""
    await update.message.reply_text(update.message.text)

def main():
    # Укажите ваш токен API
    TOKEN = "7903766986:AAGvC8PfAvK1UMfQMHVO8tBcgiQeTDsDNZY"
    
    # Настройка приложения
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Обработка команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("echo", echo))
    
    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
