from aiogram import Dispatcher
from aiogram.types import Message, InputFile

from telegram_bot.bot import bot
from video_base.video import VideoProcess
import utils.stats


async def start(message: Message) -> None:
    await message.answer(text='Hello')
    await message.delete()


async def send_screenshot(message: Message) -> None:
    user_id: int = message.from_user.id
    buf = await VideoProcess.screenshot()
    await bot.send_photo(user_id,
                         caption=f'On cam:',
                         photo=InputFile(buf))


async def off_motion_detection_mode(message: Message) -> None:
    motion_detection_mode = await VideoProcess.get_motion_detection_mode()
    if motion_detection_mode is False:
        await bot.send_message(message.from_user.id,
                               text='Motion detection mode is already turned off')
    else:
        await VideoProcess.switch_motion_detection_mode()
        await bot.send_message(message.from_user.id,
                               text='Motion detection mode is off')


async def on_motion_detection_mode(message: Message) -> None:
    motion_detection_mode = await VideoProcess.get_motion_detection_mode()
    if motion_detection_mode is True:
        await bot.send_message(message.from_user.id,
                               text='Motion detection mode is already turned on')
    else:
        await VideoProcess.switch_motion_detection_mode()
        await bot.send_message(message.from_user.id,
                               text='Motion detection mode is on')


async def get_cpu_memory_stats(message: Message):
    stats = await utils.stats.stats()
    await bot.send_message(message.from_user.id,
                           text=stats)


def register_admin(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(send_screenshot, commands=['sc'])
    dp.register_message_handler(off_motion_detection_mode, commands=['off_detection_mode'])
    dp.register_message_handler(on_motion_detection_mode, commands=['on_detection_mode'])
    dp.register_message_handler(get_cpu_memory_stats, commands=['stats'])

