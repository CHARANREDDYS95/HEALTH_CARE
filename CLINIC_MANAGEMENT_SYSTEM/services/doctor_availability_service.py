from sqlalchemy import select
from connection import get_session
from utils.id_generator import generate_id
from utils.validators import (
    validate_required,
    validate_positive_number,
    validate_status,
    validate_day
)
from models.doctor_availability import DoctorAvailability
from models.doctor_master import DoctorMaster
from models.session_master import SessionMaster

class DoctorAvailabilityService:

    @staticmethod
    def assign_doctor(
        doctor_id,
        session_id,
        available_day,
        max_patients
    ):

        validate_required(
            doctor_id,
            "Doctor ID"
        )

        validate_required(
            session_id,
            "Session ID"
        )

        validate_required(
            available_day,
            "Available Day"
        )
        
        available_day = available_day.upper()

        validate_day(
            available_day
        )

        validate_positive_number(
            max_patients,
            "Max Patients"
        )

        session = get_session()

        try:

            doctor = session.execute(
                select(DoctorMaster).where(
                    DoctorMaster.doctor_id == doctor_id
                )
            ).scalar_one_or_none()

            if not doctor:

                raise ValueError(
                    "DOCTOR NOT FOUND"
                )

            if doctor.doctor_status != "ACTIVE":

                raise ValueError(
                    "DOCTOR IS INACTIVE"
                )

            session_master = session.execute(
                select(SessionMaster).where(
                    SessionMaster.session_id == session_id
                )
            ).scalar_one_or_none()

            if not session_master:

                raise ValueError(
                    "SESSION NOT FOUND"
                )

            if session_master.status != "ACTIVE":

                raise ValueError(
                    "SESSION IS INACTIVE"
                )

            duplicate = session.execute(
                select(DoctorAvailability).where(
                    DoctorAvailability.doctor_id == doctor_id,
                    DoctorAvailability.session_id == session_id,
                    DoctorAvailability.available_day == available_day
                )
            ).scalar_one_or_none()

            if duplicate:

                raise ValueError(
                    "DOCTOR IS ALREADY ASSIGNED TO THIS SESSION"
                )

            if max_patients > session_master.max_patients:

                raise ValueError(
                    "MAX PATIENTS EXCEEDS SESSION LIMIT"
                )

            availability_id = generate_id(
                "DOCTOR_AVAILABILITY",
                "AVAILABILITY_ID",
                "A"
            )

            availability = DoctorAvailability(
                availability_id=availability_id,
                doctor_id=doctor_id,
                session_id=session_id,
                available_day=available_day,
                max_patients=max_patients,
                status="ACTIVE"
            )

            session.add(
                availability
            )

            session.commit()

            return availability_id

        except Exception:

            session.rollback()
            raise

        finally:

            session.close()
    @staticmethod
    def search_availability_by_id(
        availability_id
    ):

        session = get_session()

        try:

            availability = session.execute(
                select(
                    DoctorAvailability
                ).where(
                    DoctorAvailability.availability_id
                    == availability_id
                )
            ).scalar_one_or_none()

            return availability

        finally:

            session.close()

    @staticmethod
    def search_availability_by_doctor(
        doctor_id
    ):

        session = get_session()

        try:

            availability = session.execute(
                select(
                    DoctorAvailability
                ).where(
                    DoctorAvailability.doctor_id
                    == doctor_id
                )
            ).scalars().all()

            return availability

        finally:

            session.close()

    @staticmethod
    def search_availability_by_session(
        session_id
    ):

        session = get_session()

        try:

            availability = session.execute(
                select(
                    DoctorAvailability
                ).where(
                    DoctorAvailability.session_id
                    == session_id
                )
            ).scalars().all()

            return availability

        finally:

            session.close()

    @staticmethod
    def search_availability_by_day(
        available_day
    ):

        available_day = available_day.upper()

        validate_day(
            available_day
        )

        session = get_session()

        try:

            availability = session.execute(
                select(
                    DoctorAvailability
                ).where(
                    DoctorAvailability.available_day
                    == available_day
                )
            ).scalars().all()

            return availability

        finally:

            session.close()
            
    @staticmethod
    def view_all_availability():

        session = get_session()

        try:

            availability_list = session.execute(
                select(
                    DoctorAvailability
                )
            ).scalars().all()

            return availability_list

        finally:

            session.close()

    @staticmethod
    def view_active_availability():

        session = get_session()

        try:

            availability_list = session.execute(
                select(
                    DoctorAvailability
                ).where(
                    DoctorAvailability.status
                    == "ACTIVE"
                )
            ).scalars().all()

            return availability_list

        finally:

            session.close()

    @staticmethod
    def view_inactive_availability():

        session = get_session()

        try:

            availability_list = session.execute(
                select(
                    DoctorAvailability
                ).where(
                    DoctorAvailability.status
                    == "INACTIVE"
                )
            ).scalars().all()

            return availability_list

        finally:

            session.close()
            
    @staticmethod
    def update_availability(
        availability_id,
        doctor_id,
        session_id,
        available_day,
        max_patients
    ):

        validate_required(
            doctor_id,
            "Doctor ID"
        )

        validate_required(
            session_id,
            "Session ID"
        )

        validate_required(
            available_day,
            "Available Day"
        )
        
        available_day = available_day.upper()

        validate_day(
            available_day
        )
        
        validate_positive_number(
            max_patients,
            "Max Patients"
        )

        session = get_session()

        try:

            availability = session.execute(
                select(
                    DoctorAvailability
                ).where(
                    DoctorAvailability.availability_id
                    == availability_id
                )
            ).scalar_one_or_none()

            if not availability:

                raise ValueError(
                    "AVAILABILITY NOT FOUND"
                )

            doctor = session.execute(
                select(
                    DoctorMaster
                ).where(
                    DoctorMaster.doctor_id
                    == doctor_id
                )
            ).scalar_one_or_none()

            if not doctor:

                raise ValueError(
                    "DOCTOR NOT FOUND"
                )

            if doctor.doctor_status != "ACTIVE":

                raise ValueError(
                    "DOCTOR IS INACTIVE"
                )

            session_master = session.execute(
                select(
                    SessionMaster
                ).where(
                    SessionMaster.session_id
                    == session_id
                )
            ).scalar_one_or_none()

            if not session_master:

                raise ValueError(
                    "SESSION NOT FOUND"
                )

            if session_master.status != "ACTIVE":

                raise ValueError(
                    "SESSION IS INACTIVE"
                )

            duplicate = session.execute(
                select(
                    DoctorAvailability
                ).where(
                    DoctorAvailability.doctor_id
                    == doctor_id,
                    DoctorAvailability.session_id
                    == session_id,
                    DoctorAvailability.available_day
                    == available_day,
                    DoctorAvailability.availability_id
                    != availability_id
                )
            ).scalar_one_or_none()

            if duplicate:

                raise ValueError(
                    "DOCTOR IS ALREADY ASSIGNED TO THIS SESSION"
                )

            if max_patients > session_master.max_patients:

                raise ValueError(
                    "MAX PATIENTS EXCEEDS SESSION LIMIT"
                )

            availability.doctor_id = doctor_id
            availability.session_id = session_id
            availability.available_day = available_day
            availability.max_patients = max_patients

            session.commit()

            return True

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()

    @staticmethod
    def change_availability_status(
        availability_id,
        status
    ):

        validate_status(
            status
        )

        session = get_session()

        try:

            availability = session.execute(
                select(
                    DoctorAvailability
                ).where(
                    DoctorAvailability.availability_id
                    == availability_id
                )
            ).scalar_one_or_none()

            if not availability:

                raise ValueError(
                    "AVAILABILITY NOT FOUND"
                )

            if availability.status == status:

                raise ValueError(
                    "STATUS IS ALREADY " + status
                )

            availability.status = status

            session.commit()

            return True

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()
            
    @staticmethod
    def get_available_by_date(
        appointment_date
    ):

        session = get_session()

        try:

            available_day = (
                appointment_date.strftime(
                    "%A"
                ).upper()
            )

            availability = session.execute(
                select(
                    DoctorAvailability,
                    DoctorMaster.doctor_name,
                    SessionMaster.session_name,
                    SessionMaster.room_id,
                    SessionMaster.start_time,
                    SessionMaster.end_time
                ).join(
                    DoctorMaster,
                    DoctorAvailability.doctor_id
                    == DoctorMaster.doctor_id
                ).join(
                    SessionMaster,
                    DoctorAvailability.session_id
                    == SessionMaster.session_id
                ).where(
                    DoctorAvailability.available_day
                    == available_day,

                    DoctorAvailability.status
                    == "ACTIVE"
                ).order_by(
                    SessionMaster.start_time
                )
            ).all()

            return availability

        finally:

            session.close()