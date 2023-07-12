from typing import Any, Dict

from pydantic import BaseModel


class State(BaseModel):
    """State for the service"""

    entity_id: str
    state: str
    attributes: Dict[str, Any]
    last_changed: str
