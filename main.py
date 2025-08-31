from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_TOKEN = "8369273063:AAFCq1SpIqNSlcnEmYeu8pkLeOPbkEjH1pY"

def clean(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    # Default 10 messages clean
    count = 10  
    
    for i in range(count):
        try:
            context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id - i)
        except:
            pass
    
    update.message.reply_text(f"✅ {count} messages deleted!")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("clean", clean))

updater.start_polling()
updater.idle()
