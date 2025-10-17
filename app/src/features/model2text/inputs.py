import strawberry
from typing import List

@strawberry.input
class TextTransformationInput:
    target_path: str
    template_id: str

@strawberry.input
class ClassToTextInput:
    model: str
    transformations: List[TextTransformationInput]

@strawberry.input
class ModelToTextInput:
    tbox_id: str
    abox_id: str
    class_mappings: List[ClassToTextInput]
