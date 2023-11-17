from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from ..conf.database import Base

class ReturnText(Base):
    __tablename__ = "return_text"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(40))
    return_text = Column(String(40))
    method = Column(String(10))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())