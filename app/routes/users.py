from fastapi import APIRouter, Depends, status

from app.helper.users import check_user_name
from app.models import SuccessResponse, NameRegistration, UserRegistration, UserData, UserInfo
from app.database.conn import db
from app.database.schema import Users
from sqlalchemy.orm import Session

router = APIRouter(prefix='/user')

from app.errors.exceptions import NotFoundUserEx, DuplicateNameEx
from app.error_models import NotFoundUserModel, DuplicateNameModel


@router.get(
    path='/user_info',
    response_model=UserData,
    ### response 컨트롤 예제
    responses={
        404: {"model": NotFoundUserModel}
    }
)
async def user_info(user_id: str, session: Session = Depends(db.session)) -> UserData:
    '''
    유저 식별자를 입력받아 유저 정보를 반환하는 API

    :param user_id 유저 식별자:
    :return UserData:
    '''
    count = Users.count_users_by_user_id(session, user_id)
    if (count < 1):
        raise NotFoundUserEx(user_id=user_id)

    user = Users.get(user_id=user_id)
    return UserData(
        msg='응답 성공',
        data=UserInfo(
            user_id=user.user_id,
            user_name=user.user_name
        )
    )


@router.post(path='/name_registration',
             response_model=UserData,
             status_code=status.HTTP_201_CREATED,
             responses={
                 404: {"model": DuplicateNameModel}
             }
)
async def name_registration(data: NameRegistration, session: Session = Depends(db.session)) -> UserData:
    '''
    필명 등록 페이지에서 사용자 필명 데이터를 입력받는 API

    :param data: 유저 식별자, 필명:
    :return SuccessResponse:
    '''
    check = check_user_name(session, data.user_name)
    if check:
        Users.update_name(session, auto_commit=True, user_id=data.user_id, user_name=data.user_name)
        user = Users.get(user_id=data.user_id)
        return UserData(
            msg='요청 성공',
            data=UserInfo(
                user_id=user.user_id,
                user_name=user.user_name
            )
        )
    else:
        raise DuplicateNameEx(user_name=data.user_name)


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
    # DB에 입력되어 있는 사용자인지 확인하는 기능 구현
    count = Users.count_users_by_user_id(session, data.user_id)
    if (count < 1):
        # 카카오 계정 식별자를 입력받아 DB에 저장하는 기능 구현(user_name은 무명으로 기본값 세팅)
        Users.create_user(session, auto_commit=True, user_id=data.user_id, user_name='무명')
    # 성공적으로 저장하거나 이미 저장된 계정의 경우 UserData(user_id, user_name)를 반환하는 기능 구현
    user = Users.get(user_id=data.user_id)
    return UserData(
        msg='요청 성공',
        data=UserInfo(
            user_id=user.user_id,
            user_name=user.user_name
        )
    )
