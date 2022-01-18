
from sqlalchemy import (
    Column,
    String,
)

from app.database.conn import Base


class Users(Base):
    __tablename__ = "Users"
    user_id = Column(String(length=100), primary_key=True, nullable=False)
    user_name = Column(String(length=20), nullable=False)
