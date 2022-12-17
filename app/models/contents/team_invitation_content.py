from app.services.teams_service import TeamsService
from app.services.users_service import UsersService


class TeamInvitationContent:
    CONTENT = "{} te ha invitado al equipo {}"

    @staticmethod
    def complete(notification):
        print("entra a completar el contenido de la team invitation")
        team_name = TeamsService.get_name_by_tid(notification.resource_id)
        print("obtuvo los datos del team")
        user_name = UsersService.get_name_by_uid(notification.sender_id)
        print("obtuvo los datos del user")
        notification.content = TeamInvitationContent.CONTENT.format(
            user_name, team_name
        )
