import requests_mock

from app.models.contents import Contents, TeamInvitationContent
from app.models.notifications import Notifications
from app.services.teams_service import TeamsService
from app.services.users_service import UsersService


def test_get_content_for_team_invitation():
    tid = "1"
    json_headers = {"Content-Type": "application/json", "Accept": "application/json"}
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

    with requests_mock.Mocker() as m:
        m.get(
            TeamsService.URL + TeamsService.RESOURCE_ENDPOINT + tid,
            headers=json_headers,
            status_code=200,
            json=team_body,
        )

        m.get(
            UsersService.URL + UsersService.RESOURCE_ENDPOINT + uid,
            headers=json_headers,
            status_code=200,
            json=user_body,
        )

        notification = Notifications(
            sender_id=uid,
            receiver_id="2",
            notification_type="TEAM_INVITATION",
            resource="TEAM",
            resource_id=tid,
        )

        Contents.complete(notification)

        expected_content = TeamInvitationContent.CONTENT.format(
            user_name + " " + user_lastname, team_name
        )

        assert expected_content == notification.content
