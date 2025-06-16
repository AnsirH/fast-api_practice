# 진행 순서

1. 가상환경 생성

2. install
```
pip install fastapi uvicorn sqlalchemy flask
```

3. api 폴더 생성 후 파일 생성

- main, database, model, schemas ( .py )

4. database,

# Fast API 실행 - main.py 가 있는 api 폴더에서 진행
```
cd api
uvicorn main:app --reload
```