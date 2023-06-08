import logging
import asyncio
from bot import bot, dp
from aiogram import Dispatcher
import handlers

logging.basicConfig(level=logging.INFO)


async def main(dispatcher: Dispatcher) -> None:
    handlers.setup(dispatcher)

    try:
        await dispatcher.start_polling()
    finally:
        await dispatcher.storage.close()
        await dispatcher.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main(dp))

