import strawberry
from typing import List

@strawberry.type
class TextTransformationType:
    target_path: str
    template_id: str

@strawberry.type
class ClassToTextType:
    model: str
    transformations: List[TextTransformationType]

@strawberry.type
class ModelToTextType:
    id: str
    tbox_id: str
    abox_id: str
    class_mappings: List[ClassToTextType]
