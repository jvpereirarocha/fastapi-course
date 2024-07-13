from http import HTTPStatus

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from fast_course.schemas.users import UserDB, UserList, UserPublic, UserSchema

user_router = APIRouter(prefix='/users')

FAKE_DB: list[UserDB] = []


def invalid_id(id: int) -> bool:
    return id > len(FAKE_DB) or id < 1


@user_router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user_schema: UserSchema):
    user_with_id = UserDB(**user_schema.model_dump(), id=len(FAKE_DB) + 1)
    FAKE_DB.append(user_with_id)

    return user_with_id


@user_router.get('/', status_code=HTTPStatus.OK, response_model=UserList)
def get_all_users():
    return {'users': FAKE_DB}


@user_router.get(
    '/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic | None
)
def fetch_one_user(user_id: int):
    for user in FAKE_DB:
        if user.id == user_id:
            return user

    return HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')


@user_router.put(
    '/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic | None
)
def update_user_by_id(user_id: int, user_schema: UserSchema):
    if invalid_id(id=user_id):
        return HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    user_with_id = UserDB(**user_schema.model_dump(), id=user_id)
    FAKE_DB[user_id - 1] = user_with_id

    return user_with_id


@user_router.delete(
    '/{user_id}', status_code=HTTPStatus.NO_CONTENT, response_model=None
)
def delete_one_user(user_id: int):
    if invalid_id(id=user_id):
        return HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    del FAKE_DB[user_id - 1]
    return None
