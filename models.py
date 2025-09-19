from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Tournament(BaseModel):
    id: str
    title: str
    start_time: datetime
    description: Optional[str] = None

class User(BaseModel):
    user_id: int
    username: Optional[str] = None
    is_subscribed: bool = True

class Subscription(BaseModel):
    user_id: int
    tournament_id: str