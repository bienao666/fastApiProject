from fastapi import APIRouter

database_app = APIRouter(
    prefix="/database",
    tags=["数据库"]
)
