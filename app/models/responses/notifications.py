from typing import Optional

from pydantic.main import BaseModel


class Notifications(BaseModel):
    nid: str
    sender_id: str
    receiver_id: str
    notification_type: str
    resource: str
    resource_id: str
    content: Optional[str]
    viewed: Optional[bool]
    created_date: Optional[str]
    metadata: Optional[dict]
