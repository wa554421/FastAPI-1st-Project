from pydantic import BaseModel,Field

class Waleed(BaseModel):
    name: str = Field(..., min_length=1, description="Name is required")
    msg: str = Field(..., min_length=1, description="Message is required")