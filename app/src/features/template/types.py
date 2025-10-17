import strawberry
from typing import Optional

@strawberry.type
class JinjaTemplateType:
    name: str
    content: str
    description: Optional[str]
