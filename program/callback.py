# Copyright (C) 2021 By logiMusicProject

from pyrogram import Client, filters
from driver.queues import QUEUE
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**

💡 **Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**


🛠 [🕊.⋆𝙆𝙄𝙉𝙂༒۝꧂](https://t.me/cl_me_logesh) **if you have any problem contact**

❔ **To know how to use this bot, please click on the » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ owner", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🕊.⋆𝙆𝙄𝙉𝙂༒۝꧂", url="https://t.me/cl_me_logesh"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **turn on the video chat first before start to play video.**
5.) **all the command list you can see on » 📚 Commands button, find it on start home, tap the » Go Back button below.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 Here is the Commands list:

» /play - play music on voice chat
» /stream - enter the radio link
» /vplay - play video on video chat
» /vstream - for m3u8/live link
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link
» /queue - show you the queue list (admin only)
» /pause - pause the stream (admin only)
» /resume - resume the stream (admin only)
» /skip - switch to next stream (admin only)
» /stop - stop the streaming (admin only)
» /userbotjoin - invite the userbot to join chat (admin only)
» /userbotleave - order userbot to leave from group (admin only)
» /reload - update the admin list (admin only)
» /rmw - clean raw files (sudo only)
» /rmd - clean downloaded files (sudo only)
» /leaveall - order userbot leave from all group (sudo only)

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **ꜱᴇᴛᴛɪɴɢꜱ ᴏꜰ** {chat}\n\nII : pause stream\n▷ : resume stream\n⦿ : mute userbot\n⦾ : unmute userbot\n▢ : stop stream\n **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :** [🇦 🇵 🇵 🇺 )](https://t.me/i_appu_you) ",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)

@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
