import logging
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.types import Message, InlineQuery

# 🔑 Pobieranie tokena i ID grupy z Railway (Environment Variables)
TOKEN = os.getenv("BOT_TOKEN")  # Wprowadź token w ENV (np. Railway)
GROUP_ID = os.getenv("GROUP_ID")  # Wprowadź ID grupy w ENV
GROUP_LINK = "https://t.me/szonyzometvv"  # 🔹 Wstaw link do grupy!

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 🔹 Słownik do przechowywania liczby udostępnień użytkowników
user_shares = {}

# 🔹 Wysyłanie wiadomości do grupy po starcie bota
async def send_group_message():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📤 Udostępnij do 2 grup", switch_inline_query="🔥 Dołącz do tej grupy!")]
        ]
    )

    message_text = "🔓 Udostępnij ten post do 2 grup, aby uzyskać dostęp!"
    await bot.send_message(chat_id=GROUP_ID, text=message_text, reply_markup=keyboard)

# 🔹 Obsługa komendy /start (opcjonalnie dla użytkowników prywatnie)
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Witaj! Udostępnij naszą grupę, aby uzyskać dostęp do filmików za zaproszenia. 🔥")

# 🔹 Obsługa udostępnienia
@dp.inline_query()
async def track_shares(query: InlineQuery):
    user_id = query.from_user.id

    # Zwiększamy licznik udostępnień użytkownika
    user_shares[user_id] = user_shares.get(user_id, 0) + 1

    # 🔹 Jeśli użytkownik udostępnił 2 razy, wysyłamy mu link do grupy na PRIV
    if user_shares[user_id] >= 2:
        await bot.send_message(user_id, f"✅ Gratulacje! Otrzymałeś dostęp do grupy: {GROUP_LINK}")

    await query.answer([])

# 🔹 Komenda do sprawdzenia ID grupy
@dp.message(Command("groupid"))
async def get_group_id(message: Message):
    await message.answer(f"ID tej grupy to: `{message.chat.id}`")

# 🔹 Uruchomienie Bota
async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await send_group_message()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
