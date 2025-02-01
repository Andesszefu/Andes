import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

# 🔑 Pobieranie tokena i ID grupy z Railway (Environment Variables)
TOKEN = os.getenv("7711787949:AAHf9hK8QR4fXVitY2joJjh3sHvrIl5GRUk")  # Twój token bota
GROUP_ID = os.getenv("-1002168288878")  # ID grupy
GROUP_LINK = "https://t.me/szonyzometvv"  # 🔹 Wstaw link do grupy!

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# 🔹 Słownik do przechowywania liczby udostępnień użytkowników
user_shares = {}

# 🔹 Wysyłanie wiadomości do grupy po starcie bota
async def send_group_message(_):
    keyboard = InlineKeyboardMarkup()
    share_button = InlineKeyboardButton("📤 Udostępnij do 2 grup", switch_inline_query="🔥 Dołącz do tej grupy!")
    keyboard.add(share_button)

    message_text = "🔓 Udostępnij ten post do 2 grup, aby uzyskać dostęp!"
    await bot.send_message(chat_id=GROUP_ID, text=message_text, reply_markup=keyboard)

# 🔹 Obsługa komendy /start (opcjonalnie dla użytkowników prywatnie)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Witaj! Udostępnij naszą grupę, aby uzyskać dostęp do filmikow za zaproszenia. 🔥")

# 🔹 Obsługa udostępnienia
@dp.inline_handler()
async def track_shares(query: types.InlineQuery):
    user_id = query.from_user.id

    # Zwiększamy licznik udostępnień użytkownika
    user_shares[user_id] = user_shares.get(user_id, 0) + 1

    # 🔹 Jeśli użytkownik udostępnił 2 razy, wysyłamy mu link do grupy na PRIV
    if user_shares[user_id] >= 2:
        await bot.send_message(user_id, f"✅ Gratulacje! Otrzymałeś dostęp do grupy: {GROUP_LINK}")

    await query.answer([])

# 🔹 Komenda do sprawdzenia ID grupy
@dp.message_handler(commands=['groupid'])
async def get_group_id(message: types.Message):
    await message.answer(f"ID tej grupy to: `{message.chat.id}`")

# 🔹 Uruchomienie Bota
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=send_group_message)
