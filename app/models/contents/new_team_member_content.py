class NewTeamMemberContent:
    CONTENT = "{} es nuevo miembro del equipo {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        team_name = metadata.get("team").get("name")
        user_name = metadata.get("user").get("name")

        notification.content = NewTeamMemberContent.CONTENT.format(user_name, team_name)
