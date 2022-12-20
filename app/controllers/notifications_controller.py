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

        ok = repository.insert(notification)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")

        return notification

    @staticmethod
    def get(repository, sender_id):
        result = repository.get(sender_id)
        return result
