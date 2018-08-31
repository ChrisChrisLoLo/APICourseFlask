"""empty message

Revision ID: 7d7f08668a01
Revises: fa35c4cd2178
Create Date: 2018-08-30 19:22:13.428462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d7f08668a01'
down_revision = 'fa35c4cd2178'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('subject_name_key', 'subject', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('subject_name_key', 'subject', ['name'])
    # ### end Alembic commands ###
