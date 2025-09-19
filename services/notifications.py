from aiogram import Bot
from services.user_storage import JsonUserStorage
from services.tournament_api import TournamentAPI
from models import Tournament
from datetime import datetime, timedelta

class Notifier:
    def __init__(self, bot: Bot, user_storage: JsonUserStorage):
        self.bot = bot
        self.user_storage = user_storage
        self.sent_notifications = set()  # (user_id, tournament_id)

    async def notify_about_tournament(self, tournament: Tournament):
        users = self.user_storage.get_subscribed_users()
        for user in users:
            key = (user.user_id, tournament.id)
            if key in self.sent_notifications:
                continue
            text = (
                f"Напоминание о турнире: <b>{tournament.title}</b>\n"
                f"Начало: {tournament.start_time.strftime('%d.%m.%Y %H:%M')}\n"
                f"{tournament.description or ''}"
            )
            try:
                await self.bot.send_message(user.user_id, text)
                self.sent_notifications.add(key)
            except Exception as e:
                print(f"Ошибка при отправке напоминания {user.user_id}: {e}")

    def clear_old_notifications(self, max_age_hours=48):
        # Можно реализовать очистку старых записей для экономии памяти
        pass