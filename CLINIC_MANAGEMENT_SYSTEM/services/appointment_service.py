from sqlalchemy import select
from models.appointment_master import AppointmentMaster
from connection import get_session
from utils.id_generator import generate_id
from models.patient_master import PatientMaster
from models.doctor_master import DoctorMaster
from models.session_master import SessionMaster


class AppointmentService:

    @staticmethod
    def book_appointment(
        patient_id,
        doctor_id,
        session_id,
        appointment_date,
        token_no,
        reason_for_visit
    ):

        session = get_session()
        
        patient = session.execute(
            select(PatientMaster).where(
                PatientMaster.patient_id == patient_id
            )            ).scalar_one_or_none()

        if not patient:
            raise ValueError("Patient not found")

        if patient.patient_status != "ACTIVE":
            raise ValueError("Patient is inactive")
            
        existing_patient = session.execute(
            select(AppointmentMaster)
            .where(
                AppointmentMaster.patient_id == patient_id,
                AppointmentMaster.doctor_id == doctor_id,
                AppointmentMaster.appointment_date == appointment_date,
                AppointmentMaster.appointment_status != "CANCELLED"
            )
        ).scalar_one_or_none()

       
        
        doctor = session.execute(
            select(DoctorMaster).where(
                DoctorMaster.doctor_id == doctor_id
            )
        ).scalar_one_or_none()

        if not doctor:
            raise ValueError("Doctor not found")

        if doctor.doctor_status != "ACTIVE":
            raise ValueError("Doctor is inactive")
            
        if existing_patient:
            raise ValueError(
                "PATIENT ALREADY HAS AN APPOINTMENT WITH THIS DOCTOR ON THIS DATE"
            )
        
        existing = session.execute(
            select(AppointmentMaster)
            .where(
                AppointmentMaster.doctor_id == doctor_id,
                AppointmentMaster.session_id == session_id,
                AppointmentMaster.appointment_date == appointment_date,
                AppointmentMaster.token_no == token_no,
                AppointmentMaster.appointment_status != "CANCELLED"
            )
        ).scalar_one_or_none()

        if existing:

            raise ValueError(
                "TOKEN ALREADY BOOKED"
            )

        try:

            appointment_id = generate_id(
                "APPOINTMENT_MASTER",
                "APPOINTMENT_ID",
                "A"
            )
           
            appointment = AppointmentMaster(
                appointment_id=appointment_id,
                patient_id=patient_id,
                doctor_id=doctor_id,
                session_id=session_id,
                appointment_date=appointment_date,
                token_no=token_no,
                appointment_status="BOOKED",
                booked_date=appointment_date,
                reason_for_visit=reason_for_visit
            )

            session.add(appointment)
            session.commit()

            return appointment_id

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()


    @staticmethod
    def search_appointment(appointment_id):

        session = get_session()

        try:

            appointment = session.execute(
                select(AppointmentMaster).where(
                    AppointmentMaster.appointment_id == appointment_id
                )
            ).scalar_one_or_none()

            return appointment

        finally:
            session.close()

    @staticmethod
    def update_appointment(
        appointment_id,
        session_id,
        appointment_date,
        token_no,
        reason_for_visit
    ):

        session = get_session()

        try:

            appointment = session.execute(
                select(AppointmentMaster).where(
                    AppointmentMaster.appointment_id
                    == appointment_id
                )
                ).scalar_one_or_none()

            if not appointment:
                raise ValueError(
                    "Appointment not found"
                )

            existing = session.execute(
                select(AppointmentMaster)
                .where(
                    AppointmentMaster.doctor_id
                    == appointment.doctor_id,

                    AppointmentMaster.session_id
                    == session_id,

                    AppointmentMaster.appointment_date
                    == appointment_date,

                    AppointmentMaster.token_no
                    == token_no,

                    AppointmentMaster.appointment_id
                    != appointment_id,

                    AppointmentMaster.appointment_status
                    != "CANCELLED"
                )
            ).scalar_one_or_none()

            if existing:

                raise ValueError(
                    "TOKEN ALREADY BOOKED"
                )

            appointment.session_id = session_id

            appointment.appointment_date = (
                appointment_date
            )

            appointment.token_no = token_no

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
    def cancel_appointment(appointment_id):

        session = get_session()

        try:

            appointment = session.execute(
                select(AppointmentMaster).where(
                    AppointmentMaster.appointment_id == appointment_id
                )
            ).scalar_one_or_none()

            if not appointment:
                raise ValueError("Appointment not found")

            appointment.appointment_status = "CANCELLED"
            
            session.commit()

            return True

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
            
    @staticmethod
    def get_active_sessions():

        session = get_session()

        try:

            sessions = session.execute(
                select(SessionMaster).where(
                    SessionMaster.status == "ACTIVE"
                )
                .order_by(
                    SessionMaster.session_id
                )
            ).scalars().all()

            return sessions

        finally:
            session.close()

    @staticmethod
    def get_booked_tokens(
        doctor_id,
        session_id,
        appointment_date
    ):

        session = get_session()

        try:

            tokens = session.execute(
                select(
                    AppointmentMaster.token_no
                )
                .where(
                    AppointmentMaster.doctor_id
                    == doctor_id,

                    AppointmentMaster.session_id
                    == session_id,

                    AppointmentMaster.appointment_date
                    == appointment_date,

                    AppointmentMaster.appointment_status
                    != "CANCELLED"
                )
            ).scalars().all()

            return tokens

        finally:
            session.close()
            
    @staticmethod
    def get_session_details(
        session_id
    ):

        session = get_session()

        try:

            session_obj = session.execute(
                select(SessionMaster)
                .where(
                    SessionMaster.session_id
                    == session_id
                )
            ).scalar_one_or_none()

            return session_obj

        finally:
            session.close()
    @staticmethod
    def get_all_appointments():

        session = get_session()

        try:

            appointments = session.execute(
                select(AppointmentMaster)
                .order_by(
                    AppointmentMaster.appointment_date,
                    AppointmentMaster.token_no
                )
            ).scalars().all()

            return appointments

        finally:
            session.close()