from sqlalchemy.orm import Session

from ..models.ReturnText import ReturnText
from ..response import ResponsePostReturnText

#pas utilisé dans cette version
def create_return_text(db: Session, params: ResponsePostReturnText, method: str):
    db_return_text = ReturnText(
        text = params['text'],
        return_text = params['return_text'],
        method = method
    )

    db.add(db_return_text)
    db.commit()
    db.refresh(db_return_text)

    return db_return_text