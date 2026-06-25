from sqlalchemy import Column, String
from models.base import Base


class SessionMaster(Base):
    __tablename__ = "SESSION_MASTER"

    session_id = Column("SESSION_ID", String(5), primary_key=True)

    session_name = Column("SESSION_NAME", String(20), nullable=False)

    start_time = Column("START_TIME", String(10), nullable=False)

    end_time = Column("END_TIME", String(10), nullable=False)

    status = Column("STATUS", String(10))