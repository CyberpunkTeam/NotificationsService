class ProjectAbandonsRequestContent:
    CONTENT = "Request of {} team abandonment of {} project"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        team_name = metadata.get("team").get("name")
        project_name = metadata.get("project").get("name")

        notification.content = ProjectAbandonsRequestContent.CONTENT.format(
            team_name, project_name
        )
