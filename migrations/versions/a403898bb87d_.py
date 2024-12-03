"""empty message

Revision ID: a403898bb87d
Revises: a5cffa318ac2
Create Date: 2024-12-03 00:06:29.226528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a403898bb87d'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('specie', sa.String(), nullable=False),
    sa.Column('height', sa.String(), nullable=False),
    sa.Column('mass', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('climate', sa.String(), nullable=False),
    sa.Column('population', sa.String(), nullable=False),
    sa.Column('size', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('life_span', sa.String(), nullable=False),
    sa.Column('planet', sa.String(), nullable=False),
    sa.Column('skin_color', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('species')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###