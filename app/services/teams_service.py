from app import config
import requests

from app.models.exceptions.teams_service_error import TeamsServiceError


class TeamsService:
    URL = config.TEAMS_SERVICE_URL
    RESOURCE_ENDPOINT = "teams/"

    @staticmethod
    def get_name_by_tid(tid):
        response = requests.get(TeamsService.URL + TeamsService.RESOURCE_ENDPOINT + tid)
        if response.ok:
            team_info = response.json()
            return team_info.get("name")
        else:
            raise TeamsServiceError()
