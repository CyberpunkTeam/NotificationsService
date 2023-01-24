from app.models.metadata import Metadata
from app.models.notifications import Notifications


def test_get_metadata_for_team_review():
    project_name = "Aliados"
    pid = "12"
    project_body = {
        "pid": pid,
        "name": project_name,
        "technologies": ["python"],
        "project_preferences": ["web"],
        "owner": "1234",
    }
    tid = "1"
    team_name = "Alfa"
    team_body = {
        "name": team_name,
    }

    mid = "1"
    notification = Notifications(
        sender_id=tid,
        receiver_id=mid,
        notification_type="TEAM_REVIEW",
        resource="TEAMS",
        resource_id=tid,
        metadata={"project": project_body, "team": team_body},
    )

    Metadata.complete(notification)

    assert notification.metadata["pid"] == pid
