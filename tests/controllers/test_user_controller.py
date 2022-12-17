from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app.controllers.notifications_controller import NotificationsController
from app.models.notifications import Notifications


def test_get_notification_by_receiver_id():
    repository = Mock()
    receiver_id = "2"
    notification = Notifications(
        sender_id="1",
        receiver_id=receiver_id,
        notification_type="TEAM_INVITATION",
        resource="TEAM",
        resource_id="3",
    )
    repository.get.return_value = [notification]
    result = NotificationsController.get(repository, receiver_id)
    assert result[0].receiver_id == receiver_id


def test_create_notification():
    repository = Mock()
    repository.insert.return_value = True
    notification = Notifications(
        sender_id="1",
        receiver_id="2",
        notification_type="TEAM_INVITATION",
        resource="TEAM",
        resource_id="3",
    )
    result = NotificationsController.post(repository, notification)
    assert result == notification


def test_error_create_user():
    repository = Mock()
    repository.insert.return_value = False
    notification = Notifications(
        sender_id="1",
        receiver_id="2",
        notification_type="TEAM_INVITATION",
        resource="TEAM",
        resource_id="3",
    )
    with pytest.raises(HTTPException):
        NotificationsController.post(repository, notification)
