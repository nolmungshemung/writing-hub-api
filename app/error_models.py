from pydantic.main import BaseModel
from typing import Dict


class APIExceptionModel(BaseModel):

    msg: str = 'Internal Server Error'
    data: Dict = {}


class NotFoundUserModel(APIExceptionModel):

    msg: str = '해당 유저를 찾을 수 없습니다'
    data: Dict = {}