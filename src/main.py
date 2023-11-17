from fastapi import FastAPI

from .params import PostReturnTextParams
from .response import ResponseGetReturnWord, ResponsePostReturnText
from .conf.database import Base, SessionLocal, engine
from .repositories.ReturnText import create_return_text

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def index():
    return {"msg": "Hello World !"}

@app.get("/return/{word}", response_model=ResponseGetReturnWord)
def return_word(word: str):
    create_return_text(SessionLocal(), {'text': word, 'return_text': "".join(reversed(word))}, method='GET')

    return {
        "return_word": "".join(reversed(word))
    }

@app.post("/return-text", response_model=ResponsePostReturnText)
def post_return_text(params: PostReturnTextParams):

    create_return_text(SessionLocal(), {'text': params.text, 'return_text': "".join(reversed(params.text))}, method='POST')

    return {
        "text": params.text,
        "return_text": "".join(reversed(params.text))
    }
