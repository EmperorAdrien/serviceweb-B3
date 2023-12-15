from pydantic import BaseModel
from sqlalchemy import DateTime
from typing import Optional, List
from datetime import datetime
from sqlalchemy.sql.sqltypes import JSON

# une ligne de dictionnaire
class PostCreateDictUnitParams(BaseModel):
    key: str
    value: str

    class Config:
        orm_mode = True


# un dictionnaire (entier, composé de lignes)
class PostCreateDictParams(BaseModel):
    name: str
    dict_units: List[PostCreateDictUnitParams]

    
    class Config:
        orm_mode = True






#response création de dictionnaire
class ResponseCreatedDict(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True

#récuperer les infos d'un dictionnaire en bdd
class ResponseGetDict(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True
    
#récuperer tout les dictionnaires (une liste de dict)
class ResponseGetAllDict(BaseModel):
    dicts : List[ResponseGetDict]
    class Config:
        orm_mode = True


#récupérer le mot traduit
class ResponseGetTranslatedWord(BaseModel):
    translatedWord: str
    class Config:
        orm_mode = True

#post pour traduir un mot (clé+ id dictionnaire)
class PostTranslateWordParams(BaseModel):
    word: str
    id: int
    class Config:
        orm_mode = True