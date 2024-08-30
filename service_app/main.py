from fastapi import APIRouter

service_app = APIRouter(
    prefix="/auth",
    tags=["业务功能"]
)