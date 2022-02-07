from fastapi import APIRouter, Depends, status
from app.models import Contents, Writer, MainContents, MainWriters, ReadingContents, TranslatingContents, FeedContents, \
    WritingContents, MainContentsData, MainWritersData, ReadingContentsData, TranslatingContentsData, FeedContentsData, \
    SuccessResponse, IncreaseViews, EditingContents

from app.database.conn import db
from app.database.schema import Contents
from sqlalchemy.orm import Session

from app.errors.exceptions import NotProperWritingContentsEx

from typing import Optional

router = APIRouter(prefix='/services')


@router.get(path='/main_contents', response_model=MainContentsData)
async def main_contents(
        start: int = 0,
        count: int = 10,
        base_time: int = 0,
        keyword: Optional[str] = None
) -> MainContentsData:
    '''
    메인 페이지에서 표시되는 작품 데이터를 반환하는 API

    :param start: 가져오려는 데이터 시작점:
    :param count: 가져오려는 데이터 개수:
    :param base_time: 기준 시점, timestamp로 소수점 없이 입력(시간순서대로 정렬된 데이터가 새로 입력되는 데이터와 관계없이 중복되지 않기 위해 필요):
    :param keyword: 검색어:
    :return MainContentsData:
    '''

    return MainContentsData(
        msg='응답 성공',
        data=MainContents(
            main_contents_list=[
                Contents(
                    contents_id=20,
                    title='장발장의 신나는 하루',
                    thumbnail='그때 내가 왜그랬는지 도무지 이해할 수 없네',
                    introduction='장발장의 하루를 담은 이야기',
                    writer=Writer(
                        writer_name='장발장',
                        writer_id='10asff'
                    ),
                    language='영어',
                    is_translate=True,
                    original_id=24,
                    views=0,
                    translation_num=0
                ),
                Contents(
                    contents_id=21,
                    title='장발장의 신나는 하루2',
                    thumbnail='어제 내가 왜그랬는지 도무지 이해할 수 없네',
                    introduction='장발장의 어제를 담은 이야기',
                    writer=Writer(
                        writer_name='어제의 나',
                        writer_id='10asfg'
                    ),
                    language='한국어',
                    is_translate=False,
                    original_id=-1,
                    views=0,
                    translation_num=0
                )
            ]
        )
    )


@router.get(path='/main_writers', response_model=MainWritersData)
async def main_writers(
        start: int = 0,
        count: int = 10,
        base_time: int = 0,
        keyword: Optional[str] = None
) -> MainWritersData:
    '''
    메인 페이지에서 표시되는 작가 데이터를 반환하는 API
    :param start: 가져오려는 데이터 시작점:
    :param count: 가져오려는 데이터 개수:
    :param base_time: 기준 시점, timestamp로 소수점 없이 입력(시간순서대로 정렬된 데이터가 새로 입력되는 데이터와 관계없이 중복되지 않기 위해 필요):
    :param keyword: 검색어:
    :return MainWritersData:
    '''
    return MainWritersData(
        msg='응답 성공',
        data=MainWriters(
            main_writer_list=[
                Writer(
                    writer_name='장발장',
                    writer_id='10asff'
                ),
                Writer(
                    writer_name='어제의 나',
                    writer_id='10asfg'
                )
            ]
        )
    )


@router.get(path='/reading_contents', response_model=ReadingContentsData)
async def reading_contents(contents_id: int) -> ReadingContentsData:
    '''
    글읽기 페이지에서 표시되는 작품 데이터를 반환하는 API

    :param contents_id: 작품 식별자:
    :return ReadingContentsData:
    '''
    return ReadingContentsData(
        msg='응답 성공',
        data=ReadingContents(
            contents_id=21,
            title='장발장의 신나는 하루2',
            thumbnail='어제 내가 왜그랬는지 도무지 이해할 수 없네',
            introduction='장발장의 어제를 담은 이야기',
            writer=Writer(
                writer_name='어제의 나',
                writer_id='10asfg'
            ),
            language='한국어',
            is_translate=False,
            original_id=-1,
            views=0,
            translation_num=0,
            contents='그때 내가 왜그랬는지 도무지 이해할 수 없네\n 배고픔이 사람을 이렇게 만들줄이야',
            created_date=1641495600,
            translated_contents_list=[
                Contents(
                    contents_id=43,
                    title='Fun Day',
                    thumbnail='I cant understand why I did that back then.',
                    introduction='The Story of a Day',
                    writer=Writer(
                        writer_name='장발장',
                        writer_id='10asff'
                    ),
                    language='영어',
                    is_translate=True,
                    original_id=21,
                    views=0,
                    translation_num=0
                ),
                Contents(
                    contents_id=43,
                    title='Fun Day',
                    thumbnail='I cant understand why I did that back then.',
                    introduction='The Story of a Day',
                    writer=Writer(
                        writer_name='장발장',
                        writer_id='10asff'
                    ),
                    language='영어',
                    is_translate=True,
                    original_id=21,
                    views=0,
                    translation_num=0
                )
            ]
        )
    )


