from fastapi import FastAPI
from database import engine
from sqlmodel import SQLModel
from models import User  # 우리가 방금 만든 모델 불러오기

app = FastAPI()


@app.on_event("startup")  # 서버 시작 시 실행
def on_startup():
    SQLModel.metadata.create_all(engine)  # 모델에 정의된 테이블들을 DB에 생성


@app.get("/")
def root():
    return {"message": "DB Connection Success!"}