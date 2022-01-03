from pydantic.main import BaseModel
from typing import List, Dict


class SuccessResponse(BaseModel):
    '''
    API 요청 성공에 대한 기본적인 인터페이스

    status_code: 200으로 고정
    msg: 응답 또는 요청 성공
    data: API 데이터 반환값
    '''

    status_code: int = 200
    msg: str = '응답 성공'
    data: Dict = {}


class Writer(BaseModel):
    '''
    작가 데이터

    writer_name: 작가 닉네임
    writer_id: 작가 식별자(카카오 계정에서 넘어오는 식별자)
    '''

    writer_name: str = ''
    writer_id: str = ''


class Contents(BaseModel):
    '''
    작품 데이터

    contents_id: 작품 식별자
    title: 작품 제목
    thumbnail: 썸네일
    introduction: 소개글
    writer: 작가 정보
    language: 쓰여진 언어
    is_translate: 번역 여부
    original_id: 원작 식별자
    '''

    contents_id: int = 0
    title: str = ''
    thumbnail: str = ''
    introduction: str = ''
    writer: Writer = {}
    language: str = '한국어'
    is_translate: bool = False
    original_id: int = -1


class MainContents(BaseModel):
    '''
    메인 페이지에서 보여지는 컨텐츠 데이터

    main_contents_list: 작품 리스트(작성일자 기준 내림차순 정렬)
    '''

    main_contents_list: List[Contents] = []


class MainContentsData(SuccessResponse):
    data: MainContents = {}


class FeedContents(Writer):
    '''
    피드 페이지에서 보여지는 컨텐츠 데이터

    feed_contents_list: 작품 리스트(작성일자 기준 내림차순 정렬)
    '''
    feed_contents_list: List[Contents] = []


class FeedContentsData(SuccessResponse):
    data: FeedContents = {}


class MainWriters(BaseModel):
    '''
    메인 페이지에서 보여지는 작가 데이터

    main_writer_list: 작가 리스트(작품 등록수 기준 내림차순 정렬)
    '''

    main_writer_list: List[Writer]


class MainWritersData(SuccessResponse):
    data: MainWriters = {}


class ReadingContents(Contents):
    '''
    글읽기 페이지에서 보여지는 작품 데이터

    Contents 상속
    contents: 작품 내용
    translated_contents_list: 번역본 작품 리스트(작성일자 기준 내림차순 정렬)
    '''

    contents: str = ''
    translated_contents_list: List[Contents] = []


class ReadingContentsData(SuccessResponse):
    data: ReadingContents = {}


class TranslatingContents(Contents):
    '''
    번역하기 페이지에서 보여지는 원작 데이터

    Contents 상속
    contents: 작품 내용
    '''

    contents: str = ''


class TranslatingContentsData(SuccessResponse):
    data: TranslatingContents = {}


class WritingContents(BaseModel):
    '''
    작품 등록할 때 사용하는 API 입력 데이터 인터페이스

    title: 제목
    thumbnail: 썸네일
    introduction: 소개글
    contents: 내용
    writer_id: 작가 식별자
    language: 언어
    is_translate: 번역본 여부
    original_id: 원작 식별자 (번역이 아닌 경우 -1)
    '''

    title: str = ''
    thumbnail: str = ''
    introduction: str = ''
    contents: str = ''
    writer_id: str = ''
    language: str = '한국어'
    is_translate: bool = False
    original_id: int = -1


class NameRegistration(BaseModel):
    '''
    필명 등록 페이지에서 사용하는 API 데이터 입력 인터페이스

    name: 필명
    '''

    name: str = ''