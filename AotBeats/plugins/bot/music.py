from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup
from AootBeats import app
from config import BANNED_USERS
from AootBeats.About.buttons import BUTTONS
from AootBeats.About.abouttext import Helper  # Correct source with HELP

@app.on_callback_query(filters.regex("MUSIC_CP") & ~BANNED_USERS)
async def about_callback(client, CallbackQuery):
    await CallbackQuery.edit_message_text(
        Helper.HELP_ABOUT,
        reply_markup=InlineKeyboardMarkup(BUTTONS.ABUTTON)
    )
