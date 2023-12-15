from sqlalchemy.orm import Session

from ..models.Dicto import Dict, DictUnit
from ..schemas import PostCreateDictParams, ResponseCreatedDict

def CreateDict(db: Session, params):

    dict = Dict(name=params['name'])
    
    print(dict)
    print(type(dict))
    db.add(dict)
    db.commit()
    db.refresh(dict)
    
    for key, value in params['dict_unit'].items():
        dict_unit = DictUnit(dict_id=dict.id, key=key, value=value)
        db.add(dict_unit)
        db.commit()
        db.refresh(dict_unit)

    

    return dict

def all_dict(db: Session):
    dicts = db.query(Dict).all()
    print(dicts)
    print(type(dicts))
    
    return dicts


def get_dict_by_id(db: Session, id: int):
    return db.query(Dict).filter(Dict.id == id).first()

