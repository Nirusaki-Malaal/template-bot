from pyrogram import filters, idle
from bot import bot, Config, LOGS


@bot.on_message(filters.incoming & filters.command(["start"]))
async def help_message(bot, message):
  if message.chat.id not in Config.AUTH_USERS:
    return
  text = "**▻ This is A Simple Telegram BOT**"
  await bot.send_message(
        chat_id=message.from_user.id,
        text=text,
        reply_to_message_id=message.id,
    )
  
async def startup():
    await bot.start()
    LOGS.info(f'[Started]: @{(await bot.get_me()).username}')
    x = len(Config.AUTH_USERS)
    for i in range(0, x):
      await bot.send_message(chat_id=Config.AUTH_USERS[i], text="**Bot Has Restarted**") ## MAKE SURE YOU HAVE STARTED THE BOT ONCE FROM TELEGRAM OTHERWISE IT WILL GIVE AN ERROR
    await idle()
    await bot.stop()

bot.loop.run_until_complete(startup())