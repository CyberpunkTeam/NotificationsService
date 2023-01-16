class ProjectFinishedContent:
    CONTENT = "La solicitud de finalizacion del proyecto {} fue {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        project_name = metadata.get("project").get("name")
        response = "aceptada" if metadata.get("response") == "ACCEPTED" else "rechazada"

        notification.content = ProjectFinishedContent.CONTENT.format(
            project_name, response
        )
