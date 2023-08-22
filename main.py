import asyncio

from telegram_bot import handlers
from telegram_bot.bot import dp
from video_base.video import VideoProcess


async def main():

    while True:
        handlers.setup(dp)

        try:
            async with asyncio.TaskGroup() as tg:
                tg.create_task(dp.start_polling())
                tg.create_task(VideoProcess.read_video())

        except Exception as ex:
            print(ex)
            continue

        finally:
            dp.stop_polling()


if __name__ == '__main__':
    asyncio.run(main())



