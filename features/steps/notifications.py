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
    body = {
        "sender_id": "2",
        "receiver_id": f"{len(name)}",
        "notification_type": "TEAM_INVITATION",
        "resource": "TEAM",
        "resource_id": "14453",
    }
    response = context.client.post(url, json=body, headers=headers)

    assert response.status_code == 201


@then('a "{name}" le llega una notificacion')
def step_impl(context, name):
    """
    :param name: str
    :type context: behave.runner.Context
    """
    receiver_id = f"{len(name)}"
    url = f"/notifications?receiver_id={receiver_id}"

    response = context.client.get(url)

    assert response.status_code == 200
    assert len(response.json()) == 1
