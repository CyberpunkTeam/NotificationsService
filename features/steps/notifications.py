from behave import *


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

    body = {
        "sender_id": uid,
        "receiver_id": f"{len(name)}",
        "notification_type": "TEAM_INVITATION",
        "resource": "TEAM",
        "resource_id": tid,
        "metadata": {"user": user_body, "team": team_body},
    }
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