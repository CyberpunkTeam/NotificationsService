class NewTeamCandidateContent:
    CONTENT = "Hay un nuevo candidato para la posicion {} de tu equipo {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata
        position = metadata.get("position")
        position_title = position.get("title")
        team_name = position.get("team").get("name")

        notification.content = NewTeamCandidateContent.CONTENT.format(
            position_title, team_name
        )
