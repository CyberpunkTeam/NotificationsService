import requests_mock
from behave import *

from app.services.teams_service import TeamsService
from app.services.users_service import UsersService


@given("que cree un equipo y soy owner de el")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('invito al usuario "{name}" para que sea miembro del equipo')
def step_impl(context, name):
    """
    :param name: str
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/notifications"
    uid = "2"
    tid = "14453"
    body = {
        "sender_id": uid,
        "receiver_id": f"{len(name)}",
        "notification_type": "TEAM_INVITATION",
        "resource": "TEAM",
        "resource_id": tid,
    }

    json_headers = {"Content-Type": "application/json", "Accept": "application/json"}
    team_name = "Aliados"
    team_body = {
        "name": team_name,
        "technologies": ["python"],
        "project_preferences": ["web"],
        "owner": uid,
    }
    user_name = "Gonzalo"
    user_lastname = "Marino"

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

        response = context.client.post(url, json=body, headers=headers)

        assert response.status_code == 201


@then('a "{name}" le llega una notificacion de invitacion a equipo')
def step_impl(context, name):
    """
    :param name: str
    :type context: behave.runner.Context
    """
    receiver_id = f"{len(name)}"
    url = f"/notifications?receiver_id={receiver_id}"

    response = context.client.get(url)

    assert response.status_code == 200
    assert (
        response.json()[0].get("content")
        == "Gonzalo Marino te ha invitado al equipo Aliados"
    )
