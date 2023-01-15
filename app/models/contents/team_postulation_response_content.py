class TeamPostulationResponseContent:
    CONTENT = "Se {} tu postulación al proyecto {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata
        responses = {"ACCEPTED": "acepto", "REJECTED": "rechazo"}
        response = responses[metadata.get("response")]
        project_name = metadata.get("project").get("name")

        notification.content = TeamPostulationResponseContent.CONTENT.format(
            response, project_name
        )