@router.get(path='/translating_contents', response_model=TranslatingContentsData)
async def translating_contents(contents_id: int) -> TranslatingContentsData:
    '''
    번역 페이지에서 표시되는 데이터를 반환하는 API

    :param contents_id: 작품 식별자:
    :return TranslatingContentsData:
    '''
    return TranslatingContentsData(
        msg='응답 성공',
        data=TranslatingContents(
            contents_id=21,
            title='장발장의 신나는 하루2',
            thumbnail='어제 내가 왜그랬는지 도무지 이해할 수 없네',
            introduction='장발장의 어제를 담은 이야기',
            writer=Writer(
                writer_name='어제의 나',
                writer_id='10asfg'
            ),
            language='한국어',
            is_translate=False,
            original_id=-1,
            views=0,
            translation_num=0,
            contents='그때 내가 왜그랬는지 도무지 이해할 수 없네\n 배고픔이 사람을 이렇게 만들줄이야'
        )
    )


@router.get(path='/feed_contents', response_model=FeedContentsData)
async def feed_contents(writer_id: str) -> FeedContentsData:
    '''
    피드 페이지에서 표시되는 데이터를 반환하는 API

    :param writer_id: 작가 식별자:
    :return FeedContentsData:
    '''
    return FeedContentsData(
        msg='응답 성공',
        data=FeedContents(
            writer=Writer(
                writer_name='장발장',
                writer_id='10asff'
            ),
            feed_contents_list=[
                Contents(
                    contents_id=20,
                    title='장발장의 신나는 하루',
                    thumbnail='그때 내가 왜그랬는지 도무지 이해할 수 없네',
                    introduction='장발장의 하루를 담은 이야기',
                    writer=Writer(
                        writer_name='장발장',
                        writer_id='10asff'
                    ),
                    language='영어',
                    is_translate=True,
                    original_id=24,
                    views=0,
                    translation_num=0,
                ),
                Contents(
                    contents_id=21,
                    title='장발장의 신나는 하루2',
                    thumbnail='어제 내가 왜그랬는지 도무지 이해할 수 없네',
                    introduction='장발장의 어제를 담은 이야기',
                    writer=Writer(
                        writer_name='장발장',
                        writer_id='10asff'
                    ),
                    language='한국어',
                    is_translate=False,
                    original_id=-1,
                    views=0,
                    translation_num=0,
                )
            ]
        )
    )


@router.post(
    path='/writing_contents',
    response_model=SuccessResponse,
    status_code=status.HTTP_201_CREATED,
)
async def writing_contents(data: WritingContents, session: Session = Depends(db.session)) -> SuccessResponse:
    '''
    글쓰기 페이지에서 작성한 작품 데이터를 입력받는 API

    :param data: 작품 데이터:\n
    :param session: DB 세션:\n
    :return SuccessResponse:
    '''

    if data.title == '':
        raise NotProperWritingContentsEx(wrong_value='title')
    if data.thumbnail == '':
        raise NotProperWritingContentsEx(wrong_value='thumbnail')
    if data.introduction == '':
        raise NotProperWritingContentsEx(wrong_value='introduction')
    if data.contents == '':
        raise NotProperWritingContentsEx(wrong_value='contents')
    if data.writer_id == '':
        raise NotProperWritingContentsEx(wrong_value='writer_id')
    if data.language == '':
        raise NotProperWritingContentsEx(wrong_value='language')

    Contents.create_contents(session, data)
    return SuccessResponse(
        msg='요청 성공',
        data={}
    )


@router.post(path='/editing_contents', response_model=SuccessResponse, status_code=status.HTTP_201_CREATED)
async def editing_contents(data: EditingContents) -> SuccessResponse:
    '''
    글수정 페이지에서 작성한 작품 데이터를 입력받는 API

    :param data: 작품 데이터:
    :return SuccessResponse:
    '''
    print(data)
    return SuccessResponse(
        msg='요청 성공',
        data={}
    )


@router.post(path='/increase_views', response_model=SuccessResponse, status_code=status.HTTP_201_CREATED)
async def increase_views(data: IncreaseViews) -> SuccessResponse:
    '''
    작품 조회수 카운트를 위한 API

    :param data: 작품 직별자:
    :return SuccessResponse:
    '''
    print(data)
    return SuccessResponse(
        msg='요청 성공',
        data={}
    )
