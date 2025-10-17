import strawberry
from typing import List, Optional

@strawberry.input
class ClassInput:
    name: str
    description: Optional[str] = None
    constraints: Optional[List[str]] = None

@strawberry.input
class DatatypePropertyInput:
    name: str
    domain: str
    range: str
    constraints: Optional[List[str]] = None

@strawberry.input
class ObjectPropertyInput:
    name: str
    domain: str
    range: str
    constraints: Optional[List[str]] = None
