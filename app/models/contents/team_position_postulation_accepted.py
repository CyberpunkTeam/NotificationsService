class TeamPositionAcceptedContent:
    CONTENT = "Your postulation to {} of {} team was accepted"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata
        position = metadata.get("position")
        position_title = position.get("title")
        team_name = position.get("team").get("name")

        notification.content = TeamPositionAcceptedContent.CONTENT.format(
            position_title, team_name
        )
