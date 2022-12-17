from fastapi import HTTPException

from app.models.contents import Contents
from app.models.exceptions.teams_service_error import TeamsServiceError
from app.models.exceptions.users_service_error import UsersServiceError
from app.models.notification_types import NotificationTypes
from app.models.notifications import Notifications


class NotificationsController:
    @staticmethod
    def post(repository, notification: Notifications):
        try:
            if not NotificationTypes.is_valid_type(notification.notification_type):
                raise HTTPException(
                    status_code=400, detail="Invalid type of notification"
                )
            print("el tipo de noficacion es valido")
            Contents.complete(notification)
            print("termino de completar el contenido")
            ok = repository.insert(notification)
            if not ok:
                raise HTTPException(status_code=500, detail="Error saving")
            print("termino de insertar en el repositorio")
            return notification
        except UsersServiceError:
            raise HTTPException(
                status_code=500, detail="Error to get sender information"
            )
        except TeamsServiceError:
            raise HTTPException(status_code=500, detail="Error to get team information")
        except Exception as e:
            raise e

    @staticmethod
    def get(repository, sender_id):
        result = repository.get(sender_id)
        return result
