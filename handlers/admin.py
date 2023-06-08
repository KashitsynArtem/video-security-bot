from aiogram import Dispatcher
from aiogram.types import Message, InputFile
from video_base import video_base as vb
from bot import bot


async def start(message: Message) -> None:
    await message.answer(text='Hello')
    await message.delete()


async def get_image(message: Message) -> None:
    user_id: int = message.from_user.id
    buf = await vb.get_screenshot()
    await bot.send_photo(user_id,
                         caption=f'On cam:',
                         photo=InputFile(buf))


def register_admin(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(get_image, commands=['sc'])
