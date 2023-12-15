from fastapi import FastAPI

from .params import PostReturnTextParams
from .response import ResponseGetReturnWord, ResponsePostReturnText
from .schemas import ResponseCreatedDict, PostCreateDictParams, ResponseGetAllDict, ResponseGetDict, ResponseGetTranslatedWord, PostTranslateWordParams
from .conf.database import Base, SessionLocal, engine
from .repositories.ReturnText import create_return_text
from .repositories.Dicto import CreateDict, all_dict, get_dict_by_id
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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

@app.post("/create-dict", response_model=ResponseCreatedDict)
def post_create_dict(params: PostCreateDictParams):
        print("Debug@post_return_text")
        
        dict_unit = {}
        for pair in params.dict_units:
                
                dict_unit[pair.key] = pair.value
        print(dict_unit)
        dict = CreateDict(SessionLocal(), {'name': params.name, 'dict_unit': dict_unit})

        return {
                "name": params.name,
                "id": dict.id,
                "created_at": dict.created_at,
                "updated_at": dict.updated_at
        }

@app.get("/dict/{id}", response_model=ResponseGetDict)
def getDictID(id: int):
    dict = get_dict_by_id(SessionLocal(), id)
    return {
        "id": dict.id,
        "name": dict.name,
        "created_at": dict.created_at,
        "updated_at": dict.updated_at
    }


@app.get("/dict/all",response_model= ResponseGetAllDict)
def get_all_dict():
        dicts = all_dict(SessionLocal())
        return {
                "dicts": dicts
        }

@app.post("/translate", response_model=ResponseGetTranslatedWord)
def PostTranslateWord(params: PostTranslateWordParams):
    dict = get_dict_by_id(SessionLocal(), params.id)
    print(dict)
    dict_unit = dict.relationDict
    print(dict_unit)
    translatedWord = ""
    for letter in params.word.lower():
        for unit in dict_unit:
            if letter == unit.key:
                translatedWord += unit.value
                translatedWord += " "

    return {
        "translatedWord": translatedWord
    }



