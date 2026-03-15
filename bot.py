from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, SOURCE_CHANNEL, TARGET_CHANNEL, LOG_CHANNEL

app = Client(
    "forward-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.chat(SOURCE_CHANNEL))
async def forward_files(client, message):

    try:

        # target channel
        await message.copy(
            chat_id=TARGET_CHANNEL
        )

        # log channel
        await message.copy(
            chat_id=LOG_CHANNEL
        )

        print("Message forwarded successfully")

    except Exception as e:

        print(f"Error: {e}")

app.run()
