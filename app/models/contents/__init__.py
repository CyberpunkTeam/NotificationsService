from app.models.contents.team_invitation_content import TeamInvitationContent
from app.models.contents.team_postulation_content import TeamPostulationContent
from app.models.contents.team_postulation_response_content import (
    TeamPostulationResponseContent,
)


class Contents:
    COMPLETERS = {
        "TEAM_INVITATION": TeamInvitationContent,
        "TEAM_POSTULATION": TeamPostulationContent,
        "TEAM_POSTULATION_RESPONSE": TeamPostulationResponseContent,
    }

    @staticmethod
    def complete(notification):
        notification_type = notification.notification_type

        if notification_type in Contents.COMPLETERS:
            completer = Contents.COMPLETERS.get(notification_type)
            completer.complete(notification)
