import itertools
from typing import Optional, List

from pyrogram import Client
from pyrogram.raw.types import Updates
from pyrogram.types import Message, InlineKeyboardButton


async def parse_message(client: Client, updates: Updates) -> Message:
    message = await Message._parse(
        client,
        updates.updates[-1].message,
        {user.id: user for user in updates.users},
        {chat.id: chat for chat in updates.chats},
    )
    return message


def process_button(button: InlineKeyboardButton) -> str:
    d = {
        '⬜': ' ',
        '❌': 'X',
        '⭕': 'O'
    }
    return d.get(button.text, ' ')


def extract_game(message: Message) -> Optional[List[str]]:
    buttons = list(
        itertools.chain(
            *message.reply_markup.inline_keyboard
        )
    )

    if len(buttons) != 9:
        return None

    game = list(
        map(
            process_button, buttons
        )
    )
    return game
