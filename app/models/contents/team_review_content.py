class TeamReviewContent:
    CONTENT = "Se finalizo el proyecto {}, haz la review de tu equipo {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        project_name = metadata.get("project").get("name")
        team_name = metadata.get("team").get("name")

        notification.content = TeamReviewContent.CONTENT.format(project_name, team_name)
