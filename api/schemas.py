# 요청 / 응답 모델( 데이터 타입 ) 정의
from pydantic import BaseModel

# 회원가입용 데이터 클래스 pydantic
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

# 로그인용 데이터 클래스
class UserCreate(BaseModel):
    username: str
    password: str