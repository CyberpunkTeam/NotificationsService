from app.models.contents.team_invitation_content import TeamInvitationContent


class Contents:
    COMPLETERS = {"TEAM_INVITATION": TeamInvitationContent}

    @staticmethod
    def complete(notification):
        notification_type = notification.notification_type

        if notification_type in Contents.COMPLETERS:
            completer = Contents.COMPLETERS.get(notification_type)
            completer.complete(notification)
