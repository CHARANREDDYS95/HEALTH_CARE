from sqlalchemy import Column, String, Integer
from models.base import Base


class DoctorAvailability(Base):
    __tablename__ = "DOCTOR_AVAILABILITY"

    availability_id = Column("AVAILABILITY_ID", String(10), primary_key=True)
    doctor_id = Column("DOCTOR_ID", String(10), nullable=False)
    session_id = Column("SESSION_ID", String(10), nullable=False)
    available_day = Column("AVAILABLE_DAY", String(20), nullable=False)
    max_patients = Column("MAX_PATIENTS", Integer)
    status = Column("STATUS", String(20))