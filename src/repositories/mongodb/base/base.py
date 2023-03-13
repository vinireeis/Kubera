from abc import abstractmethod

from src.infrastructures.mongodb.infrastructure import MongoDBInfrastructure


class MongoDbBaseRepository:
    infra = MongoDBInfrastructure

    @classmethod
    @abstractmethod
    async def _get_collection(cls):
        pass
