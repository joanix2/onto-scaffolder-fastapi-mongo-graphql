from app.src.features.mongo_db.db import get_tbox_collection
from app.src.features.t_box.inputs import ClassInput, DatatypePropertyInput, ObjectPropertyInput
import strawberry

@strawberry.type
class TBoxMutation:
    @strawberry.mutation
    async def add_class_to_tbox(self, tbox_id: str, class_input: ClassInput) -> bool:
        result = await get_tbox_collection().update_one(
            {"_id": tbox_id},
            {"$push": {"classes": class_input.__dict__}}
        )
        return result.modified_count > 0

    @strawberry.mutation
    async def add_datatype_property_to_tbox(self, tbox_id: str, prop_input: DatatypePropertyInput) -> bool:
        result = await get_tbox_collection().update_one(
            {"_id": tbox_id},
            {"$push": {"datatype_properties": prop_input.__dict__}}
        )
        return result.modified_count > 0

    @strawberry.mutation
    async def add_object_property_to_tbox(self, tbox_id: str, prop_input: ObjectPropertyInput) -> bool:
        result = await get_tbox_collection().update_one(
            {"_id": tbox_id},
            {"$push": {"object_properties": prop_input.__dict__}}
        )
        return result.modified_count > 0