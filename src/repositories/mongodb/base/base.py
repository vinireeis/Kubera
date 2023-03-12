# Jormungandr - Onboarding
from src.infrastructures.mongodb.infrastructure import MongoDBInfrastructure

# Standards
from abc import abstractmethod


class MongoDbBaseRepository:
    infra = MongoDBInfrastructure

    @classmethod
    @abstractmethod
    async def _get_collection(cls):
        pass
