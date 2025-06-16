# FAST API의 메인 서버
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from model import *
from database import SessionLocal, engin, Base
from schemas import *
from fastapi.staticfiles import StaticFiles
from fastapi. middleware.cors import CORSMiddleware
# Fast api 생성
app = FastAPI()

# CORS( Cross-Origin Resource Sharing ) 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://128.0.0.1:5000", "http://localhost:5000"], # flask 주소 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# 앱을 실행하면 dB에 정의된 모든 테이블을 생성
Base.metadata.create_all(bind=engin)

def get_db():
    db = SessionLocal() # 세션 객체 생성
    try:
        yield db # 종속된 함수에 세션 주입
    finally:
        db.close() # 요청이 끝나면 자동으로 세션 종료


from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, requests

# 템플릿 디렉토리 설정
# pip install jinja2


# 라우터( 요청에 응답하는 )
# 회원가입 post 시 실행되는 라우터
@app.post("/api/register")
def register_user(user: RegisterRequest, db:Session=Depends(get_db)):
    # 같은 사용자가 있는지 조회
    existing_user = db.query(User) \
        .filter(User.username == user.username or User.email == user.email) \
        .first()
    # 같은 사용자가 있으면 400에러로 응답
    if existing_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 사용자입니다.")
    # 새 유저에 대한 객체( 인스턴스 ) 생성
    new_user = User(
        username = user.username,
        email = user.email,
        password = user.password
    )
    # db commit하는 과정과 동일
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # DB에서 자동 생성된 id를 유저 인스턴스에 할당
    return {"success":True, "message": "회원가입 성공", "user_id": new_user.id}

# 사용자 정보 UserCreate로 DB 조회
@app.post("/api/login")
def login(user:UserCreate, db:Session=Depends(get_db)):
    # 사용자 테이블에서 입력한 이름과 패스워드가 있는지 조회
    print(user)
    found = db.query(user) \
        .filter(User.username == user.username, User.password == user.password) \
        .first()
    
    if not found:
        raise HTTPException(status_code=400, detail="로그인 실패")
    return {"success": True, "message": "로그인 성공"}

# 사용자의 고유 id로 user 테이블의 데이터 조회
@app.get("/api/users/{user_id}", response_model=UserResponse)
def get_user(user_id:int, db:Session=Depends(get_db)):
    user = db.query(User). \
        filter(User.id == user.id). \
        first()
    if not user:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
    return user
