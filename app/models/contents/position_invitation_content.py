class PositionInvitationContent:
    CONTENT = "You have a new position invitation: '{}'"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        team_position = metadata.get("team_position").get("title")

        notification.content = PositionInvitationContent.CONTENT.format(team_position)
