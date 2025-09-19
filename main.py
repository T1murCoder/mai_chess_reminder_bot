import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import settings
from handlers import register_handlers
from services.scheduler import Scheduler
from services.user_storage import get_user_storage
from services.tournament_api import TournamentAPI
from middleware.user_storage import UserStorageMiddleware


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)

async def main():
    # Инициализация бота и диспетчера
    bot = Bot(token=settings.BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())
    
    user_storage = get_user_storage(settings.USER_STORAGE_TYPE)
        
    dp.message.middleware(UserStorageMiddleware(user_storage))

    # Инициализация сервисов
    tournament_api = TournamentAPI(settings.TOURNAMENT_API_URL)
    scheduler = Scheduler(
        bot=bot,
        user_storage=user_storage,
        tournament_api=tournament_api,
        interval=settings.SCHEDULER_INTERVAL
    )

    # Регистрация обработчиков
    register_handlers(dp)

    # Старт планировщика напоминаний
    asyncio.create_task(scheduler.run())

    # Запуск polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())