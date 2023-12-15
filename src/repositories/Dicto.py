from sqlalchemy.orm import Session

from ..models.Dicto import Dict, DictUnit
from ..schemas import PostCreateDictParams, ResponseCreatedDict


#pour créer un dictionnaire
def CreateDict(db: Session, params):

    #on créé un objet Dict
    dict = Dict(name=params['name'])
    

    #on ajoute l'objet Dict à la base de données
    db.add(dict)
    db.commit()
    db.refresh(dict)
    
    # on créé un objet DictUnit pour chaque ligne du dictionnaire
    for key, value in params['dict_unit'].items():
        dict_unit = DictUnit(dict_id=dict.id, key=key, value=value)
        db.add(dict_unit)
        db.commit()
        db.refresh(dict_unit)

    
    #on retourne l'objet Dict (au main.py)
    return dict

def all_dict(db: Session):
    dicts = db.query(Dict).all()
    print(dicts)
    print(type(dicts))
    
    return dicts


def get_dict_by_id(db: Session, id: int):
    return db.query(Dict).filter(Dict.id == id).first()

