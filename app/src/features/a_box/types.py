import strawberry
from typing import List, Optional

@strawberry.type
class InstanceType:
    class_name: str
    properties: Optional[List[str]]  # For GraphQL, use List or custom types
    constraints: Optional[List[str]]

@strawberry.type
class RelationType:
    subject: str
    predicate: str
    object: str
    constraints: Optional[List[str]]

@strawberry.type
class ABoxType:
    id: str
    instances: List[InstanceType]
    relations: List[RelationType]
