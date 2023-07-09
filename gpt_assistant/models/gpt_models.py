import json
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from gpt_assistant.models.gpt_models import Function


class Message(BaseModel):
    """Message for the service"""

    role: str
    content: str


class Property(BaseModel):
    """Property for the service"""

    name: str
    description: Optional[str]
    enum: Optional[List[str]]


class Parameters(BaseModel):
    """Parameter for the service"""

    type: str
    properties: List[Property]
    required: List[str]


class Function(BaseModel):
    """Function for the service"""

    name: str
    description: str
    parameters: Parameters


class BaseRequestBody(BaseModel):
    """Request body for the service"""

    model: str = "gpt-3.5-turbo-0613"
    messages: List[Message]


class FunctionRequestBody(BaseRequestBody):
    """Request body for the function service"""

    functions: List[Function]
    function_call: str = "auto"


class FunctionCall(BaseModel):
    """Function call for the service"""

    name: str
    arguments: str

    @property
    def arguments_dict(self) -> Dict[str, Any]:
        """Get arguments dict"""
        return json.loads(self.arguments)
