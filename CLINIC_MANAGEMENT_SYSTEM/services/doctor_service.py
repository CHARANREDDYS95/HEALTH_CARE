from sqlalchemy import select
from models.doctor_master import DoctorMaster
from connection import get_session
from utils.id_generator import generate_id
from utils.validators import (
    validate_required,
    validate_phone,
    validate_email,
    validate_gender,
    validate_status,
    validate_positive_number,
    validate_date_not_future
)


class DoctorService:

    @staticmethod
    def add_doctor(
        doctor_name,
        gender,
        dob,
        specialization,
        qualification,
        license_no,
        experience_years,
        phone,
        email,
        address,
        consultation_fee,

        joining_date
    ):

        validate_required(doctor_name, "Doctor Name")
        validate_required(specialization, "Specialization")
        validate_required(license_no, "License Number")

        validate_phone(phone)
        validate_email(email)
        validate_gender(gender)


        validate_positive_number(
            experience_years,
            "Experience Years"
        )

        validate_positive_number(
            consultation_fee,
            "Consultation Fee"
        )

        validate_date_not_future(dob)
        validate_date_not_future(joining_date)

        session = get_session()

        try:

            phone_exists = session.execute(
                select(DoctorMaster).where(
                    DoctorMaster.phone == phone
                )
            ).scalar_one_or_none()

            if phone_exists:
                raise ValueError(
                    "Phone number already exists"
                )

            email_exists = session.execute(
                select(DoctorMaster).where(
                    DoctorMaster.email == email
                )
            ).scalar_one_or_none()

            if email_exists:
                raise ValueError(
                    "Email already exists"
                )

            license_exists = session.execute(
                select(DoctorMaster).where(
                    DoctorMaster.license_no == license_no
                )
            ).scalar_one_or_none()

            if license_exists:
                raise ValueError(
                    "License number already exists"
                )

            doctor_id = generate_id(
                "DOCTOR_MASTER",
                "DOCTOR_ID",
                "D"
            )

            doctor = DoctorMaster(
                doctor_id=doctor_id,
                doctor_name=doctor_name,
                gender=gender,
                dob=dob,
                specialization=specialization,
                qualification=qualification,
                license_no=license_no,
                experience_years=experience_years,
                phone=phone,
                email=email,
                address=address,
                consultation_fee=consultation_fee,
                consultation_duration=12,
                doctor_status="ACTIVE",
                joining_date=joining_date
            )

            session.add(doctor)
            session.commit()

            return doctor_id

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
    @staticmethod
    def search_doctor(doctor_id):

        session = get_session()

        try:
            doctor = session.execute(
                select(DoctorMaster).where(
                    DoctorMaster.doctor_id == doctor_id
                    )
            ).scalar_one_or_none()

            return doctor
    
        finally:
            session.close()
            
    @staticmethod
    def search_doctor_by_id(
        doctor_id
    ):

        session = get_session()
        
        try:
            
            doctor = session.execute(
                select(DoctorMaster).where(
                    DoctorMaster.doctor_id == doctor_id
                )
            ).scalar_one_or_none()

            return doctor

        finally:
            session.close()
            
    @staticmethod
    def search_doctor_by_phone(
        phone
    ):

        session = get_session()

        try:

            doctor = session.execute(
                select(DoctorMaster).where(
                    DoctorMaster.phone == phone
                )
            ).scalar_one_or_none()

            return doctor

        finally:
            session.close()
    
    @staticmethod
    def search_doctor_by_license(
        license_no
    ):

        session = get_session()

        try:

            doctor = session.execute(
                select(DoctorMaster).where(
                    DoctorMaster.license_no == license_no
                )
            ).scalar_one_or_none()

            return doctor

        finally:
            session.close()
    
    @staticmethod
    def update_doctor(
        doctor_id,
        doctor_name,
        phone,
        email,
        address,
        consultation_fee,
        doctor_status
    ):

        session = get_session()    
        try:

            doctor = session.execute(
                select(DoctorMaster).where(
                    DoctorMaster.doctor_id == doctor_id
                )
            ).scalar_one_or_none()
            if not doctor:
                raise ValueError("Doctor not found")

            validate_phone(phone)
            validate_email(email)
            validate_status(doctor_status)

            validate_positive_number(
                consultation_fee,
                "Consultation Fee"
            )

            doctor.doctor_name = doctor_name
            doctor.phone = phone
            doctor.email = email
            doctor.address = address
            doctor.consultation_fee = consultation_fee
            doctor.doctor_status = doctor_status

            session.commit()

            return True

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
            
    @staticmethod
    def view_all_doctors():

        session = get_session()

        try:

            doctors = session.execute(
                select(
                    DoctorMaster
                ).order_by(
                    DoctorMaster.doctor_id
                )
            ).scalars().all()

            return doctors

        finally:
            session.close()

    @staticmethod
    def view_active_doctors():

        session = get_session()

        try:

            doctors = session.execute(

                select(

                    DoctorMaster

                ).where(

                    DoctorMaster.doctor_status
                    ==
                    "ACTIVE"

                )

            ).scalars().all()

            return doctors

        finally:

            session.close()
            
    @staticmethod
    def get_active_doctors():

        session = get_session()

        try:

            doctors = session.execute(

                select(
                    DoctorMaster
                ).where(

                    DoctorMaster.doctor_status
                    ==
                    "ACTIVE"

                ).order_by(

                    DoctorMaster.doctor_id

                )

            ).scalars().all()

            return doctors

        finally:

            session.close()

    @staticmethod
    def change_doctor_status(
        doctor_id,
        new_status
    ):

        session = get_session()

        try:

            doctor = session.execute(
                select(DoctorMaster).where(
                    DoctorMaster.doctor_id == doctor_id
                )
            ).scalar_one_or_none()

            if not doctor:

                raise ValueError(
                    "Doctor not found"
                )

            if doctor.doctor_status == new_status:

                raise ValueError(
                    f"Doctor is already {new_status}"
                )

            validate_status(
                new_status
            )

            doctor.doctor_status = new_status

            session.commit()

            return True

        except Exception:

            session.rollback()
            raise

        finally:

            session.close()
            
    @staticmethod
    def get_active_doctors():

        session = get_session()

        try:

            doctors = session.execute(
                select(
                    DoctorMaster
                ).where(
                    DoctorMaster.doctor_status == "ACTIVE"
                ).order_by(
                    DoctorMaster.doctor_id
                )
            ).scalars().all()

            return doctors

        finally:
            session.close()