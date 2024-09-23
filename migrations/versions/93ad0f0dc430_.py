"""empty message

Revision ID: 93ad0f0dc430
Revises: 862f694900c3
Create Date: 2024-09-23 14:42:09.400304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93ad0f0dc430'
down_revision = '862f694900c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job_post', schema=None) as batch_op:
        batch_op.alter_column('intro',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.String(length=1000),
               existing_nullable=True)
        batch_op.alter_column('more_about_your_plants',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.String(length=1000),
               existing_nullable=True)
        batch_op.alter_column('more_about_services',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.String(length=1000),
               existing_nullable=True)
        batch_op.alter_column('job_duration',
               existing_type=sa.VARCHAR(length=300),
               type_=sa.String(length=1000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job_post', schema=None) as batch_op:
        batch_op.alter_column('job_duration',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=300),
               existing_nullable=True)
        batch_op.alter_column('more_about_services',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=300),
               existing_nullable=True)
        batch_op.alter_column('more_about_your_plants',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=300),
               existing_nullable=True)
        batch_op.alter_column('intro',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=300),
               existing_nullable=True)

    # ### end Alembic commands ###
