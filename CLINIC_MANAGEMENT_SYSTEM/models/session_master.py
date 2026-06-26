from sqlalchemy import Column, String, Integer
from models.base import Base


class SessionMaster(Base):

    __tablename__ = "SESSION_MASTER"

    session_id = Column(
        "SESSION_ID",
        String(5),
        primary_key=True
    )

    session_name = Column(
        "SESSION_NAME",
        String(20),
        nullable=False
    )

    start_time = Column(
        "START_TIME",
        String(10),
        nullable=False
    )

    end_time = Column(
        "END_TIME",
        String(10),
        nullable=False
    )

    max_patients = Column(
        "MAX_PATIENTS",
        Integer,
        nullable=False
    )

    status = Column(
        "STATUS",
        String(10),
        nullable=False
    )
    
    room_id = Column(
        "ROOM_ID",
        String(5),
        nullable=False
    )