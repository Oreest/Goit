"""Add avatar column to users

Revision ID: 7beba515965f
Revises: fa8c8234cedf
Create Date: 2024-06-09 21:44:26.746412

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7beba515965f'
down_revision: Union[str, None] = 'fa8c8234cedf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatarBinary', sa.LargeBinary(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatarBinary')
    # ### end Alembic commands ###