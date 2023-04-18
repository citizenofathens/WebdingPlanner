import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


from wedding.backend.db import schemas

app = FastAPI()
#https://wikidocs.net/176934


# 사용자 정보를 저장하는 데이터베이스를 구현합니다.
users =[]


# 사용자 정보를 등록하는 API를 구현합니다.
@app.get("/USERS")
async def create_user(user: schemas.User):
    users.append(user)
    return JSONResponse(content={"message": "Hello World"})


@app.get("/")
async def root():
    # 여권
    # 아파트 대출 정보 카카오 연동
    # 아이디나 이름 입력 하면 정보 나오도록 모든 체크리스트에 대한



    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
