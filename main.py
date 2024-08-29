from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List  # 用于定义对象数组

from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI(
    title='项目名称',
    description='描述',
    version='1.0.0'
)

# mount表示将某个目录下一个完全独立的应用挂载过来
app.mount('/static', StaticFiles(directory='./static'), name='static')


# # 重写HTTPException异常处理器
# @app.exception_handlers(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     """
#
#     :param request:
#     :param exc:
#     :return:
#     """
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
#
#
# # 重写HTTPException异常处理器
# @app.exception_handlers(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     """
#
#     :param request:
#     :param exc:
#     :return:
#     """
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


# 在数据库中生成表结构
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
