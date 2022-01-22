from app.database.schema import Users
from sqlalchemy.orm import Session

def check_user_name(session: Session,  user_name: str) -> bool:
    if user_name == '무명':
        return True
    else:
        count = Users.count_users_by_user_name(session, user_name)
        if count < 1:
            return True
        else:
            return False
