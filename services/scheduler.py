import asyncio
from datetime import datetime, timedelta

from services.notifications import Notifier
from services.tournament_api import TournamentAPI

class Scheduler:
    def __init__(self, bot, user_storage, tournament_api: TournamentAPI, interval: int = 60):
        self.bot = bot
        self.user_storage = user_storage
        self.tournament_api = tournament_api
        self.interval = interval
        self.notifier = Notifier(bot, user_storage)

    async def run(self):
        while True:
            now = datetime.utcnow()
            try:
                tournaments = await self.tournament_api.fetch_tournaments()
                for tournament in tournaments:
                    # Шлём напоминание, если турнир через 1-2 часа
                    if timedelta(minutes=1) <= (tournament.start_time - now) <= timedelta(hours=2):
                        await self.notifier.notify_about_tournament(tournament)
                # Дополнительно можно реализовать напоминание за 10 минут и т.д.
            except Exception as e:
                print(f"Ошибка в планировщике: {e}")
            await asyncio.sleep(self.interval)