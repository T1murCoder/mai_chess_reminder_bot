from aiogram import Router, types
from aiogram.filters import Command

help_router = Router()

@help_router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Команды:\n"
        "/start — начать общение\n"
        "/subscribe — подписаться на напоминания\n"
        "/unsubscribe — отписаться от напоминаний\n"
        "/help — помощь"
    )