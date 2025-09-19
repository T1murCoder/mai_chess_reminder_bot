import json
import os
from typing import List, Optional
from models import User

USER_JSON_FILE = "users.json"

class JsonUserStorage:
    def __init__(self):
        if not os.path.exists(USER_JSON_FILE):
            with open(USER_JSON_FILE, "w") as f:
                json.dump([], f)
    
    def _load(self) -> List[dict]:
        with open(USER_JSON_FILE, "r") as f:
            return json.load(f)

    def _save(self, data: List[dict]):
        with open(USER_JSON_FILE, "w") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def subscribe(self, user_id: int, username: Optional[str]):
        users = self._load()
        for user in users:
            if user["user_id"] == user_id:
                user["is_subscribed"] = True
                user["username"] = username
                self._save(users)
                return
        users.append({"user_id": user_id, "username": username, "is_subscribed": True})
        self._save(users)

    def unsubscribe(self, user_id: int):
        users = self._load()
        for user in users:
            if user["user_id"] == user_id:
                user["is_subscribed"] = False
        self._save(users)

    def get_subscribed_users(self) -> List[User]:
        users = self._load()
        return [User(**u) for u in users if u.get("is_subscribed")]

def get_user_storage(storage_type: str = "json"):
    # На данном этапе реализован только json, можно добавить SQLite и др.
    return JsonUserStorage()