from app.models.notifications import Notifications


def test_create_notification():
    notification = Notifications(
        sender_id="1",
        receiver_id="2",
        notification_type="TEAM_INVITATION",
        resource="TEAM",
        resource_id="3",
    )
    assert notification.sender_id == "1"
    assert notification.receiver_id == "2"
    assert notification.notification_type == "TEAM_INVITATION"
    assert notification.resource == "TEAM"
    assert notification.resource_id == "3"
