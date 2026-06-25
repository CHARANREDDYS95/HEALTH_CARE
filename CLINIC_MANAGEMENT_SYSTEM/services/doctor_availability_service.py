from sqlalchemy import select
from connection import get_session
from datetime import date, timedelta
from models.session_master import SessionMaster
from models.doctor_availability import (
    DoctorAvailability
)


class DoctorAvailabilityService:

    @staticmethod
    def get_available_sessions(
        doctor_id,
        appointment_date
    ):

        session = get_session()

        try:

            day_name = (
                appointment_date
                .strftime("%A")
                .upper()
            )

            sessions = session.execute(
                select(
                    SessionMaster.session_id,
                    SessionMaster.start_time,
                    SessionMaster.end_time
                )
                .join(
                    DoctorAvailability,
                    DoctorAvailability.session_id
                    == SessionMaster.session_id
                )
                .where(
                    DoctorAvailability.doctor_id
                    == doctor_id,

                    DoctorAvailability.available_day
                    == day_name,

                    DoctorAvailability.status
                    == "ACTIVE"
                )
                .order_by(
                    SessionMaster.session_id
                )
            ).all()

            return sessions

        finally:
            session.close()
            
    @staticmethod
    def get_next_available_dates(
            doctor_id
            ):

        session = get_session()
        
        try:

            days = session.execute(
                select(
                    DoctorAvailability.available_day
                )
                .where(
                    DoctorAvailability.doctor_id
                    == doctor_id,

                    DoctorAvailability.status
                    == "ACTIVE"
                )
                .distinct()
            ).scalars().all()

            next_dates = []

            current_date = date.today()

            for i in range(0, 60):

                check_date = (
                    current_date
                    + timedelta(days=i)
                )

                day_name = (
                    check_date
                    .strftime("%A")
                    .upper()
                )

                if day_name in days:

                    next_dates.append(
                        check_date
                    )

                if len(next_dates) == 3:
                    break

            return next_dates

        finally:
            session.close()