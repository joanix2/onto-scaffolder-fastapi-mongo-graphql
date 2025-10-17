import strawberry
from typing import List, Optional

@strawberry.type
class ClassType:
    name: str
    description: Optional[str]
    constraints: Optional[List[str]]

@strawberry.type
class DatatypePropertyType:
    name: str
    domain: str
    range: str
    constraints: Optional[List[str]]

@strawberry.type
class ObjectPropertyType:
    name: str
    domain: str
    range: str
    constraints: Optional[List[str]]

@strawberry.type
class TBoxType:
    id: str
    classes: List[ClassType]
    datatype_properties: List[DatatypePropertyType]
    object_properties: List[ObjectPropertyType]
