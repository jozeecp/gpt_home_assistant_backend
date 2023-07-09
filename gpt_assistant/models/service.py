from typing import Any, Dict, Optional

from pydantic import BaseModel


class Target(BaseModel):
    """Target for the service"""

    entity: Dict[str, Any]


class Field(BaseModel):
    """Field for the service"""

    name: str
    description: str
    required: bool
    example: Any
    selector: Optional[Dict[str, Any]]


class Service(BaseModel):
    name: str
    description: str
    fields: Optional[Dict[str, Field]]


class Domain(BaseModel):
    domain: str
    services: Optional[Dict[str, Service]]
