from pydantic import BaseModel
from sqlalchemy import DateTime
from typing import Optional, List
from datetime import datetime
from sqlalchemy.sql.sqltypes import JSON


class PostCreateDictUnitParams(BaseModel):
    key: str
    value: str

    class Config:
        orm_mode = True


#params
class PostCreateDictParams(BaseModel):
    name: str
    dict_units: List[PostCreateDictUnitParams]

    
    class Config:
        orm_mode = True






#response
class ResponseCreatedDict(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True

class ResponseGetDict(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True
    
class ResponseGetAllDict(BaseModel):
    dicts : List[ResponseGetDict]
    class Config:
        orm_mode = True


class ResponseGetTranslatedWord(BaseModel):
    translatedWord: str
    class Config:
        orm_mode = True

class PostTranslateWordParams(BaseModel):
    word: str
    id: int
    class Config:
        orm_mode = True