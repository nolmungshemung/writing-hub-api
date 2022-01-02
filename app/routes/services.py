from fastapi import APIRouter
from app.models import Contents, Writer, MainContents, MainWriters, ReadingContents, TranslatingContents, FeedContents

router = APIRouter(prefix='/services')

@router.get('/main_contents', response_model=MainContents)
async def main_contents(keyword: str) -> MainContents:
    return MainContents(
        main_contents_list=[
            Contents(
                contents_id=20,
                title='장발장의 신나는 하루',
                thumbnail='그때 내가 왜그랬는지 도무지 이해할 수 없네',
                Introduction='장발장의 하루를 담은 이야기',
                writer=Writer(
                    writer_name='장발장',
                    writer_id='10asff'
                ),
                language='영어',
                is_translate=True,
                original_id=24
            ),
            Contents(
                contents_id=21,
                title='장발장의 신나는 하루2',
                thumbnail='어제 내가 왜그랬는지 도무지 이해할 수 없네',
                Introduction='장발장의 어제를 담은 이야기',
                writer=Writer(
                    writer_name='어제의 나',
                    writer_id='10asfg'
                ),
                language='한국어',
                is_translate=False,
                original_id=-1
            )
        ]
    )


@router.get('/main_writers', response_model=MainWriters)
async def main_writers(keyword: str) -> MainWriters:
    return MainWriters(
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

@router.get('/reading_contents', response_model=ReadingContents)
async def reading_contents(contents_id: int) -> ReadingContents:
    return ReadingContents(
        contents_id=21,
        title='장발장의 신나는 하루2',
        thumbnail='어제 내가 왜그랬는지 도무지 이해할 수 없네',
        Introduction='장발장의 어제를 담은 이야기',
        writer=Writer(
            writer_name='어제의 나',
            writer_id='10asfg'
        ),
        language='한국어',
        is_translate=False,
        original_id=-1,
        contents='그때 내가 왜그랬는지 도무지 이해할 수 없네\n 배고픔이 사람을 이렇게 만들줄이야',
        translated_contents_list=[
            Contents(
                contents_id=43,
                title='Fun Day',
                thumbnail='I cant understand why I did that back then.',
                Introduction='The Story of a Day',
                writer=Writer(
                    writer_name='장발장',
                    writer_id='10asff'
                ),
                language='영어',
                is_translate=True,
                original_id=21
            ),
            Contents(
                contents_id=43,
                title='Fun Day',
                thumbnail='I cant understand why I did that back then.',
                Introduction='The Story of a Day',
                writer=Writer(
                    writer_name='장발장',
                    writer_id='10asff'
                ),
                language='영어',
                is_translate=True,
                original_id=21
            )
        ]
    )

@router.get('/translating_contents', response_model=TranslatingContents)
async def translating_contents(contents_id: int) -> TranslatingContents:
    return TranslatingContents(
        contents_id=21,
        title='장발장의 신나는 하루2',
        thumbnail='어제 내가 왜그랬는지 도무지 이해할 수 없네',
        Introduction='장발장의 어제를 담은 이야기',
        writer=Writer(
            writer_name='어제의 나',
            writer_id='10asfg'
        ),
        language='한국어',
        is_translate=False,
        original_id=-1,
        contents='그때 내가 왜그랬는지 도무지 이해할 수 없네\n 배고픔이 사람을 이렇게 만들줄이야'
    )


@router.get('/feed_contents', response_model=FeedContents)
async def feed_contents(writer_id: str) -> FeedContents:
    return FeedContents(
        writer_name='장발장',
        writer_id='10asff',
        feed_contents_list=[
            Contents(
                contents_id=20,
                title='장발장의 신나는 하루',
                thumbnail='그때 내가 왜그랬는지 도무지 이해할 수 없네',
                Introduction='장발장의 하루를 담은 이야기',
                writer=Writer(
                    writer_name='장발장',
                    writer_id='10asff'
                ),
                language='영어',
                is_translate=True,
                original_id=24
            ),
            Contents(
                contents_id=21,
                title='장발장의 신나는 하루2',
                thumbnail='어제 내가 왜그랬는지 도무지 이해할 수 없네',
                Introduction='장발장의 어제를 담은 이야기',
                writer=Writer(
                    writer_name='장발장',
                    writer_id='10asff'
                ),
                language='한국어',
                is_translate=False,
                original_id=-1
            )
        ]
    )