from app import config
import requests

from app.models.exceptions.users_service_error import UsersServiceError


class UsersService:
    URL = config.USERS_SERVICE_URL
    RESOURCE_ENDPOINT = "users/"

    @staticmethod
    def get_name_by_uid(uid):
        response = requests.get(UsersService.URL + UsersService.RESOURCE_ENDPOINT + uid)
        if response.ok:
            team_info = response.json()
            return team_info.get("name") + " " + team_info.get("lastname")
        else:
            raise UsersServiceError()
