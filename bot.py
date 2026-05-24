from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "PASTE_NEW_BOT_TOKEN"

GROUP_ID = -1003883248474

CAMERA_TOPIC = 3
SNAPCHAT_TOPIC = 4
VIDEOS_TOPIC = 5
DOCUMENTS_TOPIC = 6
PRIVATE_TOPIC = 7


async def handle_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    try:

        # Photos
        if message.photo:
            await context.bot.copy_message(
                chat_id=GROUP_ID,
                from_chat_id=message.chat_id,
                message_id=message.message_id,
                message_thread_id=CAMERA_TOPIC
            )

        # Videos
        elif message.video:
            await context.bot.copy_message(
                chat_id=GROUP_ID,
                from_chat_id=message.chat_id,
                message_id=message.message_id,
                message_thread_id=VIDEOS_TOPIC
            )

        # Documents
        elif message.document:
            await context.bot.copy_message(
                chat_id=GROUP_ID,
                from_chat_id=message.chat_id,
                message_id=message.message_id,
                message_thread_id=DOCUMENTS_TOPIC
            )

    except Exception as e:
        print(e)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.PHOTO | filters.VIDEO | filters.Document.ALL,
        handle_media
    )
)

print("Bot is running...")
app.run_polling()