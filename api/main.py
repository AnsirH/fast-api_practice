# FAST API의 메인 서버
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from model import *
from database import SessionLocal, engin
from schemas import *
from fastapi.staticfiles import StaticFiles
from fastapi. middleware.cors import CORSMiddleware