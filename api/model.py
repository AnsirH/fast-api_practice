# 데이터 베이스 테이블 정의
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class User(Base): # 테이블. Base를 상속 받아야만 sqlite 테이블 생성 가능
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String) # 일단 보안은 나중에

# 상품 테이블
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    price = Column(Integer)