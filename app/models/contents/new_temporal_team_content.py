class NewTemporalTeamContent:
    CONTENT = "You joined to a new temporal team: {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata
        team_name = metadata.get("team").get("name")

        notification.content = NewTemporalTeamContent.CONTENT.format(team_name)
