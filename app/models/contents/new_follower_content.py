class NewFollowerContent:
    CONTENT = "{} has started following you"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata
        follower_name = metadata.get("follower_name")

        notification.content = NewFollowerContent.CONTENT.format(follower_name)
