from app.src.features.mongo_db.db import get_m2t_collection
from app.src.features.model2text.inputs import ModelToTextInput
import strawberry

@strawberry.type
class Model2TextMutation:
    @strawberry.mutation
    async def add_model2text(self, model2text_input: ModelToTextInput) -> bool:
        result = await get_m2t_collection().insert_one(model2text_input.__dict__)
        return result.acknowledged

    @strawberry.mutation
    async def delete_model2text(self, id: str) -> bool:
        result = await get_m2t_collection().delete_one({"_id": id})
        return result.deleted_count > 0
