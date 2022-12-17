from unittest.mock import Mock

import pytest
import requests_mock
from fastapi import HTTPException

from app.controllers.notifications_controller import NotificationsController
from app.models.notifications import Notifications
from app.services.teams_service import TeamsService
from app.services.users_service import UsersService


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
    tid = "1"
    team_name = "Aliados"
    team_body = {
        "name": team_name,
        "technologies": ["python"],
        "project_preferences": ["web"],
        "owner": "1234",
    }
    uid = "1"
    user_name = "Matias"
    user_lastname = "Fonseca"
    user_body = {
        "name": user_name,
        "lastname": user_lastname,
        "location": "location",
        "email": "email",
        "uid": uid,
    }

    notification = Notifications(
        sender_id=uid,
        receiver_id="2",
        notification_type="TEAM_INVITATION",
        resource="TEAM",
        resource_id=tid,
        metadata={"user": user_body, "team": team_body},
    )
    repository = Mock()
    repository.insert.return_value = True

    result = NotificationsController.post(repository, notification)
    assert result == notification


def test_error_create_notification():
    tid = "1"
    team_name = "Aliados"
    team_body = {
        "name": team_name,
        "technologies": ["python"],
        "project_preferences": ["web"],
        "owner": "1234",
    }
    uid = "1"
    user_name = "Matias"
    user_lastname = "Fonseca"
    user_body = {
        "name": user_name,
        "lastname": user_lastname,
        "location": "location",
        "email": "email",
        "uid": uid,
    }

    notification = Notifications(
        sender_id=uid,
        receiver_id="2",
        notification_type="TEAM_INVITATION",
        resource="TEAM",
        resource_id=tid,
        metadata={"user": user_body, "team": team_body},
    )
    repository = Mock()
    repository.insert.return_value = False

    with pytest.raises(HTTPException) as e:
        NotificationsController.post(repository, notification)
