from datetime import datetime
from enum import Enum
from typing import List

from pydantic import Field
from pydantic.main import BaseModel
from pydantic.networks import EmailStr, IPvAnyAddress


class UserMe(BaseModel):
    id: int
    email: str = None
    nickname: str = None
    status: str = None
    profile_img: str = None

    class Config:
        orm_mode = True