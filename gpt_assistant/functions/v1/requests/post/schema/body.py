from pydantic import BaseModel


class RequestBody(BaseModel):
    """Request body for the service"""

    request_description: str
