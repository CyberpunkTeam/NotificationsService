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
        "TEAM_MEMBER_INTERNAL_RECOMMENDATION",
        "TEAM_PROJECT_INTERNAL_RECOMMENDATION",
        "NEW_FOLLOWER",
        "TEAM_BLOCKED",
        "PROJECT_BLOCKED",
        "CONTENT_BLOCKED",
        "TEAM_UNBLOCKED",
        "PROJECT_UNBLOCKED",
        "CONTENT_UNBLOCKED",
        "TEAM_PROJECT_BLOCKED",
        "TEAM_PROJECT_UNBLOCKED",
    ]

    @staticmethod
    def is_valid_type(notification_type):
        return notification_type in NotificationTypes.TYPES
