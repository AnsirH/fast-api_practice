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

# 유저 조회용 데이터 클래스
class UserResponse(BaseModel):
    id: int
    username: str

    # ORM 객체를 직렬화할 수 있도록 함
    # DB에서 가져온 객체를 API 응답으로 사용하기 위해서 정의
    class Config:
        from_attributes = True

# 상품 등록 데이터 객체
class ProductCreate(BaseModel):
    name: str
    price: int

# 상품 조회용 데이터 객체
class ProductOut(BaseModel):
    id: int
    name: str
    price: int
    class Config: # 객체로 리턴할 때
        from_attributes = True