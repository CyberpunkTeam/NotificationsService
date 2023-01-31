class NewTeamCandidateContent:
    CONTENT = "There is a new candidate for the {} position from {} team"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata
        position = metadata.get("position")
        position_title = position.get("title")
        team_name = position.get("team").get("name")

        notification.content = NewTeamCandidateContent.CONTENT.format(
            position_title, team_name
        )
