from pydantic.main import BaseModel
from typing import List

class Writer(BaseModel):
    writer_name: str = ''
    writer_id: str = ''

class Contents(BaseModel):
    contents_id: int = 0
    title: str = ''
    thumbnail: str = ''
    Introduction: str = ''
    writer: Writer = {}
    language: str = 'KR'
    is_translate: bool = False
    original_id: int = -1

class MainContents(BaseModel):
    main_contents_list: List[Contents] = []

class FeedContents(Writer):
    feed_contents_list: List[Contents] = []

class MainWriters(BaseModel):
    main_writer_list: List[Writer]

class ReadingContents(Contents):
    contents: str = ''
    translated_contents_list: List[Contents] = []

class TranslatingContents(Contents):
    contents: str = ''