from sqlalchemy import select
from datetime import datetime
from models.session_master import SessionMaster
from connection import get_session
from utils.id_generator import generate_id
from utils.validators import (
    validate_required,
    validate_status,
    validate_room,
    validate_time
)


from utils.appointment_slot_generator import (
    AppointmentSlotGenerator
)


class SessionService:

    @staticmethod
    def add_session(
        session_name,
        room_id,
        start_time,
        end_time
    ):

        validate_required(
            session_name,
            "Session Name"
        )

        validate_required(
            start_time,
            "Start Time"
        )

        validate_required(
            end_time,
            "End Time"
        )

        validate_room(
            room_id
        )

        validate_time(
            start_time
        )

        validate_time(
            end_time
        )

        new_start = datetime.strptime(
            start_time,
            "%I:%M %p"
        )

        new_end = datetime.strptime(
            end_time,
            "%I:%M %p"
        )

        if new_start >= new_end:

            raise ValueError(
                "START TIME MUST BE BEFORE END TIME"
            )

        slot_details = (

            AppointmentSlotGenerator.generate_slots(

                start_time,

                end_time

            )

        )

        max_patients = (

            slot_details[
                "max_patients"
            ]

        )

        max_patients = slot_details[
            "max_patients"
        ]

        session = get_session()

        try:

            session_exists = session.execute(
                select(
                    SessionMaster
                ).where(
                    SessionMaster.session_name
                    ==
                    session_name
                )
            ).scalar_one_or_none()

            if session_exists:

                raise ValueError(
                    "SESSION NAME ALREADY EXISTS"
                )

            existing_sessions = session.execute(
                select(
                    SessionMaster
                ).where(
                    SessionMaster.room_id
                    ==
                    room_id,

                    SessionMaster.status
                    ==
                    "ACTIVE"
                )
            ).scalars().all()

            for existing in existing_sessions:

                existing_start = datetime.strptime(
                    existing.start_time,
                    "%I:%M %p"
                )

                existing_end = datetime.strptime(
                    existing.end_time,
                    "%I:%M %p"
                )

                if (

                    new_start < existing_end

                    and

                    new_end > existing_start

                ):

                    raise ValueError(
                        "SESSION TIME OVERLAPS WITH AN EXISTING SESSION"
                    )

            session_id = generate_id(

                "SESSION_MASTER",

                "SESSION_ID",

                "S"

            )

            session_master = SessionMaster(

                session_id=session_id,

                session_name=session_name,

                room_id=room_id,

                start_time=start_time,

                end_time=end_time,

                max_patients=max_patients,

                status="ACTIVE"

            )

            session.add(
                session_master
            )

            session.commit()

            return {

                "session_id":

                session_id,

                "max_patients":

                slot_details[
                    "max_patients"
                ],

                "consultation_duration":

                slot_details[
                    "consultation_duration"
                ],

                "session_duration":

                slot_details[
                    "session_duration"
                ],

                "distributed_minutes":

                slot_details[
                    "distributed_minutes"
                ]

            }

            

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()

    @staticmethod
    def search_session_by_id(
        session_id
    ):

        session = get_session()

        try:

            session_master = session.execute(
                select(SessionMaster).where(
                    SessionMaster.session_id == session_id
                )
            ).scalar_one_or_none()

            return session_master

        finally:

            session.close()

    @staticmethod
    def search_session_by_name(
        session_name
    ):

        session = get_session()

        try:

            session_master = session.execute(
                select(SessionMaster).where(
                    SessionMaster.session_name == session_name
                )
            ).scalar_one_or_none()

            return session_master

        finally:

            session.close()

    @staticmethod
    def view_all_sessions():

        session = get_session()

        try:

            sessions = session.execute(
                select(
                    SessionMaster
                ).order_by(
                    SessionMaster.session_id
                )
            ).scalars().all()

            return sessions

        finally:

            session.close()

    @staticmethod
    def update_session(
        session_id,
        session_name,
        room_id,
        start_time,
        end_time
    ):

        validate_required(
            session_id,
            "Session ID"
        )

        validate_required(
            session_name,
            "Session Name"
        )

        validate_required(
            start_time,
            "Start Time"
        )

        validate_required(
            end_time,
            "End Time"
        )

        validate_room(
            room_id
        )

        validate_time(
            start_time
        )

        validate_time(
            end_time
        )

        new_start = datetime.strptime(
            start_time,
            "%I:%M %p"
        )

        new_end = datetime.strptime(
            end_time,
            "%I:%M %p"
        )

        if new_start >= new_end:

            raise ValueError(
                "START TIME MUST BE BEFORE END TIME"
            )

        slot_details = (

            AppointmentSlotGenerator.generate_slots(

                start_time,

                end_time

            )

        )

        max_patients = (

            slot_details[
                "max_patients"
            ]

        )

        session = get_session()

        try:

            session_master = session.execute(
                select(
                    SessionMaster
                ).where(
                    SessionMaster.session_id
                    ==
                    session_id
                )
            ).scalar_one_or_none()

            if not session_master:

                raise ValueError(
                    "SESSION NOT FOUND"
                )

            duplicate = session.execute(
                select(
                    SessionMaster
                ).where(
                    SessionMaster.session_name
                    ==
                    session_name,

                    SessionMaster.session_id
                    !=
                    session_id
                )
            ).scalar_one_or_none()

            if duplicate:

                raise ValueError(
                    "SESSION NAME ALREADY EXISTS"
                )

            existing_sessions = session.execute(
                select(
                    SessionMaster
                ).where(
                    SessionMaster.room_id
                    ==
                    room_id,

                    SessionMaster.status
                    ==
                    "ACTIVE",

                    SessionMaster.session_id
                    !=
                    session_id
                )
            ).scalars().all()

            for existing in existing_sessions:

                existing_start = datetime.strptime(
                    existing.start_time,
                    "%I:%M %p"
                )

                existing_end = datetime.strptime(
                    existing.end_time,
                    "%I:%M %p"
                )

                if (

                    new_start < existing_end

                    and

                    new_end > existing_start

                ):

                    raise ValueError(
                        "SESSION TIME OVERLAPS WITH AN EXISTING SESSION"
                    )

            session_master.session_name = (
                session_name
            )

            session_master.room_id = (
                room_id
            )

            session_master.start_time = (
                start_time
            )

            session_master.end_time = (
                end_time
            )

            session_master.max_patients = (
                max_patients
            )

            session.commit()

            return {

                "max_patients":

                slot_details[
                    "max_patients"
                ],

                "consultation_duration":

                slot_details[
                    "consultation_duration"
                ],

                "session_duration":

                slot_details[
                    "session_duration"
                ],

                "distributed_minutes":

                slot_details[
                    "distributed_minutes"
                ]

            }

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()

    @staticmethod
    def change_session_status(
        session_id,
        status
    ):

        session = get_session()

        try:

            session_master = session.execute(
                select(SessionMaster).where(
                    SessionMaster.session_id == session_id
                )
            ).scalar_one_or_none()

            if not session_master:
                raise ValueError(
                    "Session not found"
                )

            validate_status(
                status
            )

            session_master.status = status

            session.commit()

            return True

        except Exception:

            session.rollback()
            raise

        finally:

            session.close()