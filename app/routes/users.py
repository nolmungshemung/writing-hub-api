from fastapi import APIRouter, Depends
from app.models import SuccessResponse, NameRegistration, UserRegistration, UserData, Users
router = APIRouter(prefix='/user')


@router.get('/user_info', response_model=UserData)
async def user_info(user_id: str) -> UserData:
    '''
    유저 식별자를 입력받아 유저 정보를 반환하는 API

    :param user_id 유저 식별자:
    :return UserData:
    '''
    return UserData(
        msg='응답 성공',
        data=Users(
            user_id=user_id,
            user_name='장발장'
        )
    )


@router.post('/name_registration', response_model=UserData)
async def name_registration(data: NameRegistration) -> UserData:
    '''
    필명 등록 페이지에서 사용자 필명 데이터를 입력받는 API

    :param data: 사용자 필명:
    :return SuccessResponse:
    '''
    print(data)
    return UserData(
        msg='요청 성공',
        data=Users(
            user_id=data.user_id,
            user_name='장발장'
        )
    )


@router.post('/user_login', response_model=UserData)
async def user_login(data: UserRegistration) -> UserData:
    '''
    유저 데이터를 입력받는 API

    :param data: 유저 식별자:
    :return SuccessResponse:
    '''
    print(data)
    return UserData(
        msg='요청 성공',
        data=Users(
            user_id=data.user_id,
            user_name='장발장'
        )
    )

