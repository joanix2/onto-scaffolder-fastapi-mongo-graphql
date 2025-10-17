from app.src.features.mongo_db.db import get_abox_collection
from app.src.features.a_box.inputs import InstanceInput, RelationInput
import strawberry

@strawberry.type
class ABoxMutation:
    @strawberry.mutation
    async def add_instance_to_abox(self, abox_id: str, instance_input: InstanceInput) -> bool:
        result = await get_abox_collection().update_one(
            {"_id": abox_id},
            {"$push": {"instances": instance_input.__dict__}}
        )
        return result.modified_count > 0

    @strawberry.mutation
    async def add_relation_to_abox(self, abox_id: str, relation_input: RelationInput) -> bool:
        result = await get_abox_collection().update_one(
            {"_id": abox_id},
            {"$push": {"relations": relation_input.__dict__}}
        )
        return result.modified_count > 0
