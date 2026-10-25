from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from routes import router, setup_database

load_dotenv()
TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher()
dp.include_router(router)


async def main():
  bot = Bot(token=TOKEN)

  await setup_database() #Создаем таблицу в базе данных

  print("Start...")
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())
