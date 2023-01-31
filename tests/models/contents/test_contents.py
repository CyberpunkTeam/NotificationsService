from app.models.contents import (
    Contents,
    TeamInvitationContent,
    TeamPostulationContent,
    AbandonedProjectContent,
    ProjectFinishedContent,
    ProjectFinishedRequestContent,
    ProjectAbandonsRequestContent,
    NewTeamMemberContent,
    TeamReviewContent,
    NewTeamCandidateContent,
    TeamPositionAcceptedContent,
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
        project_name, "accepted"
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
    response = "REJECTED"
    notification = Notifications(
        sender_id=tid,
        receiver_id=pid,
        notification_type="PROJECT_FINISHED",
        resource="PROJECT",
        resource_id=pid,
        metadata={"project": project_body, "response": response},
    )
    response = "aceptada" if response == "ACCEPTED" else "rechazada"
    Contents.complete(notification)

    expected_content = ProjectFinishedContent.CONTENT.format(project_name, response)

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


def test_get_content_for_project_abandons_request():
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
        notification_type="PROJECT_ABANDONS_REQUEST",
        resource="PROJECT_ABANDONS_REQUEST",
        resource_id=pid,  # par_id
        metadata={"team": team_body, "project": project_body},
    )

    Contents.complete(notification)

    expected_content = ProjectAbandonsRequestContent.CONTENT.format(
        team_name, project_name
    )

    assert expected_content == notification.content


def test_get_content_new_team_member():
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
    tid = "1"
    team_name = "Alfa"
    team_body = {
        "name": team_name,
    }

    notification = Notifications(
        sender_id=uid,
        receiver_id="team_owner",
        notification_type="NEW_TEAM_MEMBERS",
        resource="TEAM",
        resource_id=tid,
        metadata={"team": team_body, "user": user_body},
    )

    Contents.complete(notification)

    expected_content = NewTeamMemberContent.CONTENT.format(user_name, team_name)

    assert expected_content == notification.content


def test_get_content_for_team_review():
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
    response = "REJECTED"
    mid = "1"
    notification = Notifications(
        sender_id=tid,
        receiver_id=mid,
        notification_type="TEAM_REVIEW",
        resource="TEAMS",
        resource_id=tid,
        metadata={"project": project_body, "team": team_body},
    )

    Contents.complete(notification)

    expected_content = TeamReviewContent.CONTENT.format(project_name, team_name)

    assert expected_content == notification.content


def test_get_content_for_new_team_candidate():
    position_title = "Software developer"
    tpid = "124"
    tid = "1"
    team_name = "Alfa"
    owner = "123141"
    position_body = {
        "title": position_title,
        "tpid": tpid,
        "team": {"name": team_name, "owner": owner, "tid": tid},
    }

    mid = "1"
    notification = Notifications(
        sender_id=mid,
        receiver_id=owner,
        notification_type="NEW_TEAM_CANDIDATE",
        resource="TEAMS_POSITIONS",
        resource_id=tpid,
        metadata={"position": position_body},
    )

    Contents.complete(notification)

    expected_content = NewTeamCandidateContent.CONTENT.format(position_title, team_name)

    assert expected_content == notification.content


def test_get_content_for_team_position_postulation_accepted():
    position_title = "Software developer"
    tpid = "124"
    tid = "1"
    team_name = "Alfa"
    owner = "123141"
    position_body = {
        "title": position_title,
        "tpid": tpid,
        "team": {"name": team_name, "owner": owner, "tid": tid},
    }

    mid = "1"
    notification = Notifications(
        sender_id=mid,
        receiver_id=owner,
        notification_type="TEAM_POSITION_ACCEPTED",
        resource="TEAMS_POSITIONS",
        resource_id=tpid,
        metadata={"position": position_body},
    )

    Contents.complete(notification)

    expected_content = TeamPositionAcceptedContent.CONTENT.format(
        position_title, team_name
    )

    assert expected_content == notification.content
