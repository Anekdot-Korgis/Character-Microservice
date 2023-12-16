"""change id to uuid

Revision ID: a62ada84c91f
Revises: 9d5fb445d3d0
Create Date: 2023-12-16 15:41:18.227139

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a62ada84c91f'
down_revision: Union[str, None] = '9d5fb445d3d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
