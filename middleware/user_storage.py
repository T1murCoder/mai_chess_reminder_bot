from aiogram import BaseMiddleware

class UserStorageMiddleware(BaseMiddleware):
    def __init__(self, user_storage):
        self.user_storage = user_storage

    async def __call__(self, handler, event, data):
        data["user_storage"] = self.user_storage
        return await handler(event, data)