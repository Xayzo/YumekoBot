import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Yumeko.events import register as MEMEK
from Yumeko import telethn as tbot

PHOTO = "https://telegra.ph/file/460d20a0ec51ef80de06e.jpg"

@MEMEK(pattern=("/musichelp"))
async def awake(event):
  tai = event.sender.first_name
  YUMEKO = "** ──「 Member Commands 」── ** \n\n"
  YUMEKO += "• /rplay **(song title) — To Play the song you requested via YouTube** \n"
  YUMEKO += "• /vplay ** (song/video title) – To Play the video you requested via Youtube** \n"
  YUMEKO += "• /playlist - **show the list song in queue** \n"
  YUMEKO += "•/lyric - ** (song name) lyrics scrapper** \n\n"
  YUMEKO += "** ──「 Admin Commands 」── ** \n\n"
  YUMEKO += "• /pause - **To Pause Song playback** \n"
  YUMEKO += "• /vpause - **To Pause Video playback** \n"
  YUMEKO += "• /resume - **To resume playback of the paused Song** \n"
  YUMEKO += "• /vresume - **To resume playback of the paused Video** \n"
  YUMEKO += "• /skip - **To Skip playback of the Song to the next Song** \n"
  YUMEKO += "• /skip - **To Skip playback of the Video to the next Video** \n"
  YUMEKO += "• /end - **To Stop Song playback** \n"
  YUMEKO += "• /vend - **To Stop Video playback** \n"
  YUMEKO += "• /settings - **open the player settings panel** \n"
  YUMEKO += "• /reload - **To Refresh admin list** \n"

  BUTTON = [[Button.url("☎️ Support", "https://t.me/DionSupport"), Button.url("📡 Updates", "https://t.me/DionProjects")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
