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
