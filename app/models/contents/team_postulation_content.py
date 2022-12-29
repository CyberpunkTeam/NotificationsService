class TeamPostulationContent:
    CONTENT = "{} se postulo a tu projecto {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        team_name = metadata.get("team").get("name")
        project_name = metadata.get("project").get("name")

        notification.content = TeamPostulationContent.CONTENT.format(
            team_name, project_name
        )
