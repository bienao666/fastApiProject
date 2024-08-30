from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from auth_app import models, schemas, crud
from database_app.database import engine, SessionLocal

auth_app = APIRouter(
    prefix="/auth",
    tags=["认证授权"]
)

# 在数据库中生成表结构
models.Base.metadata.create_all(bind=engine)


# 数据库
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@auth_app.post("/create_user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="账号已存在")
    return crud.create_user(db=db, user=user)


@auth_app.get("/get_user/{email}", response_model=schemas.User)
def get_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="账号不存在")
    return db_user


@auth_app.get("/get_users", response_model=List[schemas.User])
def get_users(skip: int, limit: int, db: Session = Depends(get_db)):
    db_users = crud.get_users(db=db, skip=skip, limit=limit)
    return db_users

