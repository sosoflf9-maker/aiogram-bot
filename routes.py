# from mailbox import Message
# from aiogram import Router, F
# from aiogram.filters import Command
# from aiogram.types import (
#     Message,
#     CallbackQuery,
#     ReplyKeyboardMarkup,
#     KeyboardButton,
#     InlineKeyboardMarkup,
#     InlineKeyboardButton
# )
# from forms.user import Form
# from aiogram.fsm.context import FSMContext
# from  aiogram import Bot
# from aiogram.types import  Message, FSInputFile


















# from aiogram import Router, F
# from  aiogram.filters import Command
# from aiogram.types import  Message, FSInputFile




# router = Router()

# # ---- 

# import aiohttp

# async def get_product(product_id): 
#     url = f"https://fakestoreapi.com/products/{product_id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             if resp.status == 404:
#                 return None

#             data = await resp.json()
#             return data

        

# # ----
# @router.message(Command("start"))
# async def start(message: Message): 
#     await message.answer("Привет! Я простой Бот-магазин.\nВведите команду: /product ID\n\nПример: <b>/product 1</b>",
#                          parse_mode="HTML"
#     )
   
# @router.message(Command("product"))
# async def get_product_cmd(message: Message):
#     parts = message.text.strip().split()

# #   /product 23 some - example
#     if len(parts) != 2:
#         await message.answer("Используйтe: /product 1")
#         return

#     product_id = parts[1]
#     if not product_id.isdigit():
#          await message.answer("ID товара должно быть числом")
#          return

#     await message.answer(f'Ищу товары с id: {product_id}')

#     try:
#         product = await get_product(int(product_id))

#     except Exception:
#         await message.answer('Не удалось обратиться к серверу')
#         return

#     if product is None:
#         await message.answer('Такого товара нет')
#         return
    
#     title = product.get("title", "Без названия")
#     price = product.get("price", "-")
#     desc = product.get("description", "Без discription")
#     category = product.get("category", "Без category")
#     image = product.get("image")

#     text = (

#         f"<b>{title}</b>\n\n" 
#         f"Категория: <i>{category}</i>\n"
#         f"Цена: <b>{price}$</b>\n"
#         f"{desc}"
#     )

#     photo = FSInputFile("no-image.png")
#     await message.answer_photo(photo = photo, caption = text, parse_mode = "HTML")














# @router.message(Command("start"))
# async def start(message: Message, state: FSMContext): 
#     await message.answer("Давайте начнем заполнять анкету!\nСперва введите ваше имя:")
#     await state.set_state(Form.name)

# @router.message(Command("cancel"))
# async def cancel_form(message: Message, state: FSMContext):
#     await state.clear()
#     await message.answer("Анкета отклонена!")


# @router.message(Form.name, F.text)
# async def proccess_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
    
#     await message.answer("Отлично!\nА теперь введите ваш возраст:")
#     await state.set_state(Form.age)


# @router.message(Form.age, F.text)
# async def proccess_age(message: Message, state: FSMContext):
#     if not message.text.isdigit():
#         await message.answer("Возраст должен быть числом")
#         return

#     if int(message.text) < 1 or int(message.text) > 100:
#         await message.answer("Возраст должен быть от 1 до 100")
#         return

    
    
#     await state.update_data(age=int(message.text))
    
#     await message.answer("Отлично!\nА теперь введите ваш email:")
#     await state.set_state(Form.email)



# @router.message(Form.email, F.text)
# async def proccess_email(message: Message, state: FSMContext):
#     email_text = message.text
#     if "@" not in email_text or "." not in email_text:
#         await message.answer("Email не корректный")
#         return

    
    
#     await state.update_data(email=email_text)

#     data = await state.get_data()
#     name = data["name"]
#     age = data["age"]
#     email = data["email"]



    
#     await message.answer(f"Анкета готова!\nИмя: {name}\nВозраст: {age}\nПочта: {email}")
    
#     await state.clear()

# @router.message(F.photo)
# async def proccess_photo(message: Message):
#     photo = message.photo[-1]
#     file_id = photo.file_id

#     await message.answer(
#         f"Вы отправили фото!\nID photo: <code>{file_id}</code>",
#         parse_mode="HTML"
#     )

