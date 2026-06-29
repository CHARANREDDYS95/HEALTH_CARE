from sqlalchemy import (
    select,
    case
)
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
from datetime import date, timedelta

class DoctorAvailabilityService:

    @staticmethod
    def validate_overlapping_session(
        existing_session_id,
        new_session_id
    ):

        if (
            existing_session_id == "S001"
            and
            new_session_id == "S002"
        ) or (
            existing_session_id == "S002"
            and
            new_session_id == "S001"
        ):

            raise ValueError(
                "DOCTOR ALREADY HAS AN OVERLAPPING MORNING SESSION"
            )

        if (
            existing_session_id == "S003"
            and
            new_session_id == "S004"
        ) or (
            existing_session_id == "S004"
            and
            new_session_id == "S003"
        ):

            raise ValueError(
                "DOCTOR ALREADY HAS AN OVERLAPPING EVENING SESSION"
            )    

    @staticmethod
    def _is_overlapping_session(
        session1,
        session2
    ):

        overlapping_sessions = {

            "S001": ["S002"],

            "S002": ["S001"],

            "S003": ["S004"],

            "S004": ["S003"]

        }

        return (
            session2
            in
            overlapping_sessions.get(
                session1,
                []
            )
        )
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
            existing_schedule = session.execute(

                select(
                    DoctorAvailability
                ).where(

                    DoctorAvailability.doctor_id
                    == doctor_id,

                    DoctorAvailability.available_day
                    == available_day,

                    DoctorAvailability.status
                    == "ACTIVE"

                )

            ).scalars().all()

            for schedule in existing_schedule:

                DoctorAvailabilityService.validate_overlapping_session(

                    schedule.session_id,

                    session_id

                )
            if max_patients > session_master.max_patients:

                raise ValueError(
                    "MAX PATIENTS EXCEEDS SESSION LIMIT"
                )

            availability_id = generate_id(
                "DOCTOR_AVAILABILITY",
                "AVAILABILITY_ID",
                "DA"
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
            existing_schedule = session.execute(

                select(
                    DoctorAvailability
                ).where(

                    DoctorAvailability.doctor_id
                    == doctor_id,

                    DoctorAvailability.available_day
                    == available_day,

                    DoctorAvailability.status
                    == "ACTIVE",

                    DoctorAvailability.availability_id
                    != availability_id

                )

            ).scalars().all()

            for schedule in existing_schedule:

                DoctorAvailabilityService.validate_overlapping_session(

                    schedule.session_id,

                    session_id

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
                    SessionMaster.session_id
                )
            ).all()

            return availability

        finally:

            session.close()

    @staticmethod
    def get_next_available_dates(
        doctor_id
    ):

        session = get_session()

        try:

            availability = session.execute(

                select(
                    DoctorAvailability
                ).where(
                    DoctorAvailability.doctor_id
                    == doctor_id,

                    DoctorAvailability.status
                    == "ACTIVE"
                )

            ).scalars().all()

            if not availability:

                return []

            available_days = [

                doctor.available_day

                for doctor in availability

            ]

            next_dates = []

            current_date = date.today()

            while len(
                next_dates
            ) < 3:

                if (

                    current_date.strftime(
                        "%A"
                    ).upper()

                    in

                    available_days

                ):

                    next_dates.append(
                        current_date
                    )

                current_date += timedelta(
                    days=1
                )

            return next_dates

        finally:

            session.close()
            
    @staticmethod
    def get_doctor_availability(
        doctor_id
    ):

        session = get_session()

        try:

            availability = session.execute(

                select(
                    DoctorAvailability
                ).where(

                    DoctorAvailability.doctor_id
                    == doctor_id,

                    DoctorAvailability.status
                    == "ACTIVE"

                ).order_by(

                    DoctorAvailability.available_day,

                    DoctorAvailability.session_id

                )

            ).scalars().all()

            return availability

        finally:

            session.close()
            
    @staticmethod
    def get_doctor_sessions_by_date(
        doctor_id,
        appointment_date
    ):

        session = get_session()

        try:

            available_day = (
                appointment_date.strftime(
                    "%A"
                ).upper()
            )

            sessions = session.execute(

                select(

                    DoctorAvailability,

                    SessionMaster.session_name,

                    SessionMaster.room_id,

                    SessionMaster.start_time,

                    SessionMaster.end_time

                ).join(

                    SessionMaster,

                    DoctorAvailability.session_id
                    ==
                    SessionMaster.session_id

                ).where(

                    DoctorAvailability.doctor_id
                    ==
                    doctor_id,

                    DoctorAvailability.available_day
                    ==
                    available_day,

                    DoctorAvailability.status
                    ==
                    "ACTIVE"

                ).order_by(

                    SessionMaster.start_time

                )

            ).all()

            return sessions

        finally:

            session.close()
            
    @staticmethod
    def get_doctor_schedule(
        doctor_id
    ):

        validate_required(
            doctor_id,
            "Doctor ID"
        )

        session = get_session()

        try:

            doctor = session.execute(
                select(
                    DoctorMaster
                ).where(
                    DoctorMaster.doctor_id
                    ==
                    doctor_id
                )
            ).scalar_one_or_none()

            if not doctor:

                raise ValueError(
                    "DOCTOR NOT FOUND"
                )

            schedules = session.execute(

                select(
                    DoctorAvailability,
                    SessionMaster
                ).join(
                    SessionMaster,
                    DoctorAvailability.session_id
                    ==
                    SessionMaster.session_id
                ).where(
                    DoctorAvailability.doctor_id
                    ==
                    doctor_id
                ).order_by(

                    case(

                        (

                            DoctorAvailability.available_day
                            == "MONDAY",

                            1

                        ),

                        (

                            DoctorAvailability.available_day
                            == "TUESDAY",

                            2

                        ),

                        (

                            DoctorAvailability.available_day
                            == "WEDNESDAY",

                            3

                        ),

                        (

                            DoctorAvailability.available_day
                            == "THURSDAY",

                            4

                        ),

                        (

                            DoctorAvailability.available_day
                            == "FRIDAY",

                            5

                        ),

                        (

                            DoctorAvailability.available_day
                            == "SATURDAY",

                            6

                        ),

                        else_=7

                    ),

                    SessionMaster.start_time

                )

            ).all()

            return schedules

        finally:

            session.close()