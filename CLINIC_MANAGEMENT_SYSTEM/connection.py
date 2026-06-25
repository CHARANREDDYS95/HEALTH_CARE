from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USERNAME = "team40_charan"
PASSWORD = "team40_charan"

HOST = "ec2-3-111-0-185.ap-south-1.compute.amazonaws.com"
PORT = "1521"
SERVICE_NAME = "orcl"

DATABASE_URL = (
    f"oracle+oracledb://{USERNAME}:{PASSWORD}@"
    f"{HOST}:{PORT}/?service_name={SERVICE_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=False
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