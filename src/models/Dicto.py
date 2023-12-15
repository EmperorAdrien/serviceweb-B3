from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship 


from ..conf.database import Base

class DictUnit(Base):
    __tablename__ = "dict_unit"

    id = Column(Integer, primary_key=True, index=True)
    dict_id = Column(Integer, ForeignKey('dict.id'))
    key = Column(String(40))
    value = Column(String(40))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    relationDictUnit = relationship("Dict", back_populates="relationDict")

class Dict(Base):
    __tablename__ = "dict"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String(40))
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    relationDict = relationship("DictUnit", back_populates="relationDictUnit")