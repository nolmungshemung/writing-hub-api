from fastapi import APIRouter, Depends
from starlette.requests import Request

from app.database.schema import Users
from app.models import UserMe

router = APIRouter(prefix='/user')

@router.get('/me', response_model=UserMe)
async def get_me(request: Request):
    user = request.state.user
    user_info = Users.get(id=user.id)
    return user_info