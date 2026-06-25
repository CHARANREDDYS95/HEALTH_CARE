from sqlalchemy import Column, String, Date
from models.base import Base


class PatientMaster(Base):
    __tablename__ = "PATIENT_MASTER"

    patient_id = Column("PATIENT_ID", String(10), primary_key=True)

    patient_name = Column("PATIENT_NAME", String(100), nullable=False)

    gender = Column("GENDER", String(1), nullable=False)

    dob = Column("DOB", Date, nullable=False)

    phone = Column("PHONE", String(15), nullable=False)

    address = Column("ADDRESS", String(200))

    city = Column("CITY", String(50))

    blood_group = Column("BLOOD_GROUP", String(5))

    occupation = Column("OCCUPATION", String(100))

    marital_status = Column("MARITAL_STATUS", String(20))

    allergies = Column("ALLERGIES", String(500))

    emergency_contact_name = Column(
        "EMERGENCY_CONTACT_NAME",
        String(100)
    )

    emergency_phone = Column("EMERGENCY_PHONE", String(15))

    registration_date = Column("REGISTRATION_DATE", Date)

    patient_status = Column("PATIENT_STATUS", String(20))