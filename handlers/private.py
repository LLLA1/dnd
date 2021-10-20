from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAItmWD3OC0m03OLIcpSzfiJMCDxm4xJAAKFAwACH8C5V-U9VextES_XIAQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ  ɢʀᴏᴜᴩ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ. 
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀɴᴅ ᴘʟᴀʏ ᴍᴜsɪᴄ ғʀᴇᴇʟʏ Developed By [ᴡᴀʀʙᴏᴛᴢ](https://t.me/BANDA1M) !**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المبرمج..♥️🙂", url="https://t.me/alazizy")
                  ],[
                    InlineKeyboardButton(
                        "جروب الدعم..🙂♥️", url="https://t.me/alazizy1"
                    ),
                    InlineKeyboardButton(
                        "قناة السورس..🙂♥️", url="https://t.me/BANDA1M"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "اضف البوت لمجموعتك", url="https://t.me/camillamusicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/BANDA1M")
                ]
            ]
        )
   )
