from pydantic.main import BaseModel
from typing import Dict
from app.models import WritingContents


class APIExceptionModel(BaseModel):
    '''
    error response schema
    '''

    msg: str = 'Internal Server Error'
    data: Dict = {}


class NotFoundUserModel(APIExceptionModel):
    '''
    error response schema
    해당 식별자의 유저가 없는 경우
    '''

    msg: str = '해당 유저를 찾을 수 없습니다'
    data: Dict = {}


class NotProperWritingContents(WritingContents):
    '''
    error response schema
    If WritingContents values were not proper
    '''

    msg: str = 'WritingContents were not proper'
    data: Dict = {}