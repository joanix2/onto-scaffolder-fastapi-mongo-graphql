import strawberry
from typing import Optional

@strawberry.input
class JinjaTemplateInput:
    name: str
    content: str
    description: Optional[str] = None
