import requests_mock

from app.services.teams_service import TeamsService


def test_get_name():
    tid = "1"
    json_headers = {"Content-Type": "application/json", "Accept": "application/json"}
    team_name = "Aliados"
    body = {
        "name": team_name,
        "technologies": ["python"],
        "project_preferences": ["web"],
        "owner": "1234",
    }

    with requests_mock.Mocker() as m:
        m.get(
            TeamsService.URL + TeamsService.RESOURCE_ENDPOINT + tid,
            headers=json_headers,
            status_code=200,
            json=body,
        )

        result = TeamsService.get_name_by_tid(tid)
        assert result == team_name
