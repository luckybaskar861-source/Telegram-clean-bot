from pyrogram import Client, filters

API_ID = 25362995
API_HASH = "1bd4bac9f262c3437d2d425a863b1f63"
BOT_TOKEN = "8369273063:AAFCq1SpIqNSlcnEmYeu8pkLeOPbkEjH1pY"

app = Client(
    "cleaner-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("👋 Bot running successfully 24/7!")

@app.on_message(filters.command("clean") & filters.reply)
async def clean(_, message):
    try:
        await message.reply_to_message.delete()
        await message.delete()
    except:
        await message.reply("⚠️ Can't delete this message!")

app.run()
