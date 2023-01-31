class NewTeamMemberContent:
    CONTENT = "{} is now a member of {} team"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        team_name = metadata.get("team").get("name")
        user_name = metadata.get("user").get("name")

        notification.content = NewTeamMemberContent.CONTENT.format(user_name, team_name)
