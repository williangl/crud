from datetime import datetime

from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Table,
    Integer,
    String,
    DateTime)

engine = create_engine("sqlite:///base_new.db", echo=True)

metadata = MetaData(bind=engine)


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(40), nullable=False),
    Column("phone", String(10), nullable=False),
    Column("email", String, nullable=False),
    Column(
        "last_update",
        DateTime,
        default=datetime.now,
        onupdate=datetime.now),
    )

metadata.create_all()
