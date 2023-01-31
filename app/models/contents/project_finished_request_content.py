class ProjectFinishedRequestContent:
    CONTENT = "Request of {} project finalization"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        project_name = metadata.get("project").get("name")

        notification.content = ProjectFinishedRequestContent.CONTENT.format(
            project_name
        )
