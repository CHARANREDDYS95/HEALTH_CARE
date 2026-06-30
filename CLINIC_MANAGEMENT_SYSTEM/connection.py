from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.config_reader import (
    ConfigReader
)

USERNAME = ConfigReader.get(
    "database.txt",
    "USERNAME"
)

PASSWORD = ConfigReader.get(
    "database.txt",
    "PASSWORD"
)

HOST = ConfigReader.get(
    "database.txt",
    "HOST"
)

PORT = ConfigReader.get(
    "database.txt",
    "PORT"
)

SERVICE_NAME = ConfigReader.get(
    "database.txt",
    "SERVICE_NAME"
)

DATABASE_URL = (
    f"oracle+oracledb://{USERNAME}:{PASSWORD}@"
    f"{HOST}:{PORT}/?service_name={SERVICE_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_engine():

    return engine


def get_session():

    return SessionLocal()