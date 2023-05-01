class NewFollowerContent:
    CONTENT = "{} has started following you"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata
        follower_name = metadata.get("follower_name")
        following_type = metadata.get("following_type")
        following_team_name = metadata.get("following_team_name")
        notification.content = NewFollowerContent.CONTENT.format(follower_name)

        if following_type == "user":
            notification.content = NewFollowerContent.CONTENT.format(follower_name)

        if following_type == "team":
            notification.content = NewFollowerContent.CONTENT.replace(
                "you", "your team {}"
            ).format(follower_name, following_team_name)
