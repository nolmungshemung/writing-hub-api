from dataclasses import dataclass
from os import path, environ
import boto3
import os

region = "ap-northeast-2"
base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
ssm_client = boto3.client(
        'ssm',
        region_name=region,
        aws_access_key_id=os.environ.get("AWS_ACCESS", None),
        aws_secret_access_key=os.environ.get("AWS_SECRET", None),
)

ssm_key = ssm_client.get_parameter(Name='dev_mysql_pass')
mysql_pass = ssm_key['Parameter']['Value']


@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR: str = base_dir
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True
    DEBUG: bool = False
    TEST_MODE: bool = False
    DB_URL: str = environ.get("DB_URL", f"mysql+pymysql://admin:{mysql_pass}@writinghub-sql-dev.c0xi6rczrwou.ap-northeast-2.rds.amazonaws.com/writinghub?charset=utf8mb4")



@dataclass
class LocalConfig(Config):
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    DEBUG: bool = True


@dataclass
class ProdConfig(Config):
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]


@dataclass
class TestConfig(Config):
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    TEST_MODE: bool = True


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig, local=LocalConfig, test=TestConfig)
    return config[environ.get("API_ENV", "local")]()


