from datetime import datetime

def format_tournament_time(dt: datetime) -> str:
    return dt.strftime("%d.%m.%Y %H:%M")