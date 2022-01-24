from sqlalchemy import (
    Column,
    String,
    func
)

from sqlalchemy.orm import Session, relationship
from app.database.conn import Base, db


class UserRepository:
    def __init__(self):
        self._q = None
        self._session = None
        self.served = None

    @classmethod
    def get(cls, session: Session = None, **kwargs):
        """
        Simply get a Row
        :param session:
        :param kwargs:
        :return:
        """
        sess = next(db.session()) if not session else session
        query = sess.query(cls)
        for key, val in kwargs.items():
            col = getattr(cls, key)
            query = query.filter(col == val)

        if query.count() > 1:
            raise Exception("Only one row is supposed to be returned, but got more than one.")
        result = query.first()
        if not session:
            sess.close()
        return result

    @classmethod
    def create_user(cls, session: Session = None, auto_commit: bool = False, user_id='', user_name=''):
        user = Users(user_id=user_id, user_name=user_name)
        session.add(user)
        session.commit()

    @classmethod
    def update_name(cls, session: Session = None, auto_commit: bool = False, user_id='', user_name=''):
        user = session.query(Users).filter(Users.user_id == user_id).update({'user_name': user_name})
        session.commit()

    @classmethod
    def count_users_by_user_id(cls, session: Session = None, user_id=''):
        sess = next(db.session()) if not session else session
        result = sess.query(Users).filter(Users.user_id == user_id).count()
        return result

    @classmethod
    def count_users_by_user_name(cls, session: Session = None, user_name=''):
        sess = next(db.session()) if not session else session
        result = sess.query(Users).filter(Users.user_name == user_name).count()
        return result


class Users(Base, UserRepository):
    __tablename__ = "Users"
    user_id = Column(String(length=100), primary_key=True, nullable=False)
    user_name = Column(String(length=20), nullable=False)
