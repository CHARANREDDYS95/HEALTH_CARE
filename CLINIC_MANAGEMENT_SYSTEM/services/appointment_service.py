from datetime import date
from sqlalchemy import select
from connection import get_session
from utils.id_generator import generate_id
from utils.validators import (
    validate_required,
    validate_future_date
)
from models.appointment_master import AppointmentMaster
from models.patient_master import PatientMaster
from models.doctor_availability import DoctorAvailability
from models.doctor_master import DoctorMaster
from models.session_master import SessionMaster
from datetime import datetime, timedelta
from config.config_reader import (
    ConfigReader
)

CONSULTATION_DURATION = int(
    ConfigReader.get(
        "consultation_duration.txt",
        "CONSULTATION_DURATION"
    )
)

class AppointmentService:

    @staticmethod
    def book_appointment(
        patient_id,
        availability_id,
        appointment_date,
        token_no,
        reason_for_visit
    ):

        validate_required(
            patient_id,
            "Patient ID"
        )

        validate_required(
            availability_id,
            "Availability ID"
        )

        validate_required(
            reason_for_visit,
            "Reason For Visit"
        )

        reason_for_visit = (
            reason_for_visit.strip()
        )

        validate_future_date(
            appointment_date
        )
        
        session = get_session()

        try:

            patient = session.execute(
                select(
                    PatientMaster
                ).where(
                    PatientMaster.patient_id
                    == patient_id
                )
            ).scalar_one_or_none()

            if not patient:

                raise ValueError(
                    "PATIENT NOT FOUND"
                )

            if patient.patient_status != "ACTIVE":

                raise ValueError(
                    "PATIENT IS INACTIVE"
                )
            existing = session.execute(
                select(
                    AppointmentMaster
                ).where(
                    AppointmentMaster.patient_id
                    == patient_id,

                    AppointmentMaster.appointment_date
                    == appointment_date,

                    AppointmentMaster.appointment_status
                    == "BOOKED"
                )
            ).scalar_one_or_none()

            if existing:

                raise ValueError(
                    "PATIENT ALREADY HAS AN APPOINTMENT ON THIS DATE"
                )

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
                    "DOCTOR AVAILABILITY NOT FOUND"
                )

            if availability.status != "ACTIVE":

                raise ValueError(
                    "DOCTOR AVAILABILITY IS INACTIVE"
                )
            if appointment_date.strftime(
                "%A"
            ).upper() != availability.available_day:

                raise ValueError(
                    "DOCTOR IS NOT AVAILABLE ON THE SELECTED DATE"
                )

            if (
                token_no < 1
                or
                token_no > availability.max_patients
            ):

                raise ValueError(
                    "INVALID TOKEN NUMBER"
                )

            token_exists = session.execute(
                select(
                    AppointmentMaster
                ).where(
                    AppointmentMaster.availability_id
                    == availability_id,

                    AppointmentMaster.appointment_date
                    == appointment_date,

                    AppointmentMaster.token_no
                    == token_no,

                    AppointmentMaster.appointment_status
                    == "BOOKED"
                )
            ).scalar_one_or_none()

            if token_exists:

                raise ValueError(
                    "TOKEN ALREADY BOOKED"
                )

            appointment_id = generate_id(
                "APPOINTMENT_MASTER",
                "APPOINTMENT_ID",
                "A"
            )

            appointment = AppointmentMaster(
                appointment_id=appointment_id,
                patient_id=patient_id,
                availability_id=availability_id,
                appointment_date=appointment_date,
                token_no=token_no,
                booked_date=date.today(),
                reason_for_visit=reason_for_visit,
                appointment_status="BOOKED"
            )

            session.add(
                appointment
            )

            session.commit()

            return (
                appointment_id,
                token_no
            )

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()
            
    @staticmethod
    def get_session_tokens(
        availability_id,
        appointment_date
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

            if not availability:

                raise ValueError(
                    "DOCTOR AVAILABILITY NOT FOUND"
                )

            session_master = session.execute(
                select(
                    SessionMaster
                ).where(
                    SessionMaster.session_id
                    == availability.session_id
                )
            ).scalar_one()

            booked_tokens = session.execute(
                select(
                    AppointmentMaster.token_no
                ).where(
                    AppointmentMaster.availability_id
                    == availability_id,

                    AppointmentMaster.appointment_date
                    == appointment_date,

                    AppointmentMaster.appointment_status
                    == "BOOKED"
                )
            ).scalars().all()

            start_time = datetime.strptime(
                session_master.start_time,
                "%I:%M %p"
            )

            tokens = []

            for token in range(
                1,
                session_master.max_patients + 1
            ):

                consultation_time = (
                    start_time
                    +
                    timedelta(
                        minutes=(
                            token - 1
                        ) * CONSULTATION_DURATION
                    )
                ).strftime(
                    "%I:%M %p"
                )

                status = (
                    "BOOKED"
                    if token in booked_tokens
                    else "AVAILABLE"
                )

                tokens.append(

                    (
                        token,
                        consultation_time,
                        status
                    )

                )

            return tokens

        finally:

            session.close()
            
    @staticmethod
    def get_token_status(
        availability_id,
        appointment_date
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

            if not availability:

                raise ValueError(
                    "DOCTOR AVAILABILITY NOT FOUND"
                )

            booked_tokens = session.execute(
                select(
                    AppointmentMaster.token_no
                ).where(
                    AppointmentMaster.availability_id
                    == availability_id,

                    AppointmentMaster.appointment_date
                    == appointment_date,

                    AppointmentMaster.appointment_status
                    == "BOOKED"
                )
            ).scalars().all()

            token_status = []

            start_time = datetime.combine(
                appointment_date,
                availability.start_time
            )

            for token in range(
                1,
                availability.max_patients + 1
            ):

                consultation_time = (
                    start_time
                    +
                    timedelta(
                        minutes=
                        (
                            token - 1
                        )
                        *
                        CONSULTATION_DURATION
                    )
                ).time()

                status = (
                    "BOOKED"
                    if token in booked_tokens
                    else "AVAILABLE"
                )

                token_status.append(

                    (
                        token,
                        consultation_time,
                        status
                    )

                )

            return token_status

        finally:

            session.close()
            
    @staticmethod
    def search_appointment_by_id(
        appointment_id
    ):

        validate_required(
            appointment_id,
            "Appointment ID"
        )

        session = get_session()

        try:

            appointment = session.execute(
                select(
                    AppointmentMaster
                ).where(
                    AppointmentMaster.appointment_id
                    == appointment_id
                )
            ).scalar_one_or_none()

            return appointment

        finally:

            session.close()
            
    @staticmethod
    def search_appointment_details(
        appointment_id
    ):

        validate_required(
            appointment_id,
            "Appointment ID"
        )

        session = get_session()

        try:

            result = session.execute(
                select(
                    AppointmentMaster,
                    PatientMaster.patient_name,
                    DoctorMaster.doctor_name,
                    SessionMaster.session_name,
                    SessionMaster.room_id,
                    SessionMaster.start_time,
                    SessionMaster.end_time
                ).join(
                    PatientMaster,
                    AppointmentMaster.patient_id
                    == PatientMaster.patient_id
                ).join(
                    DoctorAvailability,
                    AppointmentMaster.availability_id
                    == DoctorAvailability.availability_id
                ).join(
                    DoctorMaster,
                    DoctorAvailability.doctor_id
                    == DoctorMaster.doctor_id
                ).join(
                    SessionMaster,
                    DoctorAvailability.session_id
                    == SessionMaster.session_id
                ).where(
                    AppointmentMaster.appointment_id
                    == appointment_id
                )
            ).one_or_none()

            return result

        finally:

            session.close()

    @staticmethod
    def search_appointments_by_patient(
        patient_id
    ):

        validate_required(
            patient_id,
            "Patient ID"
        )

        session = get_session()

        try:

            appointments = session.execute(

                select(
                    AppointmentMaster
                ).where(

                    AppointmentMaster.patient_id
                    ==
                    patient_id

                ).order_by(

                    AppointmentMaster.appointment_date,

                    AppointmentMaster.token_no

                )

            ).scalars().all()

            return appointments

        finally:

            session.close()
            
    @staticmethod
    def search_appointments_by_availability(
        availability_id
    ):

        validate_required(
            availability_id,
            "Availability ID"
        )

        session = get_session()

        try:

            appointments = session.execute(
                select(
                    AppointmentMaster
                ).where(
                    AppointmentMaster.availability_id
                    == availability_id
                ).order_by(
                    AppointmentMaster.appointment_date,
                    AppointmentMaster.token_no
                )
            ).scalars().all()

            return appointments

        finally:

            session.close()
            
    @staticmethod
    def view_all_appointments():

        session = get_session()

        try:

            appointments = session.execute(
                select(
                    AppointmentMaster
                ).order_by(
                    AppointmentMaster.appointment_id
                )
            ).scalars().all()

            return appointments

        finally:

            session.close()
            
    @staticmethod
    def update_appointment(
        appointment_id,
        availability_id,
        appointment_date,
        token_no,
        reason_for_visit
        ):

        validate_required(
            appointment_id,
            "Appointment ID"
        )

        validate_required(
            availability_id,
            "Availability ID"
        )

        validate_required(
            reason_for_visit,
            "Reason For Visit"
        )

        reason_for_visit = reason_for_visit.strip()

        if reason_for_visit == "":

            raise ValueError(
                "REASON FOR VISIT CANNOT BE EMPTY"
            )
         
        validate_future_date(
            appointment_date
        )
            
        session = get_session()

        try:

            appointment = session.execute(
                select(
                    AppointmentMaster
                ).where(
                    AppointmentMaster.appointment_id
                    == appointment_id
                )
            ).scalar_one_or_none()

            if not appointment:

                raise ValueError(
                    "APPOINTMENT NOT FOUND"
                )

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
                    "DOCTOR AVAILABILITY NOT FOUND"
                )

            if availability.status != "ACTIVE":

                raise ValueError(
                    "DOCTOR AVAILABILITY IS INACTIVE"
                )

            if appointment_date.strftime(
                "%A"
            ).upper() != availability.available_day:

                raise ValueError(
                    "DOCTOR IS NOT AVAILABLE ON THE SELECTED DATE"
                )
                
            existing = session.execute(
                select(
                    AppointmentMaster
                ).where(
                    AppointmentMaster.patient_id
                    == appointment.patient_id,

                    AppointmentMaster.appointment_date
                    == appointment_date,

                    AppointmentMaster.appointment_status
                    == "BOOKED",

                    AppointmentMaster.appointment_id
                    != appointment_id
                )
            ).scalar_one_or_none()

            if existing:

                raise ValueError(
                    "PATIENT ALREADY HAS AN APPOINTMENT ON THIS DATE"
                )

            if (

                appointment.availability_id
                != availability_id

                or

                appointment.appointment_date
                != appointment_date

                or

                appointment.token_no
                != token_no

            ):

                if (

                    token_no
                    <
                    1

                    or

                    token_no
                    >
                    availability.max_patients

                ):

                    raise ValueError(
                        "INVALID TOKEN NUMBER"
                    )

                existing_token = session.execute(
                    select(
                        AppointmentMaster
                    ).where(
                        AppointmentMaster.availability_id
                        == availability_id,

                        AppointmentMaster.appointment_date
                        == appointment_date,

                        AppointmentMaster.token_no
                        == token_no,

                        AppointmentMaster.appointment_status
                        == "BOOKED",

                        AppointmentMaster.appointment_id
                        != appointment_id
                    )
                ).scalar_one_or_none()

                if existing_token:

                    raise ValueError(
                        "TOKEN IS ALREADY BOOKED"
                    )

            appointment.availability_id = (
                availability_id
            )

            appointment.appointment_date = (
                appointment_date
            )

            appointment.token_no = (
                token_no
            )

            appointment.reason_for_visit = (
                reason_for_visit
            )

            session.commit()

            return True

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()

    @staticmethod
    def cancel_appointment(
        appointment_id
    ):

        validate_required(
            appointment_id,
            "Appointment ID"
        )

        session = get_session()

        try:

            appointment = session.execute(
                select(
                    AppointmentMaster
                ).where(
                    AppointmentMaster.appointment_id
                    == appointment_id
                )
            ).scalar_one_or_none()

            if not appointment:

                raise ValueError(
                    "APPOINTMENT NOT FOUND"
                )

            if appointment.appointment_status == "CANCELLED":

                raise ValueError(
                    "APPOINTMENT IS ALREADY CANCELLED"
                )

            appointment.appointment_status = (
                "CANCELLED"
            )

            session.commit()

            return True

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()
            
    @staticmethod
    def search_appointments_by_doctor(
        doctor_id
    ):

        validate_required(
            doctor_id,
            "Doctor ID"
        )

        session = get_session()

        try:

            appointments = session.execute(

                select(
                    AppointmentMaster
                ).join(

                    DoctorAvailability,

                    AppointmentMaster.availability_id
                    ==
                    DoctorAvailability.availability_id

                ).where(

                    DoctorAvailability.doctor_id
                    ==
                    doctor_id

                ).order_by(

                    AppointmentMaster.appointment_date,

                    AppointmentMaster.token_no

                )

            ).scalars().all()

            return appointments

        finally:

            session.close()

    @staticmethod
    def search_appointments_by_date(
        appointment_date
    ):

        session = get_session()

        try:

            appointments = session.execute(

                select(
                    AppointmentMaster
                ).where(

                    AppointmentMaster.appointment_date
                    ==
                    appointment_date

                ).order_by(

                    AppointmentMaster.token_no

                )

            ).scalars().all()

            return appointments

        finally:

            session.close()