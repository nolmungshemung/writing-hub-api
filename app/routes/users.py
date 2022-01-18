from fastapi import APIRouter, Depends, status
from app.models import SuccessResponse, NameRegistration, UserRegistration, UserData, UserInfo
from app.database.conn import db
from app.database.schema import Users
from sqlalchemy.orm import Session

router = APIRouter(prefix='/user')

from app.errors.exceptions import NotFoundUserEx
from app.error_models import NotFoundUserModel


@router.get(
    path='/user_info',
    response_model=UserData,
    ### response 컨트롤 예제
    responses={
        404: {"model": NotFoundUserModel}
    }
)
async def user_info(user_id: str) -> UserData:
    '''
    유저 식별자를 입력받아 유저 정보를 반환하는 API

    :param user_id 유저 식별자:
    :return UserData:
    '''
    ### 에러 발생 예제
    if user_id == 'test':
        raise NotFoundUserEx(user_id=user_id)
    return UserData(
        msg='응답 성공',
        data=UserInfo(
            user_id=user_id,
            user_name='장발장'
        )
    )


@router.post(path='/name_registration', response_model=UserData, status_code=status.HTTP_201_CREATED)
async def name_registration(data: NameRegistration) -> UserData:
    '''
    필명 등록 페이지에서 사용자 필명 데이터를 입력받는 API

    :param data: 유저 식별자, 필명:
    :return SuccessResponse:
    '''
    print(data)
    return UserData(
        msg='요청 성공',
        data=UserInfo(
            user_id=data.user_id,
            user_name=data.name
        )
    )

@router.post(
    path='/user_login',
    response_model=UserData,
    status_code=status.HTTP_201_CREATED,
)
async def user_login(data: UserRegistration, session: Session = Depends(db.session)) -> UserData:
    '''
    유저 데이터를 입력받는 API

    :param data: 유저 식별자:
    :param session: DB 세션:
    :return SuccessResponse:
    '''
    print(data)
    ### ORM으로 데이터 입력 예제
    if data.user_id == 'test':
        new_user = Users(
            user_id=data.user_id,
            user_name='무명'
        )
        session.add(new_user)
        session.commit()

        return UserData(
            msg='요청 성공',
            data=UserInfo(
                user_id=data.user_id,
                user_name='무명'
            )
        )
    return UserData(
        msg='요청 성공',
        data=UserInfo(
            user_id=data.user_id,
            user_name='장발장'
        )
    )