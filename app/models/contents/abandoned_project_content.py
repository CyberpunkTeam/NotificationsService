class AbandonedProjectContent:
    CONTENT = "{} ha abandonado el proyecto {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        team_name = metadata.get("team").get("name")
        project_name = metadata.get("project").get("name")

        notification.content = AbandonedProjectContent.CONTENT.format(
            team_name, project_name
        )
