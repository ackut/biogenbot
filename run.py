import asyncio
import config as cfg
from aiogram import Bot, Dispatcher
from database.db import create_base
from app.handlers import start, genbio


async def main():
    bot = Bot(token=cfg.bot.token)
    dp = Dispatcher()
    dp.include_routers(
        start.router,
        genbio.router
    )

    await create_base()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
        # loop.run_until_complete(get_completion())
        # asyncio.run(main())

    except KeyboardInterrupt:
        print('Бот остановлен')
