class TeamPostulationResponseContent:

    CONTENT = "Your postulation for {} project was {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata
        responses = {"ACCEPTED": "accepted", "REJECTED": "rejected"}
        response = responses[metadata.get("response")]
        project_name = metadata.get("project").get("name")

        notification.content = TeamPostulationResponseContent.CONTENT.format(
            project_name, response
        )
