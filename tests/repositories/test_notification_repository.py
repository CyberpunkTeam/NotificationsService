import mongomock

from app import config
from app.models.notifications import Notifications
from app.repositories.notifications_repository import NotificationsRepository


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_save_notification():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = NotificationsRepository(url, db_name)

    notification = Notifications(
        sender_id="1",
        receiver_id="2",
        notification_type="TEAM_INVITATION",
        resource="TEAM",
        resource_id="3",
    )

    ok = repository.insert(notification)

    assert ok


@mongomock.patch(servers=(("server.example.com", 27017),))
def test_get_notification():
    url = config.DATABASE_URL
    db_name = config.DATABASE_NAME
    repository = NotificationsRepository(url, db_name)
    receiver_id = "2"
    notification = Notifications(
        sender_id="1",
        receiver_id=receiver_id,
        notification_type="TEAM_INVITATION",
        resource="TEAM",
        resource_id="3",
    )
    ok = repository.insert(notification)

    assert ok

    notification_found = repository.get(receiver_id)

    assert len(notification_found) == 1

    notification_found = notification_found[0]

    assert notification_found.sender_id == "1"
    assert notification_found.receiver_id == "2"
    assert notification_found.notification_type == "TEAM_INVITATION"
    assert notification_found.resource == "TEAM"
    assert notification_found.resource_id == "3"
