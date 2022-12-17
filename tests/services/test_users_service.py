import requests_mock

from app.services.users_service import UsersService


def test_get_name():
    uid = "1"
    json_headers = {"Content-Type": "application/json", "Accept": "application/json"}
    user_name = "Matias"
    user_lastname = "Fonseca"
    body = {
        "name": user_name,
        "lastname": user_lastname,
        "location": "location",
        "email": "email",
        "uid": uid,
    }

    with requests_mock.Mocker() as m:
        m.get(
            UsersService.URL + UsersService.RESOURCE_ENDPOINT + uid,
            headers=json_headers,
            status_code=200,
            json=body,
        )

        result = UsersService.get_name_by_uid(uid)
        assert user_name + " " + user_lastname == result
