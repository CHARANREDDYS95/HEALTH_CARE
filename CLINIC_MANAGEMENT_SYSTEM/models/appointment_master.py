from sqlalchemy import Column, String, Date, Integer
from models.base import Base


class AppointmentMaster(Base):
    __tablename__ = "APPOINTMENT_MASTER"

    appointment_id = Column("APPOINTMENT_ID", String(10), primary_key=True)

    patient_id = Column("PATIENT_ID", String(10), nullable=False)

    doctor_id = Column("DOCTOR_ID", String(10), nullable=False)

    session_id = Column("SESSION_ID", String(5), nullable=False)

    appointment_date = Column("APPOINTMENT_DATE", Date, nullable=False)

    token_no = Column("TOKEN_NO", Integer)

    appointment_status = Column("APPOINTMENT_STATUS", String(20))

    booked_date = Column("BOOKED_DATE", Date)

    reason_for_visit = Column("REASON_FOR_VISIT", String(200))