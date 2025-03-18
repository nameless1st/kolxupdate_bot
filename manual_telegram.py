from telegram.ext import Application, MessageHandler, filters
from pytz import timezone

TELEGRAM_TOKEN = "7598743933:AAEmE0WWzxQrdTyCUVa8ruTrkM-RG6Rp8Wg"
TELEGRAM_CHAT_ID = "-1002397861291"

async def forward_message(update, context):
    user_message = update.message.text
    await context.bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=user_message)
    print(f"Forwarded message to {TELEGRAM_CHAT_ID}: {user_message}")

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.job_queue.scheduler.timezone = timezone("UTC")  # Explicitly set UTC
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
    print("Bot is running... Send messages to @KOLXupdate_bot!")
    application.run_polling()

if __name__ == "__main__":
    main()
