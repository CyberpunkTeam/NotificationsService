from app.models.metadata.team_review_metadata import TeamReviewMetadata


class Metadata:
    COMPLETERS = {
        "TEAM_REVIEW": TeamReviewMetadata,
    }

    @staticmethod
    def complete(notification):
        notification_type = notification.notification_type

        if notification_type in Metadata.COMPLETERS:
            completer = Metadata.COMPLETERS.get(notification_type)
            completer.complete(notification)
        else:
            notification.metadata = None
