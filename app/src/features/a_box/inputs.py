import strawberry
from typing import List, Optional

@strawberry.input
class InstanceInput:
    class_name: str
    properties: Optional[List[str]] = None  # You may want Dict[str, Any], but GraphQL prefers List or custom types
    constraints: Optional[List[str]] = None

@strawberry.input
class RelationInput:
    subject: str
    predicate: str
    object: str
    constraints: Optional[List[str]] = None
