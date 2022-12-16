""" inline section butto """
from config import GROUP_SUPPORT , UPDATES_CHANNEL , OWNER_NAME
from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="▢", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="II", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▷", callback_data=f'cbresume | {user_id}'),
      InlineKeyboardButton(text="⦿", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="⦾", callback_data=f'cbunmute | {user_id}'),
    ],
   [
      InlineKeyboardButton(
        "🦋 ʟᴏᴠᴇʟʏ 🦋", url="tg://settings"
      ),
      InlineKeyboardButton(
          "🦋 ʟᴏɢɪ 🦋", url=f"https://t.me/cl_me_logesh"
        )
    ],
    [
      InlineKeyboardButton(text="🦋 ᴄʟᴏꜱᴇ 🦋", callback_data='cls'),
    ]    


  ]
  return buttons


def menu_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="▢", callback_data=f'cbstop | {user_id}'),
      InlineKeyboardButton(text="II", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▷", callback_data=f'cbresume | {user_id}'),
      InlineKeyboardButton(text="⦿", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="⦾", callback_data=f'cbunmute | {user_id}'),
    ],
   [
      InlineKeyboardButton(
        "🦋 ʟᴏᴠᴇʟʏ 🦋", url="tg://settings"
      ),
      InlineKeyboardButton(
          "🦋 ʟᴏɢɪ 🦋", url=f"https://t.me/cl_me_logesh"
        )
    ],
    [
      InlineKeyboardButton(text="🦋 ᴄʟᴏꜱᴇ 🦋", callback_data='cls'),
    ]    


  ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🦋 ᴄʟᴏꜱᴇ 🦋", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="cbmenu"
      )
    ]
  ]
)
