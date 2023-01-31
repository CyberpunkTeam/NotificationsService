class AbandonedProjectContent:
    CONTENT = "The team {} abandoned {} project"
    CONTENT_REQUEST = "{} project abandonment request was {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        team_name = metadata.get("team").get("name")
        project_name = metadata.get("project").get("name")
        response = "accepted" if metadata.get("response") == "ACCEPTED" else "rejected"
        request_id = metadata.get("request_id")
        if request_id is not None:
            notification.content = AbandonedProjectContent.CONTENT_REQUEST.format(
                project_name, response
            )
        else:
            notification.content = AbandonedProjectContent.CONTENT.format(
                team_name, project_name
            )
