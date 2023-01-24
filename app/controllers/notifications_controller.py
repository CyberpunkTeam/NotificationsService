from fastapi import HTTPException
from datetime import datetime
from app.models.contents import Contents
from app.models.metadata import Metadata
from app.models.notification_types import NotificationTypes
from app.models.notifications import Notifications
from app.models.requests.notification_update import NotificationUpdate


class NotificationsController:
    @staticmethod
    def post(repository, notification: Notifications):

        if not NotificationTypes.is_valid_type(notification.notification_type):
            raise HTTPException(status_code=400, detail="Invalid type of notification")

        Contents.complete(notification)
        Metadata.complete(notification)
        notification.viewed = False
        notification.nid = Notifications.get_nid()

        local = datetime.now()
        notification.created_date = local.strftime("%d-%m-%Y:%H:%M:%S")

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
        return notification_updated[0]

    @staticmethod
    def put_many_viewed(repository, nids):
        result = []
        for nid in nids:
            try:
                notification = NotificationsController.put(
                    repository, nid, NotificationUpdate(viewed=True)
                )
                result.append(notification)
            except:
                pass
        return result
