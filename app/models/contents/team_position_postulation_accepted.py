class TeamPositionAcceptedContent:
    CONTENT = "Se acepto tu postulacion a para la posicion {} del equipo {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata
        position = metadata.get("position")
        position_title = position.get("title")
        team_name = position.get("team").get("name")

        notification.content = TeamPositionAcceptedContent.CONTENT.format(
            position_title, team_name
        )
