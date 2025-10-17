from app.src.features.mongo_db.db import get_abox_collection
from app.src.features.a_box.resolvers import abox_to_type
from app.src.features.a_box.types import ABoxType
import strawberry
from typing import List, Optional

@strawberry.type
class ABoxQuery:
    @strawberry.field
    async def aboxes(self) -> List[ABoxType]:
        aboxes = await get_abox_collection().find().to_list(100)
        return [abox_to_type(a) for a in aboxes]

    @strawberry.field
    async def abox(self, abox_id: str) -> Optional[ABoxType]:
        abox = await get_abox_collection().find_one({"_id": abox_id})
        if abox:
            return abox_to_type(abox)
        return None
