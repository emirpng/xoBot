from typing import Dict, Tuple

from pyrogram import Client, filters
from pyrogram.raw.types import Updates
from pyrogram.raw.types.messages import BotResults
from pyrogram.types import Message

import config
from utils import parse_message, extract_game

app = Client(
    config.SESSION_NAME,
    config.API_ID,
    config.API_HASH
)

GAMES: Dict[str, Tuple[str, str]] = {}  # Key(chat_id|msg_id): me, opponent


@app.on_message(filters.me & filters.command('send', ['!', '/']))
async def send_game(_, message: Message):
    which_one = 'X'
    if len(cmds := message.command) > 1 and cmds[1].lower() in ['o', '2']:
        which_one = 'O'

    opponent = 'O' if which_one == 'X' else 'X'

    index = 0 if which_one == 'X' else 1

    try:
        results: BotResults = await app.get_inline_bot_results(config.XO_BOT)
        updates: Updates = await app.send_inline_bot_result(
            message.chat.id,
            results.query_id,
            results.results[index].id,
            reply_to_message_id=message.id
        )

        # Convert raw message to Message object
        parsed_msg = await parse_message(app, updates)

        key = f'{parsed_msg.chat.id}|{parsed_msg.id}'
        GAMES[key] = (which_one, opponent)

        await play_game(_, parsed_msg)
    except TimeoutError:
        await message.edit_text('Timeout error')


async def play_game(_, message: Message):
    key = f'{message.chat.id}|{message.id}'
    if key not in GAMES:
        return

    if message.via_bot.id == config.XO_BOT and message.reply_markup is not None:
        # Extract game from inline keyboard
        game = extract_game(message)
        print(game)


if __name__ == '__main__':
    print("Running XO BOT")
    app.run()
