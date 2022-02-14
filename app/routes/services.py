import time

from fastapi import APIRouter, Depends, status

from app.models import Contents, Writer, MainContents, MainWriters, ReadingContents, TranslatingContents, FeedContents, \
    WritingContents, MainContentsData, MainWritersData, ReadingContentsData, TranslatingContentsData, FeedContentsData, \
    SuccessResponse, IncreaseViews, EditingContents, Paging
from typing import Optional
from app.database.conn import db
from app.database.schema import Content, Users
from sqlalchemy.orm import Session

from app.errors.exceptions import NotFoundContentEx, NotOriginalContentEx, NotFoundFeedContentEx
from app.error_models import NotFoundContentModel, NotOriginalContentModel, NotFoundFeedContentModel

router = APIRouter(prefix='/services')


@router.get(path='/main_contents',
            response_model=MainContentsData,
            responses={
                404: {"model": NotFoundContentModel}
            })
async def main_contents(
        start: int = 0,
        count: int = 10,
        base_time: int = 0,
        keyword: Optional[str] = '',
        session: Session = Depends(db.session)
) -> MainContentsData:
    '''
    메인 페이지에서 표시되는 작품 데이터를 반환하는 API

    :param start: 가져오려는 데이터 시작점:
    :param count: 가져오려는 데이터 개수:
    :param base_time: 기준 시점, timestamp로 소수점 없이 입력(시간순서대로 정렬된 데이터가 새로 입력되는 데이터와 관계없이 중복되지 않기 위해 필요):
    :param keyword: 검색어:
    :return MainContentsData:
    '''

    main_contents_list = []
    contents = Content.get_by_title(session, keyword.replace(" ", ""), base_time, start, count)
    for content in contents:
        print(content)
        temp = Contents()
        temp.contents_id = content.contents_id
        temp.title = content.title
        temp.thumbnail = content.thumbnail
        temp.introduction = content.introduction
        temp.writer = Writer(writer_name=content.user_name,
                             writer_id=content.user_id)
        temp.language = content.language
        temp.is_translate = content.is_translate
        temp.original_id = content.original_id
        temp.views = content.views
        temp.translation_num = content.count
        main_contents_list.append(temp)

    if(len(main_contents_list) < 1):
        raise NotFoundContentEx()

    # is_last 로직 작성
    is_last = False
    next_contents = Content.get_by_title(session, keyword.replace(" ", ""), base_time, start + count, count)
    if next_contents.rowcount > 0:
        is_last = True

    return MainContentsData(
        msg='응답 성공',
        data=MainContents(
            main_contents_list=main_contents_list,
            paging=Paging(
                start=start,
                is_last=is_last,
            )
        )
    )


@router.get(path='/main_writers', response_model=MainWritersData)
async def main_writers(
        start: int = 0,
        count: int = 10,
        base_time: int = 0,
        keyword: Optional[str] = '',
        session: Session = Depends(db.session)
) -> MainWritersData:
    '''
    메인 페이지에서 표시되는 작가 데이터를 반환하는 API
    :param start: 가져오려는 데이터 시작점:
    :param count: 가져오려는 데이터 개수:
    :param base_time: 기준 시점, timestamp로 소수점 없이 입력(시간순서대로 정렬된 데이터가 새로 입력되는 데이터와 관계없이 중복되지 않기 위해 필요):
    :param keyword: 검색어:
    :return MainWritersData:
    '''

    main_writer_list = []
    users = Users.get_main_writer(session, keyword.replace(" ", ""), start, count)
    for user in users:
        print(user)
        temp = Writer()
        temp.writer_name = user.user_name
        temp.writer_id = user.user_id
        main_writer_list.append(temp)
    return MainWritersData(
        msg='응답 성공',
        data=MainWriters(
            main_writer_list=[
                Writer(
                    writer_name='장발장',
                    writer_id='10asff'
                ) for _ in range(count)
            ]
        )
    )


@router.get(path='/reading_contents',
            response_model=ReadingContentsData,
            responses={
                404: {"model": NotFoundContentModel}
            })
async def reading_contents(contents_id: int, session: Session = Depends(db.session)) -> ReadingContentsData:
    '''
    글읽기 페이지에서 표시되는 작품 데이터를 반환하는 API

    :param contents_id: 작품 식별자:
    :return ReadingContentsData:
    '''
    # 특정 컨텐츠의 데이터를 추출하는 쿼리 작성
    content = Content.get_by_content_id(session, contents_id)

    # 조건에 맞는 데이터가 없는 경우 예외처리 기능 구현(404 code와 msg 반환)
    if (len(content) < 1):
        raise NotFoundContentEx()

    # 번역본 데이터를 추출하는 쿼리 작성(작성 일자로 내림차순 정렬, 원문인 경우에만 번역본 데이터 반환)
    translated_contents_list = []
    if (content[0].Content.original_id == -1 and content[0].Content.is_translate == 1):
        translated_contents = Content.get_translated_contents(session, contents_id)
        for i in range(len(translated_contents)):
            temp = Contents()
            temp.contents_id = translated_contents[i].Content.contents_id
            temp.title = translated_contents[i].Content.title
            temp.thumbnail = translated_contents[i].Content.thumbnail
            temp.introduction = translated_contents[i].Content.introduction
            temp.writer = Writer(writer_name=translated_contents[i].Users.user_name,
                                 writer_id=translated_contents[i].Users.user_id)
            temp.language = translated_contents[i].Content.language
            temp.is_translate = False
            temp.original_id = translated_contents[i].Content.original_id
            temp.views = translated_contents[i].Content.views
            temp.translation_num = 0
            translated_contents_list.append(temp)

    return ReadingContentsData(
        msg='응답 성공',
        data=ReadingContents(
            contents_id=content[0].Content.contents_id,
            title=content[0].Content.title,
            thumbnail=content[0].Content.thumbnail,
            introduction=content[0].Content.introduction,
            writer=Writer(
                writer_name=content[0].Users.user_id,
                writer_id=content[0].Users.user_name
            ),
            language=content[0].Content.language,
            is_translate=True if content[0].Content.is_translate == 1 else False,
            original_id=content[0].Content.original_id,
            views=content[0].Content.views,
            translation_num=len(translated_contents_list),
            contents=content[0].Content.contents,
            created_date=time.mktime(content[0].Content.updated_date.timetuple()),
            translated_contents_list=translated_contents_list
        )
    )


