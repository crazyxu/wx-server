from sqlalchemy import Column, Integer, String
from app import Base

class DisplayImage(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    desc = Column(String(255))
    url = Column(String(255))
    type = Column(Integer)
