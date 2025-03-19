# Основной код бота (src/bot.py)
import logging
import telebot
from config import BOT_TOKEN
from handlers import setup_handlers

bot = telebot.TeleBot(BOT_TOKEN)
setup_handlers(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    bot.polling(none_stop=True)

# Работа с Supabase (src/database.py)
import supabase
from config import SUPABASE_URL, SUPABASE_KEY

supabase_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

def add_user(user_id, name):
    return supabase_client.table("users").insert({"id": user_id, "name": name}).execute()

def get_user(user_id):
    return supabase_client.table("users").select("*").eq("id", user_id).execute()