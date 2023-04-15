class TeamMemberInternalRecommendation:
    CONTENT = "{} suggests inviting {} to {} team"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        member_name = metadata.get("member").get("name")
        user_recommendation_name = metadata.get("user").get("name")
        team_name = metadata.get("team").get("name")

        notification.content = TeamMemberInternalRecommendation.CONTENT.format(
            member_name, user_recommendation_name, team_name
        )
