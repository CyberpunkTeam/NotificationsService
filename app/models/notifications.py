from json import loads
from typing import Optional

from pydantic import BaseModel


class Notifications(BaseModel):
    sender_id: str
    receiver_id: str
    notification_type: str
    resource: str
    resource_id: str
    content: Optional[str]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "sender_id": str,
            "receiver_id": str,
            "notification_type": str,
            "resource": str,
            "resource_id": str,
            "content": str,
        }
