from app.src.features.mongo_db.db import get_tbox_collection
from app.src.features.t_box.resolvers import tbox_to_type
from app.src.features.t_box.types import TBoxType
import strawberry
from typing import List, Optional

@strawberry.type
class TBoxQuery:
    @strawberry.field
    async def tboxes(self) -> List[TBoxType]:
        tboxes = await get_tbox_collection().find().to_list(100)
        return [tbox_to_type(t) for t in tboxes]

    @strawberry.field
    async def tbox(self, tbox_id: str) -> Optional[TBoxType]:
        tbox = await get_tbox_collection().find_one({"_id": tbox_id})
        if tbox:
            return tbox_to_type(tbox)
        return None
