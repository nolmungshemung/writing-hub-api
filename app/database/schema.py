from sqlalchemy import (
    Column,
    String,
    func
)
from sqlalchemy.dialects import mysql

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


class ContentRepository:
    def __init__(self):
        self._q = None
        self._session = None
        self.served = None

    @classmethod
    def get_by_content_id(cls, session: Session = None, contents_id=''):
        sess = next(db.session()) if not session else session
        result = sess.query(Content, Users).join(Users, Content.writer_id == Users.user_id).filter(Content.contents_id == contents_id).all()
        return result
class Users(Base, UserRepository):
    __tablename__ = "Users"
    user_id = Column(String(length=100), primary_key=True, nullable=False)
    user_name = Column(String(length=20), nullable=False)


class Content(Base, ContentRepository):
    __tablename__ = "Contents"
    contents_id = Column(mysql.BIGINT(unsigned=True), primary_key=True, nullable=False)
    writer_id = Column(mysql.VARCHAR(length=100), nullable=False)
    contents = Column(mysql.TEXT)
    is_translate = Column(mysql.TINYINT(unsigned=True))
    original_id = Column(mysql.BIGINT(unsigned=True))
    language = Column(mysql.VARCHAR(length=10))
    created_date = Column(mysql.DATETIME)
    title = Column(mysql.VARCHAR(length=100))
    thumbnail = Column(mysql.VARCHAR(length=200))
    introduction = Column(mysql.VARCHAR(length=200))
    updated_date = Column(mysql.DATETIME)
    reviews = Column(mysql.BIGINT)