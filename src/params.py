from pydantic import BaseModel

class PostReturnTextParams(BaseModel):
    text: str