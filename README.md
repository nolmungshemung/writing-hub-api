# writing-hub-api
writinghub api server


### 참고
- Swagger: https://dev-api.writinghub.app/docs
- ERD: https://www.erdcloud.com/d/eYXit3bhdgwqKQPys
- Trello: https://trello.com/b/eZ1pFOtT/writinghubbackend

### 프로그램 폴더 구조

```
Github
├─app
│  ├─common
│  ├─database
│  ├─errors
│  ├─helper
│  ├─middlewares
│  ├─routes
│  └─utils
|  main.py
|  models.py
└─tests
    conftest.py
    test_{}.py
```

### 폴더 및 파일 역할
- common: 변수의 정의
- database: DB연결 및 스키마 정의
- errors: 에러 케이스 정의 및 에러 반환값 정의
- helper: API 비즈니스 로직 처리 모듈
- middlewares: 미들웨어 관리
- routes: 라우터 정의
- utils: 유틸 함수 정의
- tests: pytest 사용을 위한 폴더
- models.py: API response model, requests body 정의
- main.py: 웹 서버 실행 관리


### 코드 작성시 참고사항
- 지역 변수, 함수, 모듈명은 snake case 사용
- class는 camle case 사용
- 전역 변수는 대문자와 _ 를 사용해 작성 (예시, MYSQL_URL)


### 기술 스택
- Python 3.8
- FastAPI
- AWS RDS(Mysql)
- AWS Elastic Beanstalk
- Docker


### Commit 메세지 규칙
```
타입(Type)
	Feat - 새로운 기능 추가
	Fix - 버그 수정
	Ci - CI관련 설정 수정
	Docs - 문서 (문서 추가, 수정, 삭제)
	Style - 스타일 (코드 형식, 세미콜론 추가: 비즈니스 로직에 변경 없는 경우)
	Refactor - 코드 리팩토링
	Test - 테스트 (테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없는 경우)
	Chore - 기타 변경사항

제목(Subject)
	제목은 50자를 넘기지 않고, 마침표를 붙이지 않습니다.
	제목에는 commit 타입을 함께 작성합니다.
	과거 시제를 사용하지 않고 명령조로 작성합니다.
	제목과 본문은 한 줄 띄워 분리합니다.
	제목의 첫 글자는 반드시 대문자로 씁니다.
	제목이나 본문에 이슈 번호(가 있다면) 붙여야 합니다.

본문(Body)
	선택 사항이기에 모든 commit에 본문 내용을 작성할 필요는 없습니다.
	한 줄에 72자를 넘기면 안 됩니다.
	어떻게(How)보다 무엇을, 왜(What, Why)에 맞춰 작성합니다.
	설명뿐만 아니라, commit의 이유를 작성할 때에도 씁니다.

꼬리말(Footer)
	선택 사항이므로 모든 commit에 꼬리말을 작성할 필요는 없습니다.
	Issue tracker ID를 작성할 때 사용합니다.
	해결: 이슈 해결 시 사용
	관련: 해당 commit에 관련된 이슈 번호
	참고: 참고할 이슈가 있는 경우 사용

예시
	Feat: 유저 등록 비즈니스 로직 추가(#123)

	유저 등록 비즈니스 로직 추가
	  - app/helper/users.py: 유저 정보를 입력받아 DB에 저장하는 비즈니스 로직 추가

	해결: #123

```
