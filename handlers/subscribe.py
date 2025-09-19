from aiogram import Router, types
from aiogram.filters import Command

subscribe_router = Router()

@subscribe_router.message(Command("subscribe"))
async def cmd_subscribe(message: types.Message, user_storage):
    user_storage.subscribe(message.from_user.id, message.from_user.username)
    await message.answer("Вы успешно подписались на напоминания о турнирах!")

@subscribe_router.message(Command("unsubscribe"))
async def cmd_unsubscribe(message: types.Message, user_storage):
    user_storage.unsubscribe(message.from_user.id)
    await message.answer("Вы отписались от напоминаний.")