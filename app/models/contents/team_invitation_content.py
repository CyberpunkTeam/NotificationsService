class TeamInvitationContent:
    CONTENT = "{} invited you to join {} team"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        team_name = metadata.get("team").get("name")
        user_name = (
            metadata.get("user", {}).get("name")
            + " "
            + metadata.get("user", {}).get("lastname")
        )

        notification.content = TeamInvitationContent.CONTENT.format(
            user_name, team_name
        )
