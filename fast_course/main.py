from fastapi import FastAPI
from fastapi.routing import APIRouter

from fast_course.routers.users import user_router

app = FastAPI(title='Task manager API', version='1.0')

v1_router = APIRouter(prefix='/api/v1')

v1_router.include_router(user_router)

app.include_router(v1_router)
