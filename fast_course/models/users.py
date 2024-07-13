from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, registry
from sqlalchemy.schema import Index
from sqlalchemy.sql import func

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())

    __table_args__ = (
        Index('email_username_idx', 'email', 'username'),
        Index('email_password_idx', 'email', 'password'),
        Index('username_password_idx', 'username', 'password'),
        Index('email_username_password_idx', 'email', 'username', 'password'),
        Index('email_created_at_idx', 'email', 'created_at'),
        Index('username_created_at_idx', 'username', 'created_at'),
    )
