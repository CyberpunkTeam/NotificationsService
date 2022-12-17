from app.models.notification_types import NotificationTypes


def test_valid_type():
    team_invitation_type = NotificationTypes.TYPES[0]

    assert NotificationTypes.is_valid_type(team_invitation_type)


def test_invalid_type():
    invalid_type = "invalid type"

    assert not NotificationTypes.is_valid_type(invalid_type)
