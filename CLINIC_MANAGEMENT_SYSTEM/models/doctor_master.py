from sqlalchemy import Column, String, Date, Integer, Numeric
from models.base import Base


class DoctorMaster(Base):
    __tablename__ = "DOCTOR_MASTER"

    doctor_id = Column("DOCTOR_ID", String(10), primary_key=True)
    doctor_name = Column("DOCTOR_NAME", String(100), nullable=False)
    gender = Column("GENDER", String(10), nullable=False)
    dob = Column("DOB", Date, nullable=False)

    specialization = Column("SPECIALIZATION", String(100), nullable=False)
    qualification = Column("QUALIFICATION", String(100), nullable=False)
    license_no = Column("LICENSE_NO", String(50), nullable=False)

    experience_years = Column("EXPERIENCE_YEARS", Integer, nullable=False)

    phone = Column("PHONE", String(10), nullable=False)
    email = Column("EMAIL", String(100))

    address = Column("ADDRESS", String(200))

    consultation_fee = Column("CONSULTATION_FEE", Numeric(10, 2))
    consultation_duration = Column("CONSULTATION_DURATION", Integer)

    doctor_status = Column("DOCTOR_STATUS", String(20))
    joining_date = Column("JOINING_DATE", Date)