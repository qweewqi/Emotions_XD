import os, datetime, sys, json
from pyrogram.types import ReplyKeyboardMarkup

token = os.getenv("token", "")
app_id = os.getenv("app_id", "")
app_hash = os.getenv("app_hash", "")

x = datetime.datetime.utcnow()
i = x + datetime.timedelta()
y = i.strftime("%Y-%m-%d")
print(y)
print("My PID is:", os.getpid())


if len(str(token)) < 5: print("please put your token in env"); sys.exit(1)

logGroup = -1001593847613

keybd = ReplyKeyboardMarkup([
     ['🤖 Start', '🔴 Feelings'],
     ['⁉️ Help', '😊 Thanks']], resize_keyboard=True)


stk0 = "CAADBAADrgcAAnILQFPgjUtxHDj-oQI"
stk1 = "CAADBAADlQoAAo8RQFOWkvFydBKJlwI"
stk2 = "CAADBAADSAsAAn_eOFPurvLfXO2hzAI"
stk3 = "CAADBAAD0QoAAkKSOFND8vqd0dBlhQI"
stk4 = "CAADBAADRgkAAhzwOFMQTCV2uQABp4wC"
stk5 = "CAADBAADHwoAAgTjOFPwcaIN8VE3uQI"
stk6 = "CAADBAAD2AgAAv1sOFOBvhMuUqdpVgI"
stk7 = "CAADBAAD_AkAAzI4U1zm0zS8ZmfzAg"
stk8 = "CAADBAADZQoAAvmvQFN_0Kq6nbL7IAI"
fthl = "CAACAgEAAxkBAAEDhMhhv1eWCc2bLbg8V5ZW2w7v5lVz0QAClQEAAjT0-UWjXL_zWuG_FiME"

start_msg0 = "Hi human,"
start_msg1 = "I can help generate Emotion circles and save you precious time, **Start by clicking Feelings button** or check out the Help"

help_text = """ Hi %s,

Welcome to **@Emotions_XD_bot** 👋

This bot was made to help people generate
Emotion circles to express thier feelings
that can help other people to easily understand
thier Emotion state.

Start by clicking the **Feelings** Button

You will get a keyboard with colors

Look at the circle and find what Emotion you want

Click the **color** that your Emotion belongs to

Next Forward the circle to your friend Or

Long click the photo and **Save to Gallery**

Cheers"""


msg0 = "Hello, **Please Select a Color** use the circle as a reference"
msg1 = "Please Select, **How you feel right now**"
msg2 = "Select a Color **If you want to add another Highlight**,\nElse click done Then forward the photo to your friend"

logger1 = "**New user!!**"
logger2 = "**User Says**:\n\n"
logger3 = "**User Wants To report** \n\n"
logger4 = "**User is Happy** says thanks "
logger5 = "**Inline Request**\n\n"
