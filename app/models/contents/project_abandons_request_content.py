class ProjectAbandonsRequestContent:
    CONTENT = "{}'s project owner requested {} team abandonment"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        team_name = metadata.get("team").get("name")
        project_name = metadata.get("project").get("name")

        notification.content = ProjectAbandonsRequestContent.CONTENT.format(
            project_name, team_name
        )
