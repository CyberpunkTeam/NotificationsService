from fastapi import HTTPException
from app.models.notifications import Notifications


class NotificationsController:
    @staticmethod
    def post(repository, notification: Notifications):
        ok = repository.insert(notification)
        if not ok:
            raise HTTPException(status_code=500, detail="Error saving")
        return notification

    @staticmethod
    def get(repository, sender_id):
        result = repository.get(sender_id)
        return result
