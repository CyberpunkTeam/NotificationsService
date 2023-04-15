class TeamProjectInternalRecommendation:
    CONTENT = "{} suggests to postule our team {} to {} project"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        member_name = metadata.get("member").get("name")
        project_name = metadata.get("project").get("name")
        team_name = metadata.get("team").get("name")

        notification.content = TeamProjectInternalRecommendation.CONTENT.format(
            member_name, team_name, project_name
        )
