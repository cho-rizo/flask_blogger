"""adding new fields to User model

Revision ID: 720c30619ebe
Revises: 5ea8557e1f5b
Create Date: 2019-02-19 11:13:25.340310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '720c30619ebe'
down_revision = '5ea8557e1f5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bio', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'bio')
    # ### end Alembic commands ###
