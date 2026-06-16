import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import basic, api_commands




logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(basic.router)
    dp.include_router(api_commands.router)
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())
