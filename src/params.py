from pydantic import BaseModel

class PostTradParams(BaseModel):
    word: str
    dictionnary: str
