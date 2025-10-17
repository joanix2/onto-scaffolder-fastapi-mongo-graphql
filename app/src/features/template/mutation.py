from app.src.features.mongo_db.db import get_templates_collection
from app.src.features.template.inputs import JinjaTemplateInput
import strawberry

@strawberry.type
class TemplateMutation:
    @strawberry.mutation
    async def add_template(self, template_input: JinjaTemplateInput) -> bool:
        result = await get_templates_collection().insert_one(template_input.__dict__)
        return result.acknowledged

    @strawberry.mutation
    async def delete_template(self, name: str) -> bool:
        result = await get_templates_collection().delete_one({"name": name})
        return result.deleted_count > 0
