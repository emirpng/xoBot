from pyrogram import Client, filters
from pyrogram.raw.types.messages import BotResults
from pyrogram.types import Message

import config

app = Client(
    config.SESSION_NAME,
    config.API_ID,
    config.API_HASH
)


@app.on_message(filters.me & filters.command('send', ['!', '/']))
async def send_game(_, message: Message):
    which_one = 'X'
    if len(cmds := message.command) > 1 and cmds[1].lower() in ['o', '2']:
        which_one = 'O'

    index = 0 if which_one == 'X' else 1

    try:
        results: BotResults = await app.get_inline_bot_results(config.XO_BOT)
        await app.send_inline_bot_result(
            message.chat.id,
            results.query_id,
            results.results[index].id,
            reply_to_message_id=message.id
        )
    except TimeoutError:
        await message.edit_text('Timeout error')


if __name__ == '__main__':
    print("Running XO BOT")
    app.run()
