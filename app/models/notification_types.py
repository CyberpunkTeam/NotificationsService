class NotificationTypes:
    TYPES = [
        "TEAM_INVITATION",
        "TEAM_POSTULATION",
        "TEAM_POSTULATION_RESPONSE",
        "PROJECT_FINISHED",
        "PROJECT_FINISHED_REQUEST",
        "ABANDONED_PROJECT",
        "PROJECT_ABANDONS_REQUEST",
        "NEW_TEAM_MEMBERS",
        "TEAM_REVIEW",
        "NEW_TEAM_CANDIDATE",
        "TEAM_POSITION_ACCEPTED",
        "PROJECT_INVITATION",
        "POSITION_INVITATION",
        "NEW_TEMPORAL_TEAM",
    ]

    @staticmethod
    def is_valid_type(notification_type):
        return notification_type in NotificationTypes.TYPES
