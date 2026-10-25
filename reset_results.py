
import asyncio
import aiosqlite
from routes import DB_PATH


async def reset_results():
    confirm = input(
        "Удалить ВСЕ результаты из рейтинга? Напиши ДА для подтверждения: "
    )

    if confirm != "ДА":
        print("Отменено. Данные сохранены.")
        return

    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM results")
        await db.commit()

    print("Все результаты удалены. Таблица и фотографии сохранены.")


if __name__ == "__main__":
    asyncio.run(reset_results())
