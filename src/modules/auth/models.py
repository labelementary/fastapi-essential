# Models, Define your models here
from sqlalchemy import Column, Integer, String

from configs.model import Base


# User Model
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
