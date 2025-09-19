import aiohttp
from typing import List
from models import Tournament
from datetime import datetime
from dateutil import parser as date_parser
import pandas as pd


class TournamentAPI:
    def __init__(self, api_url: str):
        self.api_url = api_url

    async def fetch_tournaments(self) -> List[Tournament]:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.api_url) as resp: # TODO: Change this shit
                data = await resp.json(content_type="text/html")
                print(data)
                tournaments = []
                for item in data:
                    tournaments.append(
                        Tournament(
                            id=str(item["id"]),
                            title=item["name"],
                            start_time=date_parser.parse(item["startDateWithTime"]),
                            description="хуууй"
                        )
                    )
                return tournaments