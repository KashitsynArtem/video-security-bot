import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InputFile


from settings import Settings


bot = Bot(token=Settings.BOT_API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


async def send_alert(buf):
    await bot.send_photo(chat_id=Settings.ID_ADMIN,
                         caption=f'Alert:',
                         photo=InputFile(buf))


async def send_error(caption_error):
    await bot.send_message(chat_id=Settings.ID_ADMIN,
                           text=f'Error: {caption_error}')