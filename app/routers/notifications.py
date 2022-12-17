from typing import List

from fastapi import APIRouter

from app import config
from app.controllers.notifications_controller import NotificationsController
from app.models.notifications import Notifications
from app.repositories.notifications_repository import NotificationsRepository

router = APIRouter()

# Repository
user_repository = NotificationsRepository(config.DATABASE_URL, config.DATABASE_NAME)


@router.post(
    "/notifications",
    tags=["notifications"],
    response_model=Notifications,
    status_code=201,
)
async def create_notification(notification: Notifications):

    return NotificationsController.post(user_repository, notification)


@router.get(
    "/notifications", tags=["notifications"], response_model=List[Notifications]
)
async def list_notifications(receiver_id: str):
    return NotificationsController.get(user_repository, receiver_id)
