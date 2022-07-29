from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultPhoto, InputMediaPhoto
from stuff import *
from random import randint
from io import BytesIO
from PIL import Image
import json

eme = Client("emotion",
      api_id = app_id, api_hash = app_hash,
      bot_token = token)

# The reason why we do this on startup instead of using constants
# is because later we can add/modfiy json and reload the bot and new
# changes will be applied adding new feelings or even changing the wheel

# load json
feel = json.loads(open("emotions.json",'r').read())
colors = feel.keys()

# Generate colors keyboard on startup
ckeyboard = []

for i in colors:
    c = f"{i}|wfs"
    ckeyboard.append([InlineKeyboardButton(i, callback_data=c)])
t = []
for i in ckeyboard: t.append(i[0])
ckey = [[i1, i2] for i1, i2 in zip(t[::2], t[1::2])]
if len(ckey)%2 != 0: ckey.append(ckeyboard[-1])
ckey.append([InlineKeyboardButton("❌Cancel", callback_data="del")])
finalckey = list(ckey)
finalckey.append([InlineKeyboardButton("✔️Done", callback_data="done")])
finalckey = InlineKeyboardMarkup(finalckey)
ckey = InlineKeyboardMarkup(ckey)

# Generate feelings keyboard on startup
fkey = {}
for c in colors:
    feels = feel[c] # get emotions by color
    key = []
    for i in feels:
        index = feel[c][i]['index']
        key.append([InlineKeyboardButton(i, callback_data=f"{index}|mkh")])

    t = []
    for i in key: t.append(i[0])
    fkeys = [[i1, i2, i3] for i1, i2, i3 in zip(t[::3], t[1::3], t[2::3])]
    if len(key)%3 != 0:
       missing = len(key)%3 # possibly 2 or 1
       fkeys.append([key[-2][0], key[-1][0]] if missing == 2 else key[-1])

    fkeys.append([InlineKeyboardButton("⋘ Back ⋙", callback_data="back"), InlineKeyboardButton("Cancel", callback_data="del")])
    fkey[c] = InlineKeyboardMarkup(fkeys)

# Indexing feelings on startup
findex = {}
for c in colors:
    feels = feel[c] # get emotions by color
    for i in feels:
        index = feel[c][i]['index']
        pos   = feel[c][i]['pos']
        color = feel[c][i]['color']
        findex[index] = {'pos': pos, 'color': color}

tasks = {}

@eme.on_message(filters.private & filters.command("start") | filters.regex("🤖 Start"))
async def start(client, message):
    await message.reply_text(start_msg0, reply_markup = keybd)
    await message.reply_sticker(stk5)
    await message.reply_text(start_msg1)
    await logger(client, message, logger1)

@eme.on_message(filters.private & filters.command("help") | filters.regex("⁉️ Help"))
async def help(client, message):
    name = getname(client,message)
    await message.reply_text(help_text%name, reply_markup = keybd, disable_web_page_preview=True)
    await message.reply_sticker(stk8)

@eme.on_message(filters.private & filters.regex("thanks") | filters.regex("Thanks") | filters.regex("thank you") | filters.regex("Thank you") | filters.regex("😊 Thanks"))
async def thank(client, message):
    ran = randint(0, 1)
    msg = "**You are welcome**" if ran == 1 else "**it's my duty**"
    await message.reply_text(msg, reply_markup = keybd)
    await message.reply_sticker(stk7)
    await logger(client, message, logger4)


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


@eme.on_message(filters.private & filters.command("feelings") | filters.regex("🔴 Feelings"))
async def feelings(client, message):
    await reply_photo(client, message, 'assets/feelswheel.jpg', msg0, ckey)
    await logger(client, message, "New request!")

async def highlight(client,message,index):
    try:
       circle = Image.open(tasks[message.from_user.id])
    except KeyError: circle = Image.open("assets/feelswheel.jpg")
    color = findex[index]['color']
    pos = findex[index]['pos']
    highlight = Image.open("assets/" + color + ".png")
    circle.paste(highlight, (round(pos[0])-10,round(pos[1])-10), highlight)
    finalc = BytesIO()
    circle.save(finalc, quality=100, format="jpeg")
    finalc.name = "feel.jpg"
    tasks[message.from_user.id] = finalc
    await delete(client, message)
    await reply_photo(client, message, finalc, msg2, finalckey)

@eme.on_callback_query()
async def calls(client, message):
    data = message.data
    print(data)
    inline=False
    if message.inline_message_id: inline=True

    if "del" in data:
       await message.answer()
       await delete(client, message)

    elif "back" in data:
       await message.answer()
       try:
           circle = tasks[message.from_user.id]
           msg = msg2; keyb = finalckey
       except KeyError: msg = msg0; keyb = ckey
       await edit(client, message, msg, keyb)

    elif "done" in data:
       await message.answer()
       await edit(client, message, None, None)
       tasks.pop(message.from_user.id)

    elif "wfs" in data: # wfs = want feelings
       color, _ = data.split("|")
       await message.answer()
       await edit(client, message, msg1, fkey[color])

    elif "mkh" in data: # mkh = make highlight
       index, _ = data.split("|")
       await message.answer()
       await highlight(client,message,int(index))

@eme.on_inline_query()
async def inlines(client, message):
    print("new inline query", message.query)
    answer = [
        InlineQueryResultPhoto(
            title="Feelings Wheel",
            description=inline_msg,
            photo_url="https://telegra.ph/file/3bf1f29a14a6546b76077.jpg",
            caption=msg0,
            reply_markup=ckey)
        ]
    await message.answer(answer)
    await logger(client, message, logger5)

# just a looging function
async def logger(c, m, msg, text=""):
    if not logGroup: return
    client = c; message = m;
    ms = msg + text + f"\n\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} {message.from_user.id} {message.from_user.mention}"
    await client.send_message(logGroup, ms, disable_web_page_preview=True)


### Message reply tools ###

async def reply_photo(c, m, p, t, k):
    inline = is_inline(m)
    if inline:
       # Because of bug in pyrogram
       # BytesIO object cant be used as input
       # so we save photo from memory to disk
       # then upload from disk
#       with open(f"{m.from_user.id}.jpg", 'wb') as f: f.write(p.getbuffer())
#       media = InputMediaPhoto(f"{m.from_user.id}.jpg")
#     Edit i'm using a pyrogram fork that temp fixes the problem
       media = InputMediaPhoto(p)
       await c.edit_inline_media(m.inline_message_id, media)
       await c.edit_inline_caption(m.inline_message_id, caption=t, reply_markup=k)
#       try: os.remove(f"{m.from_user.id}.jpg")
#       except: pass
    else:
       try: m = m.message
       except AttributeError: m = m
       await m.reply_photo(p, caption=t, reply_markup=k)

async def edit(c, m, t, k):
    inline = is_inline(m)
    if inline:
       await c.edit_inline_caption(m.inline_message_id, t, reply_markup=k)
    else: await m.message.edit_text(t, reply_markup=k)

async def delete(c, m):
    inline = is_inline(m)
    if inline:
       await c.edit_inline_caption(m.inline_message_id, None, reply_markup=None)
    else: await m.message.delete()

def is_inline(m):
    try:
       id = m.inline_message_id
       return True if id else False
    except Exception as e:
       return False

eme.run()
