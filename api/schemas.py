# 요청 / 응답 모델( 데이터 타입 ) 정의
from pydantic import BaseModel

# 회원가입용 데이터 타입 pydantic
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

