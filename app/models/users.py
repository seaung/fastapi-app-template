from sqlalchemy import Column, Integer, String
from app.configs.databases import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True, index=True, nullable=False)
    password = Column(String(128), nullable=False)