@router.get(path='/translating_contents',
            response_model=TranslatingContentsData,
            responses={
                404: {"model": NotFoundContentModel},
                403: {"model": NotOriginalContentModel}
            })
async def translating_contents(contents_id: int, session: Session = Depends(db.session)) -> TranslatingContentsData:
    '''
    번역 페이지에서 표시되는 데이터를 반환하는 API

    :param contents_id: 작품 식별자:
    :return TranslatingContentsData:
    '''
    # 특정 컨텐츠의 데이터를 반환하는 코드 구현
    content = Content.get_by_content_id(session, contents_id)

    # 조건에 맞는 데이터가 없는 경우 예외처리 기능 구현(404 code와 msg 반환)
    if (len(content) < 1):
        raise NotFoundContentEx()

    # 번역하고자하는 컨텐츠가 원문인지 확인하는 기능 구현(원문이 아닌 경우 403 code와 msg 반환)
    if (content[0].Content.original_id != -1):
        raise NotOriginalContentEx(contents_id=contents_id)

    translating_count = Content.count_translated_contents(session, contents_id)
    return TranslatingContentsData(
        msg='응답 성공',
        data=TranslatingContents(
            contents_id=content[0].Content.contents_id,
            title=content[0].Content.title,
            thumbnail=content[0].Content.thumbnail,
            introduction=content[0].Content.introduction,
            writer=Writer(
                writer_name=content[0].Users.user_id,
                writer_id=content[0].Users.user_name
            ),
            language=content[0].Content.language,
            is_translate=True if content[0].Content.is_translate == 1 else False,
            original_id=content[0].Content.original_id,
            views=content[0].Content.views,
            translation_num=translating_count,
            contents=content[0].Content.contents,
        )
    )


@router.get(path='/feed_contents',
            response_model=FeedContentsData,
            responses={
                404: {"model": NotFoundFeedContentModel}
            })
async def feed_contents(writer_id: str, session: Session = Depends(db.session)) -> FeedContentsData:
    '''
    피드 페이지에서 표시되는 데이터를 반환하는 API

    :param writer_id: 작가 식별자:
    :return FeedContentsData:
    '''
    # 특정 유저의 데이터를 반환하는 코드 구현
    writer = Users.get(user_id=writer_id)

    # 특정 유저가 작성한 컨텐츠를 반환하는 코드 구현(작성 일자로 내림차순 정렬)
    feed_contents = Content.get_by_writer_id(session, writer_id)

    # 조건에 맞는 데이터가 없는 경우 예외처리 기능 구현(404 code와 msg 반환)
    if (len(feed_contents) == 0):
        raise NotFoundFeedContentEx(writer_id=writer_id)

    feed_contents_list = []
    for i in range(len(feed_contents)):
        temp = Contents()
        temp.contents_id = feed_contents[i].Content.contents_id
        temp.title = feed_contents[i].Content.title
        temp.thumbnail = feed_contents[i].Content.thumbnail
        temp.introduction = feed_contents[i].Content.introduction
        temp.writer = Writer(writer_name=feed_contents[i].Users.user_name,
                             writer_id=feed_contents[i].Users.user_id)
        temp.language = feed_contents[i].Content.language
        temp.is_translate = True if feed_contents[i].Content.is_translate == 1 else False
        temp.original_id = feed_contents[i].Content.original_id
        temp.views = feed_contents[i].Content.views
        temp.translation_num = Content.count_translated_contents(session, feed_contents[i].Content.contents_id)
        feed_contents_list.append(temp)

    return FeedContentsData(
        msg='응답 성공',
        data=FeedContents(
            writer=Writer(
                writer_name=writer.user_name,
                writer_id=writer.user_id
            ),
            feed_contents_list=feed_contents_list
        )
    )


@router.post(path='/writing_contents', response_model=SuccessResponse, status_code=status.HTTP_201_CREATED)
async def writing_contents(data: WritingContents) -> SuccessResponse:
    '''
    글쓰기 페이지에서 작성한 작품 데이터를 입력받는 API

    :param data: 작품 데이터:
    :return SuccessResponse:
    '''
    print(data)
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
