from app.models.contents import (
    Contents,
    TeamInvitationContent,
    TeamPostulationContent,
    AbandonedProjectContent,
    ProjectFinishedContent,
    ProjectFinishedRequestContent,
)
from app.models.contents.team_postulation_response_content import (
    TeamPostulationResponseContent,
)
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


def test_get_content_for_team_postulation():
    project_name = "Aliados"
    project_body = {
        "name": project_name,
        "technologies": ["python"],
        "project_preferences": ["web"],
        "owner": "1234",
    }
    tid = "1"
    team_name = "Alfa"
    team_body = {
        "name": team_name,
    }

    notification = Notifications(
        sender_id=tid,
        receiver_id="2",
        notification_type="TEAM_POSTULATION",
        resource="TEAM_POSTULATION",
        resource_id="1234",
        metadata={"team": team_body, "project": project_body},
    )

    Contents.complete(notification)

    expected_content = TeamPostulationContent.CONTENT.format(team_name, project_name)

    assert expected_content == notification.content


def test_get_content_for_team_postulation_response():
    project_name = "Aliados"
    project_body = {
        "name": project_name,
        "technologies": ["python"],
        "project_preferences": ["web"],
        "owner": "1234",
    }
    response = "ACCEPTED"

    notification = Notifications(
        sender_id="12",
        receiver_id="2",
        notification_type="TEAM_POSTULATION_RESPONSE",
        resource="TEAM_POSTULATION",
        resource_id="1234",
        metadata={"response": response, "project": project_body},
    )

    Contents.complete(notification)

    expected_content = TeamPostulationResponseContent.CONTENT.format(
        "acepto", project_name
    )

    assert expected_content == notification.content


def test_get_content_for_abandoned_project():
    project_name = "Aliados"
    pid = "12"
    project_body = {
        "pid": pid,
        "name": project_name,
        "technologies": ["python"],
        "project_preferences": ["web"],
        "owner": "1234",
    }
    tid = "1"
    team_name = "Alfa"
    team_body = {
        "name": team_name,
    }

    notification = Notifications(
        sender_id=tid,
        receiver_id=pid,
        notification_type="ABANDONED_PROJECT",
        resource="PROJECT",
        resource_id=pid,
        metadata={"team": team_body, "project": project_body},
    )

    Contents.complete(notification)

    expected_content = AbandonedProjectContent.CONTENT.format(team_name, project_name)

    assert expected_content == notification.content


def test_get_content_for_project_finished():
    project_name = "Aliados"
    pid = "12"
    project_body = {
        "pid": pid,
        "name": project_name,
        "technologies": ["python"],
        "project_preferences": ["web"],
        "owner": "1234",
    }
    tid = "1"
    team_name = "Alfa"
    team_body = {
        "name": team_name,
    }

    notification = Notifications(
        sender_id=tid,
        receiver_id=pid,
        notification_type="PROJECT_FINISHED",
        resource="PROJECT",
        resource_id=pid,
        metadata={"project": project_body},
    )

    Contents.complete(notification)

    expected_content = ProjectFinishedContent.CONTENT.format(project_name)

    assert expected_content == notification.content


def test_get_content_for_project_finished_request():
    project_name = "Aliados"
    pid = "12"
    project_body = {
        "pid": pid,
        "name": project_name,
        "technologies": ["python"],
        "project_preferences": ["web"],
        "owner": "1234",
    }
    tid = "1"
    team_name = "Alfa"
    team_body = {
        "name": team_name,
    }

    notification = Notifications(
        sender_id=pid,
        receiver_id=tid,  # owner team id
        notification_type="PROJECT_FINISHED_REQUEST",
        resource="PROJECT",
        resource_id=pid,
        metadata={"project": project_body},
    )

    Contents.complete(notification)

    expected_content = ProjectFinishedRequestContent.CONTENT.format(project_name)

    assert expected_content == notification.content
