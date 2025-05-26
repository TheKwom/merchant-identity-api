from sqlalchemy import Table, Column, Integer, String, Boolean
from app.database import metadata

merchants = Table(
    "merchants",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("website", String(255)),
    Column("address", String(255)),
    Column("verified_identity", Boolean, default=False),
    Column("risk_score", Integer, default=0),
    Column("high_risk", Boolean, default=False),
)
