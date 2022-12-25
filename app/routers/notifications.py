from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.notifications_controller import NotificationsController
from app.models.notifications import Notifications
from app.models.responses.notifications import Notifications as NotificationsResponse
from app.models.requests.notification_update import NotificationUpdate
from app.repositories.notifications_repository import NotificationsRepository

router = APIRouter()

# Repository
notification_repository = NotificationsRepository(
    config.DATABASE_URL, config.DATABASE_NAME
)


@router.post(
    "/notifications/",
    tags=["notifications"],
    response_model=Notifications,
    status_code=201,
)
async def create_notification(notification: Notifications):
    return NotificationsController.post(notification_repository, notification)


@router.get(
    "/notifications/",
    tags=["notifications"],
    response_model=List[NotificationsResponse],
)
async def list_notifications(receiver_id: str):
    return NotificationsController.get(notification_repository, receiver_id=receiver_id)


@router.get(
    "/notifications/{nid}",
    tags=["notifications"],
    response_model=List[NotificationsResponse],
)
async def get_notification(nid: str):
    return NotificationsController.get(notification_repository, nid=nid)


@router.put(
    "/notifications/viewed/",
    tags=["notifications"],
    response_model=List[NotificationsResponse],
)
async def update_viewed(nids: str):
    list_to_update = nids[1 : len(nids) - 1].replace(" ", "").split(",")
    return NotificationsController.put_many_viewed(
        notification_repository, list_to_update
    )


@router.put(
    "/notifications/{nid}", tags=["notifications"], response_model=NotificationsResponse
)
async def update(nid: str, notification: NotificationUpdate):
    return NotificationsController.put(notification_repository, nid, notification)
