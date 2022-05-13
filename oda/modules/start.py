from pyrogram import Client, filters
from oda import app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from oda.config import BOT_USERNAME, ASSUSERNAME, BOT_NAME
from oda.utils.filters import command


@app.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>┗┓ Hi {message.from_user.first_name} My Name is [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ┏┛\n
I'm Bot Music Group, Which Can Play Songs in Group Voice Chat In Easy Way
I Have Many Practical Features Like:
┏━━━━━━━━━━━━━━
┣• Play music.
┣• Download Songs.
┣• Search for the song you want to play or download.
┗━━━━━━━━━━━━━━
Type » /help « To View List of Commands!
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan Ke Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                         "🤖 Assistant", url=f"https://t.me/{ASSISTANT_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "🛠 Repo", url="https://github.com/UserLazy/OdaMusic"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )


@app.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.mention()}!
\n/play (song title/link/audio) — To Play the song you requested via YouTube
/song (song title) - To Download songs from YouTube
/yts (video title) — To Search Videos on YouTube with details
\n**Admins Only:**
/pause - To Pause Song playback
/resume - To resume playback of the paused song
/skip - To Skip playback of the song to the next Song
/end - To Stop Song playback
/cleandb - remove all queue
/userbotjoin - To Invite assistant to your chat
/broadcast - broadcast
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/OdaSupport"
                    ),
                    InlineKeyboardButton(
                        "Updates", url="https://t.me/UserLazyXBot"
                    )
                ]
            ]
        )
    )
