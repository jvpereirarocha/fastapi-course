from datetime import datetime

from sqlalchemy import Index, func
from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy.orm import registry

mapped_registry = registry()


@mapped_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(init=False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(init=False, onupdate=func.now())

    __table_args__ = (
        Index('user_email_pass_idx', 'username', 'email', 'password'),
        Index('email_pass_idx', 'email', 'password'),
        Index('user_pass_idx', 'username', 'password'),
        Index('user_created_at_idx', 'username', 'created_at'),
        Index('email_created_at_idx', 'email', 'created_at'),
        Index('user_updated_at_idx', 'username', 'updated_at'),
        Index('email_updated_at_idx', 'email', 'updated_at'),
    )
