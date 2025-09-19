from aiogram import Dispatcher

from .start import start_router
from .subscribe import subscribe_router
from .help import help_router

def register_handlers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(subscribe_router)
    dp.include_router(help_router)