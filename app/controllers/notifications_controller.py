from fastapi import HTTPException

from app.models.contents import Contents
from app.models.notification_types import NotificationTypes
from app.models.notifications import Notifications


class NotificationsController:
    @staticmethod
    def post(repository, notification: Notifications):

        if not NotificationTypes.is_valid_type(notification.notification_type):
            raise HTTPException(status_code=400, detail="Invalid type of notification")

        Contents.complete(notification)
        notification.metadata = None
        notification.viewed = False
        notification.nid = Notifications.get_nid()
        ok = repository.insert(notification)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")

        return notification

    @staticmethod
    def get(repository, receiver_id=None, nid=None):
        result = repository.get(receiver_id=receiver_id, nid=nid)
        return result

    @staticmethod
    def put(repository, nid, notification):
        notification.nid = nid
        ok = repository.put(notification)
        if not ok:
            raise HTTPException(status_code=500, detail="Error to update")

        notification_updated = repository.get(nid=nid)
        return notification_updated
