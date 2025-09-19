from aiogram import Router, types
from aiogram.filters import CommandStart

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я напомню тебе о ближайших шахматных турнирах.\n"
        "Используй /subscribe чтобы получать напоминания.\n"
        "Используй /help для справки."
    )