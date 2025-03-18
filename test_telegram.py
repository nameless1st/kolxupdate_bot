from telegram.ext import Updater, MessageHandler, Filters

TELEGRAM_TOKEN = "7598743933:AAEmE0WWzxQrdTyCUVa8ruTrkM-RG6Rp8Wg"
TELEGRAM_CHAT_ID = "-1002397861291"  # t.me/kolx_ai chat ID

def forward_message(update, context):
    user_message = update.message.text
    context.bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=user_message)
    print(f"Forwarded message to {TELEGRAM_CHAT_ID}: {user_message}")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))
    updater.start_polling()
    print("Bot is running... Send messages to @KOLXupdate_bot!")
    updater.idle()

if __name__ == "__main__":
    main()
