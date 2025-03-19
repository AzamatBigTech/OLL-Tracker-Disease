# Обработчики команд (src/handlers.py)
def setup_handlers(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Добро пожаловать! Я бот для отслеживания ALL.")

    @bot.message_handler(commands=['help'])
    def send_help(message):
        bot.reply_to(message, "Список доступных команд: /start, /help")
