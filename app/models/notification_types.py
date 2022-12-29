class NotificationTypes:
    TYPES = ["TEAM_INVITATION", "TEAM_POSTULATION", "TEAM_POSTULATION_RESPONSE"]

    @staticmethod
    def is_valid_type(notification_type):
        return notification_type in NotificationTypes.TYPES
