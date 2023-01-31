class ProjectFinishedContent:
    CONTENT = "{} project finalization request was {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        project_name = metadata.get("project").get("name")
        response = "aceptada" if metadata.get("response") == "ACCEPTED" else "rechazada"

        notification.content = ProjectFinishedContent.CONTENT.format(
            project_name, response
        )
        if metadata.get("response") == "ACCEPTED":
            notification.content += (
                " Haz la review del equipo para finalizar el proyecto."
            )
