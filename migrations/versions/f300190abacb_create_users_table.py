"""create users table

Revision ID: f300190abacb
Revises: 
Create Date: 2024-07-14 14:27:18.057523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f300190abacb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index('email_created_at_idx', 'users', ['email', 'created_at'], unique=False)
    op.create_index('email_pass_idx', 'users', ['email', 'password'], unique=False)
    op.create_index('user_created_at_idx', 'users', ['username', 'created_at'], unique=False)
    op.create_index('user_email_pass_idx', 'users', ['username', 'email', 'password'], unique=False)
    op.create_index('user_pass_idx', 'users', ['username', 'password'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('user_pass_idx', table_name='users')
    op.drop_index('user_email_pass_idx', table_name='users')
    op.drop_index('user_created_at_idx', table_name='users')
    op.drop_index('email_pass_idx', table_name='users')
    op.drop_index('email_created_at_idx', table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
