from app.models.contents.abandoned_project_content import AbandonedProjectContent
from app.models.contents.new_team_member_content import NewTeamMemberContent
from app.models.contents.project_abandons_request_content import (
    ProjectAbandonsRequestContent,
)
from app.models.contents.project_finished_content import ProjectFinishedContent
from app.models.contents.project_finished_request_content import (
    ProjectFinishedRequestContent,
)

from app.models.contents.team_invitation_content import TeamInvitationContent
from app.models.contents.team_postulation_content import TeamPostulationContent
from app.models.contents.team_postulation_response_content import (
    TeamPostulationResponseContent,
)
from app.models.contents.team_review_content import TeamReviewContent


class Contents:
    COMPLETERS = {
        "TEAM_INVITATION": TeamInvitationContent,
        "TEAM_POSTULATION": TeamPostulationContent,
        "TEAM_POSTULATION_RESPONSE": TeamPostulationResponseContent,
        "PROJECT_FINISHED": ProjectFinishedContent,
        "PROJECT_FINISHED_REQUEST": ProjectFinishedRequestContent,
        "ABANDONED_PROJECT": AbandonedProjectContent,
        "PROJECT_ABANDONS_REQUEST": ProjectAbandonsRequestContent,
        "NEW_TEAM_MEMBERS": NewTeamMemberContent,
        "TEAM_REVIEW": TeamReviewContent,
    }

    @staticmethod
    def complete(notification):
        notification_type = notification.notification_type

        if notification_type in Contents.COMPLETERS:
            completer = Contents.COMPLETERS.get(notification_type)
            completer.complete(notification)
