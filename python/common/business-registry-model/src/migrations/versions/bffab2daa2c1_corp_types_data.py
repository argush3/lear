"""corp_types_data

Revision ID: bffab2daa2c1
Revises: e62e82cc80e0
Create Date: 2023-05-31 12:12:51.472037

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String

# revision identifiers, used by Alembic.
revision = 'bffab2daa2c1'
down_revision = '3d8eb786f4c2'
branch_labels = None
depends_on = None


def upgrade():

    corp_types_table = table('corp_types',
        sa.Column('corp_type_cd', sa.String()),
        sa.Column('colin_ind', sa.String()),
        sa.Column('corp_class', sa.String()),
        sa.Column('short_desc', sa.String()),
        sa.Column('full_desc', sa.String()),
        sa.Column('legislation', sa.String()),
        sa.Column('version', sa.Integer()),
    )

    op.bulk_insert(
        corp_types_table,
        [
            {'corp_type_cd': 'A', 'colin_ind': 'Y', 'corp_class': 'XPRO', 'short_desc': 'EXTRA PRO', 'full_desc': 'Extraprovincial Company', 'legislation': 'BC Business Corporations Act', 'version': 0},
            {'corp_type_cd': 'B', 'colin_ind': 'Y', 'corp_class': 'XPRO', 'short_desc': 'EXTRA PRO', 'full_desc': 'Extraprovincial Company', 'legislation': 'BC Business Corporations Act', 'version': 0},
            {'corp_type_cd': 'BC', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'BC COMPANY', 'full_desc': 'BC Limited Company', 'legislation': 'BC Business Corporations Act', 'version': 0},
            {'corp_type_cd': 'C', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'CONTINUE IN', 'full_desc': 'BC Limited Company', 'legislation': 'BC Business Corporations Act', 'version': 0},
            {'corp_type_cd': 'CEM', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'CEMETARY', 'full_desc': 'Cemetary', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'CP', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'COOP', 'full_desc': 'BC Cooperative Association', 'legislation': 'BC Cooperative Association Act', 'version': 0},
            {'corp_type_cd': 'EPR', 'colin_ind': 'Y', 'corp_class': 'XPRO', 'short_desc': 'EXTRA PRO REG', 'full_desc': 'Extraprovincial Registration', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'FOR', 'colin_ind': 'Y', 'corp_class': 'XPRO', 'short_desc': 'FOREIGN', 'full_desc': 'Foreign Registration', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'LIC', 'colin_ind': 'Y', 'corp_class': 'XPRO', 'short_desc': 'LICENSED', 'full_desc': 'Licensed (Extra-Pro)', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'LIB', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'LIBRARY', 'full_desc': 'Public Library Association', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'LLC', 'colin_ind': 'Y', 'corp_class': 'XPRO', 'short_desc': 'LIMITED CO', 'full_desc': 'Limited Liability Company', 'legislation': 'BC Business Corporations Act', 'version': 0},
            {'corp_type_cd': 'PA', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'PRIVATE ACT', 'full_desc': 'Private Act', 'legislation': 'Private Act', 'version': 0},
            {'corp_type_cd': 'PAR', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'PARISHES', 'full_desc': 'Parishes', 'legislation': 'BC Partnership Act', 'version': 0},
            {'corp_type_cd': 'PFS', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'PENS FUND SOC', 'full_desc': 'Pension Funded Society', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'QA', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'CO 1860', 'full_desc': 'CO 1860', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'QB', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'CO 1862', 'full_desc': 'CO 1862', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'QC', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'CO 1878', 'full_desc': 'CO 1878', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'QD', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'CO 1890', 'full_desc': 'CO 1890', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'QE', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'CO 1897', 'full_desc': 'CO 1897', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'REG', 'colin_ind': 'Y', 'corp_class': 'XPRO', 'short_desc': 'REGISTRATION', 'full_desc': 'Registraton (Extra-pro)', 'legislation': 'BC Business Corporations Act', 'version': 0},
            {'corp_type_cd': 'RLY', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'RAILWAYS', 'full_desc': 'Railways', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'SB', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'SOCIETY BRANCH', 'full_desc': 'Society Branch', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'T', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'TRUST', 'full_desc': 'Trust', 'legislation': 'BC Partnership Act', 'version': 0},
            {'corp_type_cd': 'TMY', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'TRAMWAYS', 'full_desc': 'Tramways', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'XCP', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'XPRO COOP', 'full_desc': 'Extraprovincial Cooperative Association', 'legislation': 'BC Cooperative Association Act', 'version': 0},
            {'corp_type_cd': 'ULC', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'BC ULC COMPANY', 'full_desc': 'BC Unlimited Liability Company', 'legislation': 'BC Business Corporations Act', 'version': 0},
            {'corp_type_cd': 'CUL', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'ULC CONTINUE IN', 'full_desc': 'Continuation In as a BC ULC', 'legislation': 'BC Business Corporations Act', 'version': 0},
            {'corp_type_cd': 'UQA', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'ULC CO 1860', 'full_desc': 'ULC CO 1860', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'UQB', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'ULC CO 1862', 'full_desc': 'ULC CO 1862', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'UQC', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'ULC CO 1878', 'full_desc': 'ULC CO 1878', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'UQD', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'ULC CO 1890', 'full_desc': 'ULC CO 1890', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'UQE', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'ULC CO 1897', 'full_desc': 'ULC CO 1897', 'legislation': '', 'version': 0},
            {'corp_type_cd': 'CC', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'BC CCC', 'full_desc': 'BC Community Contribution Company', 'legislation': 'BC Business Corporations Act', 'version': 0},
            {'corp_type_cd': 'CCC', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'CCC CONTINUE IN', 'full_desc': 'BC Community Contribution Company', 'legislation': 'BC Business Corporations Act', 'version': 0},
            {'corp_type_cd': 'S', 'colin_ind': 'Y', 'corp_class': 'SOC', 'short_desc': 'SOCIETY', 'full_desc': 'Society', 'legislation': 'BC Societies Act', 'version': 0},
            {'corp_type_cd': 'XS', 'colin_ind': 'Y', 'corp_class': 'SOC', 'short_desc': 'XPRO SOCIETY', 'full_desc': 'Extraprovincial Society', 'legislation': 'BC Societies Act', 'version': 0},
            {'corp_type_cd': 'SP', 'colin_ind': 'Y', 'corp_class': 'FIRM', 'short_desc': 'SOLE PROP', 'full_desc': 'Sole Proprietorship', 'legislation': 'BC Partnership Act', 'version': 0},
            {'corp_type_cd': 'GP', 'colin_ind': 'Y', 'corp_class': 'FIRM', 'short_desc': 'PARTNERSHIP', 'full_desc': 'General Partnership', 'legislation': 'BC Partnership Act', 'version': 0},
            {'corp_type_cd': 'LP', 'colin_ind': 'Y', 'corp_class': 'FIRM', 'short_desc': 'LIM PARTNERSHIP', 'full_desc': 'Limited Partnership', 'legislation': 'BC Partnership Act', 'version': 0},
            {'corp_type_cd': 'XP', 'colin_ind': 'Y', 'corp_class': 'FIRM', 'short_desc': 'XPRO LIM PARTNR', 'full_desc': 'Extraprovincial Limited Partnership', 'legislation': 'BC Partnership Act', 'version': 0},
            {'corp_type_cd': 'LL', 'colin_ind': 'Y', 'corp_class': 'FIRM', 'short_desc': 'LL PARTNERSHIP', 'full_desc': 'Limited Liability Partnership', 'legislation': 'BC Partnership Act', 'version': 0},
            {'corp_type_cd': 'XL', 'colin_ind': 'Y', 'corp_class': 'FIRM', 'short_desc': 'XPRO LL PARTNR', 'full_desc': 'Extrapro Limited Liability Partnership', 'legislation': 'BC Partnership Act', 'version': 0},
            {'corp_type_cd': 'MF', 'colin_ind': 'Y', 'corp_class': 'FIRM', 'short_desc': 'MISC FIRM', 'full_desc': 'Miscellaneous Firm', 'legislation': 'BC Partnership Act', 'version': 0},
            {'corp_type_cd': 'FI', 'colin_ind': 'N', 'corp_class': 'OT', 'short_desc': 'FINANCIAL', 'full_desc': 'Financial Institutions', 'legislation': 'Credit Union Incorporation Act', 'version': 0},
            {'corp_type_cd': 'CS', 'colin_ind': 'Y', 'corp_class': 'SOC', 'short_desc': 'CONT IN SOCIETY', 'full_desc': 'Society', 'legislation': 'BC Societies Act', 'version': 0},
            {'corp_type_cd': 'BEN', 'colin_ind': 'Y', 'corp_class': 'BC', 'short_desc': 'BENEFIT COMPANY', 'full_desc': 'BC Benefit Company', 'legislation': 'BC Business Corporations Act', 'version': 0}
        ]
    )


def downgrade():
    pass