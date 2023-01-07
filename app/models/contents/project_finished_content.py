class ProjectFinishedContent:
    CONTENT = "El proyecto {} ha finalizado"

    @staticmethod
    def complete(notification):
        metadata = notification.metadata

        project_name = metadata.get("project").get("name")

        notification.content = ProjectFinishedContent.CONTENT.format(project_name)
