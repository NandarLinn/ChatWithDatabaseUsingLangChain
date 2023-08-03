from fastapi import APIRouter
from apis.v1 import ask

api_router = APIRouter()
api_router.include_router(ask.router)
