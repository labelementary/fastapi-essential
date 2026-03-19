from sqlalchemy import Column, Integer, String

from src.configs.model import Base


# Class to Handle User Model
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
