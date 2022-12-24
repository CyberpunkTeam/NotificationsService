import uuid
from json import loads
from typing import Optional

from pydantic import BaseModel


class Notifications(BaseModel):
    nid: Optional[str] = None
    sender_id: str
    receiver_id: str
    notification_type: str
    resource: str
    resource_id: str
    content: Optional[str]
    metadata: Optional[dict] = None
    viewed: Optional[bool]

    def to_json(self):
        return loads(self.json(exclude_defaults=True))

    @staticmethod
    def get_schema():
        return {
            "nid": str,
            "sender_id": str,
            "receiver_id": str,
            "notification_type": str,
            "resource": str,
            "resource_id": str,
            "content": str,
            "viewed": bool,
        }

    @staticmethod
    def get_nid():
        myuuid = uuid.uuid4()
        return str(myuuid)
