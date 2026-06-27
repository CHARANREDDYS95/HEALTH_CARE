from sqlalchemy import select, or_
from models.patient_master import PatientMaster
from connection import get_session
from utils.id_generator import generate_id
from utils.validators import (
    validate_required,
    validate_phone,
    validate_gender,
    validate_date_not_future,
    validate_blood_group
)

class PatientService:

    @staticmethod
    def register_patient(
        patient_name,
        gender,
        dob,
        phone,
        address,
        city,
        blood_group,
        occupation,
        marital_status,
        allergies,
        emergency_contact_name,
        emergency_phone,
        registration_date
    ):

        validate_required(patient_name, "Patient Name")

        validate_phone(phone)
        validate_gender(gender)
        validate_date_not_future(dob)
        validate_blood_group(blood_group)

        session = get_session()

        try:

            phone_exists = session.execute(
                select(PatientMaster).where(
                    PatientMaster.phone == phone
                )
            ).scalar_one_or_none()

            if phone_exists:
                raise ValueError(
                    "Phone number already exists"
                )

            patient_id = generate_id(
                "PATIENT_MASTER",
                "PATIENT_ID",
                "P"
            )

            patient = PatientMaster(
                patient_id=patient_id,
                patient_name=patient_name,
                gender=gender,
                dob=dob,
                phone=phone,
                address=address,
                city=city,
                blood_group=blood_group,
                occupation=occupation,
                marital_status=marital_status,
                allergies=allergies,
                emergency_contact_name=emergency_contact_name,
                emergency_phone=emergency_phone,
                registration_date=registration_date,
                patient_status="ACTIVE"
            )

            session.add(patient)
            session.commit()

            return patient_id

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    @staticmethod
    def search_patient(search_value):

        session = get_session()

        try:

            patient = session.execute(
                select(PatientMaster).where(
                    or_(
                        PatientMaster.patient_id == search_value,
                        PatientMaster.phone == search_value
                    )
                )
            ).scalar_one_or_none()

            return patient

        finally:
            session.close()
            
    @staticmethod
    def search_patient_by_id(
        patient_id
    ):

        session = get_session()

        try:

            patient = session.execute(
                select(PatientMaster).where(
                    PatientMaster.patient_id == patient_id
                )
            ).scalar_one_or_none()

            return patient

        finally:
            session.close()
        
    @staticmethod
    def search_patient_by_phone(
        phone
    ):

        session = get_session()
        
        try:

            patient = session.execute(
                select(PatientMaster).where(
                    PatientMaster.phone == phone
                )
            ).scalar_one_or_none()

            return patient

        finally:
            session.close()
                           
    @staticmethod
    def view_all_patients():

        session = get_session()

        try:

            return session.execute(
                select(
                    PatientMaster
                ).order_by(
                    PatientMaster.patient_id
                )
            ).scalars().all()

        finally:
            session.close()
            
    @staticmethod
    def get_active_patients():

        session = get_session()

        try:

            patients = session.execute(
                select(
                    PatientMaster
                ).where(
                    PatientMaster.patient_status
                    == "ACTIVE"
                ).order_by(
                    PatientMaster.patient_name
                )
            ).scalars().all()

            return patients

        finally:

            session.close()
            
    @staticmethod
    def update_patient(
        patient_id,
        patient_name,
        phone,
        address,
        city,
        occupation,
        marital_status,
        allergies,
        emergency_contact_name,
        emergency_phone,
        patient_status
    ):

        session = get_session()

        try:

            patient = session.execute(
                select(PatientMaster).where(
                    PatientMaster.patient_id == patient_id
                )
            ).scalar_one_or_none()

            if not patient:
                raise ValueError("Patient not found")

            validate_phone(phone)

            patient.patient_name = patient_name
            patient.phone = phone
            patient.address = address
            patient.city = city
            patient.occupation = occupation
            patient.marital_status = marital_status
            patient.allergies = allergies
            patient.emergency_contact_name = emergency_contact_name
            patient.emergency_phone = emergency_phone
            patient.patient_status = patient_status

            session.commit()

            return True

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    @staticmethod
    def delete_patient(patient_id):

        session = get_session()

        try:

            patient = session.execute(
                select(PatientMaster).where(
                    PatientMaster.patient_id == patient_id
                )
            ).scalar_one_or_none()

            if not patient:
                raise ValueError("Patient not found")

            patient.patient_status = "INACTIVE"

            session.commit()

            return True

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
