class ProjectInvitationContent:
    CONTENT = "Your team {} has a postulate invitation to project {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        project_name = metadata.get("project").get("name")
        team_name = metadata.get("team").get("name")

        notification.content = ProjectInvitationContent.CONTENT.format(
            team_name, project_name
        )
