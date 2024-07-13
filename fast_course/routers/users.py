from http import HTTPStatus

from fastapi import APIRouter

from fast_course.schemas.users import CreatedUserPublic, CreateUserSchema, UserDB

user_router = APIRouter(prefix='/users')

FAKE_DB = []


@user_router.post('/', status_code=HTTPStatus.CREATED, response_model=CreatedUserPublic)
def create_user(user_schema: CreateUserSchema):
    user_with_id = UserDB(**user_schema.model_dump(), id=len(FAKE_DB) + 1)
    FAKE_DB.append(user_with_id)

    return user_with_id
