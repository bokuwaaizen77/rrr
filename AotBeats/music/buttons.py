from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 
import config
from AotBeats import app

class BUTTONS(object):
    ABUTTON = [
            [
                InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1",),
                InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2",),
                InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3",),
            ],
            [
                InlineKeyboardButton(text=_["H_B_4"], callback_data="help_callback hb4",),
                InlineKeyboardButton(text=_["H_B_5"], callback_data="help_callback hb5",),
                InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6",),
            ],
            [
                InlineKeyboardButton(text=_["H_B_7"], callback_data="help_callback hb7",),
                InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8",),
                InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback hb9",),
            ],
    ]
