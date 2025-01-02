"""hide-in-ledger

Revision ID: f99e7bda56bb
Revises: f3b30f43aa86
Create Date: 2024-12-20 13:59:15.359911

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f99e7bda56bb'
down_revision = 'f3b30f43aa86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('filings', sa.Column('hide_in_ledger', sa.Boolean(), nullable=False, server_default='False'))
    op.execute("UPDATE filings SET hide_in_ledger = true WHERE filing_type = 'adminFreeze'")
    op.execute("UPDATE filings SET hide_in_ledger = true WHERE filing_type = 'dissolution' and filing_sub_type = 'involuntary'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('filings', 'hide_in_ledger')
    # ### end Alembic commands ###