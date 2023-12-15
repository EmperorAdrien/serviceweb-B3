from pydantic import BaseModel


# on utilise pas (ancienne version)
class ResponseGetReturnWord(BaseModel):
    return_word: str

class ResponsePostReturnText(BaseModel):
    text: str
    return_text: str

class PostReturnTextParams(BaseModel):
    text: str