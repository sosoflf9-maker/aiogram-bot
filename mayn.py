
from os import getenv
import asyncio

import uvicorn
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()

from routes import router, setup_database
from photo_sync import app as photo_sync_app

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(router)



async def run_bot():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN не задан")

    bot = Bot(token=TOKEN)
    await setup_database()

    print("Telegram bot started")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


async def run_http():
    config = uvicorn.Config(
        photo_sync_app,
        host="0.0.0.0",
        port=int(getenv("PORT", "8000")),
        log_level="info",
    )
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    await asyncio.gather(run_bot(), run_http())


if __name__ == "__main__":
    asyncio.run(main())
