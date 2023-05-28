from app.models.contents.abandoned_project_content import AbandonedProjectContent
from app.models.contents.blocker_manager import BlockerManager
from app.models.contents.new_follower_content import NewFollowerContent
from app.models.contents.new_team_candidate_content import NewTeamCandidateContent
from app.models.contents.new_team_member_content import NewTeamMemberContent
from app.models.contents.new_temporal_team_content import NewTemporalTeamContent
from app.models.contents.position_invitation_content import PositionInvitationContent
from app.models.contents.project_abandons_request_content import (
    ProjectAbandonsRequestContent,
)
from app.models.contents.project_finished_content import ProjectFinishedContent
from app.models.contents.project_finished_request_content import (
    ProjectFinishedRequestContent,
)
from app.models.contents.project_invitation_content import ProjectInvitationContent

from app.models.contents.team_invitation_content import TeamInvitationContent
from app.models.contents.team_member_internal_recommendation import (
    TeamMemberInternalRecommendation,
)
from app.models.contents.team_position_postulation_accepted import (
    TeamPositionAcceptedContent,
)
from app.models.contents.team_postulation_content import TeamPostulationContent
from app.models.contents.team_postulation_response_content import (
    TeamPostulationResponseContent,
)
from app.models.contents.team_project_internal_recommendation import (
    TeamProjectInternalRecommendation,
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
        "NEW_TEAM_CANDIDATE": NewTeamCandidateContent,
        "TEAM_POSITION_ACCEPTED": TeamPositionAcceptedContent,
        "PROJECT_INVITATION": ProjectInvitationContent,
        "POSITION_INVITATION": PositionInvitationContent,
        "NEW_TEMPORAL_TEAM": NewTemporalTeamContent,
        "TEAM_MEMBER_INTERNAL_RECOMMENDATION": TeamMemberInternalRecommendation,
        "TEAM_PROJECT_INTERNAL_RECOMMENDATION": TeamProjectInternalRecommendation,
        "NEW_FOLLOWER": NewFollowerContent,
        "TEAM_BLOCKED": BlockerManager,
        "PROJECT_BLOCKED": BlockerManager,
        "CONTENT_BLOCKED": BlockerManager,
        "TEAM_UNBLOCKED": BlockerManager,
        "PROJECT_UNBLOCKED": BlockerManager,
        "CONTENT_UNBLOCKED": BlockerManager,
        "TEAM_PROJECT_BLOCKED": BlockerManager,
        "TEAM_PROJECT_UNBLOCKED": BlockerManager,
    }

    @staticmethod
    def complete(notification):
        notification_type = notification.notification_type

        if notification_type in Contents.COMPLETERS:
            completer = Contents.COMPLETERS.get(notification_type)
            completer.complete(notification)
