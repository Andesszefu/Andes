from telegram import Update, ChatMember, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Ustawienia bota
TOKEN = "7711787949:AAHf9hK8QR4fXVitY2joJjh3sHvrIl5GRUk"
GROUP_ID = -123456789  # ID grupy, gdzie bot działa
JOIN_LINK = "https://t.me/joinchat/szonyzometvv"  # Link zaproszeniowy

# Konfiguracja logowania
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Udostępnij do 2 grup", switch_inline_query="")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        "Cześć! Udostępnij naszą wiadomość na 2 grupach, aby dostać dostęp!",
        reply_markup=reply_markup
    )

def check_forward(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    forwards = context.user_data.get("forwards", 0) + 1
    context.user_data["forwards"] = forwards
    
    if forwards >= 2:
        update.message.reply_text(f"Gratulacje {user.first_name}, oto Twój link: {JOIN_LINK} 🔑")
    else:
        update.message.reply_text(
            f"{user.first_name}, udostępniono {forwards}/2 🔒 Udostępnij jeszcze raz, aby uzyskać dostęp!"
        )

def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f"Update {update} spowodował błąd {context.error}")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.forwarded, check_forward))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
