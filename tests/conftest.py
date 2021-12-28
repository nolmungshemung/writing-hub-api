import asyncio
import os
from os import path
from typing import List

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.database.schema import Users
from app.main import create_app
from app.database.conn import db, Base
from app.models import UserToken
from app.routes.auth import create_access_token


"""
1. DB 생성
2. 테이블 생성
3. 테스트 코드 작동
4. 테이블 레코드 삭제 
"""

@pytest.fixture(scope="session")
def app():
    os.environ["API_ENV"] = "test"
    return create_app()


@pytest.fixture(scope="session")
def client(app):
    return TestClient(app=app)