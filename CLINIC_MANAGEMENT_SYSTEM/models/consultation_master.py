from sqlalchemy import Column, String, TIMESTAMP
from models.base import Base


class ConsultationMaster(Base):
    __tablename__ = "CONSULTATION_MASTER"

    consultation_id = Column(
        "CONSULTATION_ID",
        String(10),
        primary_key=True
    )

    appointment_id = Column(
        "APPOINTMENT_ID",
        String(10),
        nullable=False
    )

    consultation_start_time = Column(
        "CONSULTATION_START_TIME",
        TIMESTAMP
    )

    consultation_end_time = Column(
        "CONSULTATION_END_TIME",
        TIMESTAMP
    )

    symptoms = Column(
        "SYMPTOMS",
        String(1000)
    )

    diagnosis = Column(
        "DIAGNOSIS",
        String(1000)
    )

    prescription = Column(
        "PRESCRIPTION",
        String(2000)
    )

    notes = Column(
        "NOTES",
        String(1000)
    )
    
    followup_required = Column(
        "FOLLOWUP_REQUIRED",
        String(3)
    )

    followup_date = Column(
        "FOLLOWUP_DATE",
        TIMESTAMP
    )
    
    followup_required = Column(
        "FOLLOWUP_REQUIRED",
        String(3)
    )

    followup_date = Column(
        "FOLLOWUP_DATE",
        TIMESTAMP
    )

    consultation_status = Column(
        "CONSULTATION_STATUS",
        String(20)
    )