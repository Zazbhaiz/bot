from typing import Union

from pyrogram.types import InlineKeyboardButton, CallbackQuery

import config
from MARKX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="» Aᴅᴅ ᴍᴇ «",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❍ʜᴇʟᴩ❍",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❍sᴇᴛᴛɪɴɢs❍", callback_data="settings_helper"
            ),
        ],
        [
            
            InlineKeyboardButton(text="❍ᴄʜᴀɴɴᴇʟ❍", url=f"{config.SUPPORT_CHANNEL}"),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="» Aᴅᴅ ᴍᴇ  «",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍Music❍", callback_data="settings_back_helper"
            ),

             InlineKeyboardButton(
                text="❍Management❍", callback_data="settings_back_helper"
            ),
            
        ],
        [ 
            InlineKeyboardButton(text="❍ᴄʜᴀɴɴᴇʟ❍", url=f"{config.SUPPORT_CHANNEL}"),
            
        ],
        
     ]
    return buttons

#Callback



