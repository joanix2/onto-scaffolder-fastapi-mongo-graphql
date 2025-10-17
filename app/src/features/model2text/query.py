from app.src.features.mongo_db.db import get_m2t_collection
from app.src.features.model2text.resolvers import model2text_to_type
from app.src.features.model2text.types import ModelToTextType
import strawberry
from typing import List, Optional

@strawberry.type
class Model2TextQuery:
    @strawberry.field
    async def model2texts(self) -> List[ModelToTextType]:
        docs = await get_m2t_collection().find().to_list(100)
        return [model2text_to_type(d) for d in docs]

    @strawberry.field
    async def model2text(self, id: str) -> Optional[ModelToTextType]:
        doc = await get_m2t_collection().find_one({"_id": id})
        if doc:
            return model2text_to_type(doc)
        return None
