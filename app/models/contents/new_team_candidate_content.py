class NewTeamCandidateContent:
    CONTENT = "Hay un nuevo candidato para la posicion {} de tu equipo {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        position_title = metadata.get("position").get("title")
        team_name = metadata.get("team").get("name")

        notification.content = NewTeamCandidateContent.CONTENT.format(
            position_title, team_name
        )
