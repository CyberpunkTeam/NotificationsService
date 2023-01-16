class AbandonedProjectContent:
    CONTENT = "El equipo {} ha abandonado el proyecto {}"
    CONTENT_REQUEST = "La solicitud de abandono al proyecto {} fue {}"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        team_name = metadata.get("team").get("name")
        project_name = metadata.get("project").get("name")
        response = "aceptada" if metadata.get("response") == "ACCEPTED" else "rechazada"
        request_id = metadata.get("request_id")
        if request_id is not None:
            notification.content = AbandonedProjectContent.CONTENT.format(
                project_name, response
            )
        else:
            notification.content = AbandonedProjectContent.CONTENT.format(
                team_name, project_name
            )
