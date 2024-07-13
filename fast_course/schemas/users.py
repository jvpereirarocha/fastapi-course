from pydantic import BaseModel, EmailStr


class _BaseUserData(BaseModel):
    username: str
    email: EmailStr


class UserSchema(_BaseUserData):
    password: str


class UserPublic(_BaseUserData):
    id: int


class UserDB(UserPublic): ...
