"""Nouveaux champs dans la table User

Revision ID: 8322f7a9f490
Revises: 091e97b46ae5
Create Date: 2022-02-02 15:32:42.403104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8322f7a9f490'
down_revision = '091e97b46ae5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
