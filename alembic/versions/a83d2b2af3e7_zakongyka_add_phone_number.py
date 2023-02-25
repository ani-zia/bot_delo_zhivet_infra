"""zakongyka_add_phone_number

Revision ID: a83d2b2af3e7
Revises: 345200deafa6
Create Date: 2023-02-25 21:43:16.785730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a83d2b2af3e7'
down_revision = '345200deafa6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assistance_disabled', schema=None) as batch_op:
        batch_op.create_geospatial_index('idx_assistance_disabled_geometry', ['geometry'], unique=False, postgresql_using='gist', postgresql_ops={})

    with op.batch_alter_table('pollution', schema=None) as batch_op:
        batch_op.create_geospatial_index('idx_pollution_geometry', ['geometry'], unique=False, postgresql_using='gist', postgresql_ops={})

    with op.batch_alter_table('volunteer', schema=None) as batch_op:
        batch_op.create_geospatial_index('idx_volunteer_geometry', ['geometry'], unique=False, postgresql_using='gist', postgresql_ops={})

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('volunteer', schema=None) as batch_op:
        batch_op.drop_geospatial_index('idx_volunteer_geometry', postgresql_using='gist', column_name='geometry')

    with op.batch_alter_table('pollution', schema=None) as batch_op:
        batch_op.drop_geospatial_index('idx_pollution_geometry', postgresql_using='gist', column_name='geometry')

    with op.batch_alter_table('assistance_disabled', schema=None) as batch_op:
        batch_op.drop_geospatial_index('idx_assistance_disabled_geometry', postgresql_using='gist', column_name='geometry')

    # ### end Alembic commands ###
