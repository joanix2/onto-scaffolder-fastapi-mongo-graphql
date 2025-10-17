from app.src.features.mongo_db.db import get_templates_collection
from app.src.features.template.resolvers import template_to_type
from app.src.features.template.types import JinjaTemplateType
import strawberry
from typing import List, Optional

@strawberry.type
class TemplateQuery:
    @strawberry.field
    async def templates(self) -> List[JinjaTemplateType]:
        templates = await get_templates_collection().find().to_list(100)
        return [template_to_type(t) for t in templates]

    @strawberry.field
    async def template(self, name: str) -> Optional[JinjaTemplateType]:
        template = await get_templates_collection().find_one({"name": name})
        if template:
            return template_to_type(template)
        return None
