# 구현 순서

1. 가상환경 생성

2. install
```
pip install fastapi uvicorn sqlalchemy flask
```

3. api 폴더 생성 후 파일 생성

- main, database, model, schemas ( .py )

4. 데이터 베이스 정의 및 설정

    - database.py에 데이터베이스 생성 FastAPI + sqlite 연동 환경 설정 코드 작성

    - model.py에 사용자 데이터 컬럼 클래스 정의

5. 회원가입 router 구현

    - schemas.py에 회원가입용 정보 데이터 클래스 RegisterRequest 정의

    - main.py에 회원가입 post router 정의: register_user

6. 로그인 router 구현

    - schemas.py에 로그인용 정보 데이터 클래스 UserCreate 정의

    - main.py에 로그인 시 작동 router 정의

7. 사용자 조회 router 구현

    - schemas.py에 사용자 조회용 클래스 정의 UserResponse

    - main.py에 사용자 조회 router 함수 정의: get_user

# Fast API 실행 - main.py 가 있는 api 폴더에서 진행
```
cd api
uvicorn main:app --reload
```

# API 테스트
```

```