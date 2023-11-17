from pydantic import BaseModel

class ResponseGetReturnWord(BaseModel):
    return_word: str

class ResponsePostReturnText(BaseModel):
    text: str
    return_text: str