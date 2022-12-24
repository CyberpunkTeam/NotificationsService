from cpunk_mongo.db import DataBase

from app.models.notifications import Notifications


class NotificationsRepository(DataBase):
    COLLECTION_NAME = "notifications"

    def __init__(self, url, db_name):
        if db_name == "test":
            import mongomock

            self.db = mongomock.MongoClient().db
        else:
            super().__init__(url, db_name)

    def get(self, receiver_id=None, nid=None):
        if receiver_id is None and nid is None:
            return self.filter(self.COLLECTION_NAME, {}, output_model=Notifications)
        elif nid is not None:
            return self.find_by(
                self.COLLECTION_NAME, "nid", nid, output_model=Notifications
            )
        else:
            return self.find_by(
                self.COLLECTION_NAME,
                "receiver_id",
                receiver_id,
                output_model=Notifications,
            )

    def insert(self, notification: Notifications):
        return self.save(self.COLLECTION_NAME, notification)

    @staticmethod
    def create_repository(url, database_name):
        return NotificationsRepository(url, database_name)

    def put(self, notification: Notifications):
        return self.update(self.COLLECTION_NAME, "nid", notification.nid, notification)
