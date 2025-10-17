from app.src.features.template.types import JinjaTemplateType

def template_to_type(template_doc):
    return JinjaTemplateType(
        name=template_doc["name"],
        content=template_doc["content"],
        description=template_doc.get("description")
    )
