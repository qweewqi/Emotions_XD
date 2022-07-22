from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from stuff import *
import  json

eme = Client("emotion",
      api_id = app_id, api_hash = app_hash,
      bot_token = token)


@eme.on_message(filters.private & filters.command("start") or filters.regex("🤖 Start"))
async def start(client, message):
    await message.reply_text(start_msg0, reply_markup = keybd)
    await message.reply_sticker(stk5)

@eme.on_message(filters.private & filters.command("help") or filters.regex("⁉️ Help"))
async def help(client, message):
    name = getname(client,message)
    await message.reply_text(help_text%name, reply_markup = keybd, disable_web_page_preview=True)
    await message.reply_sticker(stk8)

@eme.on_message(filters.private & filters.regex("thanks") or filters.regex("Thanks") or filters.regex("thank you") or filters.regex("Thank you") or filters.regex("😊 Thanks"))
async def thank(client, message):
    ran = randint(0, 1)
    if ran == 1:
        await message.reply_text("**You are welcome**", reply_markup = keybd)
    else:
        await message.reply_text("**it's my duty**", reply_markup = keybd)

    await message.reply_sticker(stk7)


# This func used to get user's name if he have one
def getname(client,message):
    user_id = message.from_user.id
    username = "@" + message.from_user.username
    frname = message.from_user.first_name
    lasname = message.from_user.last_name
    name = ""

    if username != "None":
       name = username
    elif frname != "None":
       name = frname
    elif username == "None" and frname == "None":
       name = str(user_id)
    return name


@eme.on_message(filters.private & filters.command("feelings") or filters.regex("🔴 Feelings")
async def feelings(client, message):
    await message.reply_photo(circle, caption=msg0, reply_markup = colors)

@eme.on_callback_query()
async def calls(client, message):
    data = message.data
    print(data)
    inline=False
    if message.inline_message_id: inline=True

eme.run()
