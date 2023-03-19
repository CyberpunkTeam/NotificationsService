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

    def get(self, receiver_id=None, nid=None, sender_id=None, resource_id=None):
        filters = {}

        if receiver_id is not None:
            filters["receiver_id"] = receiver_id

        if nid is not None:
            filters["nid"] = nid

        if sender_id is not None:
            filters["sender_id"] = sender_id

        if resource_id is not None:
            filters["resource_id"] = resource_id

        return self.filter(self.COLLECTION_NAME, filters, output_model=Notifications)

    def insert(self, notification: Notifications):
        return self.save(self.COLLECTION_NAME, notification)

    @staticmethod
    def create_repository(url, database_name):
        return NotificationsRepository(url, database_name)

    def put(self, notification: Notifications):
        return self.update(self.COLLECTION_NAME, "nid", notification.nid, notification)
