
from sqlalchemy import (
    Column,
    String,
)

from app.database.conn import Base


class Users(Base):
    __tablename__ = "users"
    writer_id = Column(String(length=255), nullable=False)