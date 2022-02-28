import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register as MEMEK
from Yumeko import telethn as tbot

PHOTO = "https://telegra.ph/file/22d0cda0a988fff8e01ea.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  YUMEKO = "**Holla I'm [Royzu](https://t.me/RoyzuRobot) 👋🏻** \n\n"
  YUMEKO += "×**I'm Working Properly** \n\n"
  YUMEKO += f"×**Telethon Version : {tlhver}** \n\n"
  YUMEKO += f"×**Pyrogram Version : {pyrover}** \n\n"
  YUMEKO += "**Thanks For Using Me 🔥**"
  BUTTON = [[Button.url("My Owner", "https://t.me/RoyzuRobot"), Button.url("Updates", "https://t.me/DionProjects")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=YUMEKO,  buttons=BUTTON)
