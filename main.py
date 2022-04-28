from pyrogram import Client

import config

app = Client(
    config.SESSION_NAME,
    config.API_ID,
    config.API_HASH
)

if __name__ == '__main__':
    print("Running XO BOT")
    app.run()
