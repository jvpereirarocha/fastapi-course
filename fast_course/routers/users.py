from http import HTTPStatus

from fastapi import APIRouter

from fast_course.schemas.users import UserDB, UserList, UserPublic, UserSchema

user_router = APIRouter(prefix='/users')

FAKE_DB = []


@user_router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user_schema: UserSchema):
    user_with_id = UserDB(**user_schema.model_dump(), id=len(FAKE_DB) + 1)
    FAKE_DB.append(user_with_id)

    return user_with_id


@user_router.get('/', status_code=HTTPStatus.OK, response_model=UserList)
def get_all_users():
    return {'users': FAKE_DB}
