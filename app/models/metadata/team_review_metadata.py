class TeamReviewMetadata:
    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        pid = metadata.get("project").get("pid")

        notification.metadata = {"pid": pid}