#     await message.answer_photo(file_id, caption="Вот ваше фото")




# @router.message(F.video)
# async def proccess_video(message: Message):
#     video = message.video[-1]
#     file_id = video.file_id
#     duration = video.duration
    
#     await message.answer(
#         f"Вы отправили видео!\nID video: <code>{file_id}</code>\nДлительность: <code>{duration}</code>",
#         parse_mode="HTML"
#     )
    
#     await message.answer_video(file_id, caption="Вот ваше видео")



# @router.message(F.animation)
# async def proccess_animation(message: Message):
#     animation = message.animation
    

#     await message.answer(
#         f"Вы отправили animation!\nID animation: <code>{animation.file_id}</code>",
#         parse_mode="HTML"
#     )

#     await message.answer_animation(animation.file_id, caption="Вот ваше animation")


# @router.message(F.document)
# async def proccess_document(message: Message, bot: Bot):
#     document = message.document
#     file_id = document.file_id

#     file = await bot.get_file(file_id)
#     file_path= file.file_path

#     local_path = f'downloads/{document.file_name}'

#     await bot.download_file(file_path=file_path, destination=local_path)

#     await message.answer('Файл сохранен!')

# @router.message(Command("file"))
# async def send_file(message: Message):
#     file = FSInputFile('files/example.txt')

#     await message.answer_document(file)











# from aiogram import Router, F
# from  aiogram.filters import Command
# from aiogram.types import  Message
# import aiosqlite

# router = Router()

# # ---
# DB_NAME = "vano.sql"

# async def init_db():
#     async with aiosqlite.connect(DB_NAME) as db:
#         await db.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         full_name TEXT,
#         age INTEGER
#         )

#    """)
#         await db.commit()


# async def add_user(full_name, age):
#     async with aiosqlite.connect(DB_NAME) as db:
#         await db.execute("INSERT INTO users (full_name, age) VALUES(?, ?)", (full_name, age))
#         await db.commit()


# async def get_users():
#     async with aiosqlite.connect(DB_NAME) as db:
#        cursor =  await db.execute("SELECT full_name, age FROM users")
#        result = await cursor.fetchall()
#        return result
     

# # ---

# @router.message(Command("start"))
# async def start(message: Message):
#     await init_db()
#     await message.answer("Привет!\nПропишите команду: /reg AGE")


# @router.message(Command("reg"))

# async def reg(message: Message):
#    parts = message.text.strip().split()
   
#    if len(parts) != 2 or not parts[1].isdigit():
#     await message.answer("Введите команду верно")
#     return

#    await add_user(message.from_user.full_name, int(parts[1]))
   
#    await message.answer("Все готово")

    
    
# @router.message(Command("users"))
# async def users(message: Message):
#    users = await get_users()

#    if not users:
#        await message.answer("В базе нет пользователя")
#        return

#    text = "Пользователь в базе:\n\n"
#    for  full_name, age in users:
#        text += f"- {full_name}- <code>{age}</code>\n"

#        await message.answer(text, parse_mode="HTML")




   
   
   
   




from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import  Message
from aiogram import Bot
import asyncio

router = Router()

subscribers = set()

async def notifier(bot: Bot):
    while True:
        if subscribers:
            for user_id in list(subscribers):
                try:
                    await bot.send_message(user_id,"ти лох")
                except Exception:
                    pass
        await asyncio.sleep(10)

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет стипа\n"
        "Я могу помочь с расслыкой!\n\n"
        "Команды:\n"
        "/subscribe - подписаться на уведомление\n"
        "/unsubscribe - отписка\n"
        "/subscribers - список подписчиков"
    )

@router.message(Command("subscribe"))
async def subscribe(message: Message):
    user_id = message.from_user.id

    subscribers.add(user_id)

    await message.answer("Вы подписались!")
    
@router.message(Command("unsubscribe"))
async def unsubscribe(message: Message):
    user_id = message.from_user.id

    subscribers.discard(user_id)
    
    await message.answer("Вы отписались!")
    
@router.message(Command("subscribers"))
async def subscribers_cmd(message: Message):
    if not subscribers:
        
     await message.answer("Пока никого нет")


    text = "Подписчики:\n"
    for uid in subscribers:
        text += f"{uid}\n"
    await message.answer(text)
