from typing import Optional
from json import loads
from pydantic import BaseModel


class NotificationUpdate(BaseModel):
    nid: Optional[str] = ""
    viewed: Optional[bool] = False

    def to_json(self):
        return loads(self.json(exclude_defaults=True))
