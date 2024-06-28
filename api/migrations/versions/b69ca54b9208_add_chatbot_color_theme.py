"""add chatbot color theme

Revision ID: b69ca54b9208
Revises: 4ff534e1eb11
Create Date: 2024-06-25 01:14:21.523873

"""
import sqlalchemy as sa
from alembic import op

import models as models

# revision identifiers, used by Alembic.
revision = 'b69ca54b9208'
down_revision = '4ff534e1eb11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('chat_color_theme', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('chat_color_theme_inverted', sa.Boolean(), server_default=sa.text('false'), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sites', schema=None) as batch_op:
        batch_op.drop_column('chat_color_theme_inverted')
        batch_op.drop_column('chat_color_theme')

    # ### end Alembic commands ###