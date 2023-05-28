class BlockerManager:
    CONTENT_BLOCK = "Your {} has been blocked"
    CONTENT_UNBLOCK = "Your {} has been unblocked"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata
        name = metadata.get("name")
        entity = notification.notification_type

        if entity == "TEAM_BLOCKED":
            notification.content = BlockerManager.CONTENT_BLOCK.format(f"team {name}")
        elif entity == "PROJECT_BLOCKED":
            notification.content = BlockerManager.CONTENT_BLOCK.format(
                f"project {name}"
            )
        elif entity == "CONTENT_BLOCKED":
            notification.content = BlockerManager.CONTENT_BLOCK.format(
                f"content {name}"
            )
        elif entity == "TEAM_UNBLOCKED":
            notification.content = BlockerManager.CONTENT_UNBLOCK.format(f"team {name}")
        elif entity == "PROJECT_UNBLOCKED":
            notification.content = BlockerManager.CONTENT_UNBLOCK.format(
                f"project {name}"
            )
        elif entity == "CONTENT_UNBLOCKED":
            notification.content = BlockerManager.CONTENT_UNBLOCK.format(
                f"content {name}"
            )
        elif entity == "TEAM_PROJECT_BLOCKED":
            message = BlockerManager.CONTENT_BLOCK.format(f"project {name}")

            notification.content = message.replace("Your", "The")
        elif entity == "TEAM_PROJECT_UNBLOCKED":
            message = BlockerManager.CONTENT_UNBLOCK.format(f"project {name}")

            notification.content = message.replace("Your", "The")
