"""“initial migration

Revision ID: 48591c733cc2
Revises: None
Create Date: 2016-02-15 22:24:14.050670

"""

# revision identifiers, used by Alembic.
revision = '48591c733cc2'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_email', 'users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    ### end Alembic commands ###
