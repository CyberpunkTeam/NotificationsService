class NotificationTypes:
    TYPES = ["TEAM_INVITATION"]

    @staticmethod
    def is_valid_type(notification_type):
        return notification_type in NotificationTypes.TYPES
