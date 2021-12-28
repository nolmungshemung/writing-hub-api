import boto3
import os

region = "ap-northeast-2"
ssm_client = boto3.client(
        'ssm',
        region_name=region,
        aws_access_key_id=os.environ.get("AWS_ACCESS", None),
        aws_secret_access_key=os.environ.get("AWS_SECRET", None),
)

EXCEPT_PATH_LIST = ["/", "/openapi.json"]
EXCEPT_PATH_REGEX = "^(/docs|/redoc|/api/auth)"
MAX_API_KEY = 3
MAX_API_WHITELIST = 10
