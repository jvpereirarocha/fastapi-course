from pydantic import BaseModel, EmailStr


class _BaseUserData(BaseModel):
    username: str
    email: EmailStr


class CreateUserSchema(_BaseUserData):
    password: str


class CreatedUserPublic(_BaseUserData):
    id: int


class UserDB(CreatedUserPublic): ...
