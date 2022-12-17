from app.models.contents import Contents, TeamInvitationContent
from app.models.notifications import Notifications


def test_get_content_for_team_invitation():
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

    Contents.complete(notification)

    expected_content = TeamInvitationContent.CONTENT.format(
        user_name + " " + user_lastname, team_name
    )

    assert expected_content == notification.content
