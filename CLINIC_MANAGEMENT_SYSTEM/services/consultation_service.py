from sqlalchemy import select
from models.consultation_master import ConsultationMaster
from models.appointment_master import AppointmentMaster
from connection import get_session
from utils.id_generator import generate_id
from datetime import datetime

class ConsultationService:

    @staticmethod
    def check_in_patient(appointment_id):

        session = get_session()

        try:

            appointment = session.execute(
                select(AppointmentMaster).where(
                    AppointmentMaster.appointment_id == appointment_id
                )
            ).scalar_one_or_none()

            if not appointment:
                raise ValueError("Appointment not found")

            if appointment.appointment_status != "BOOKED":
                raise ValueError("Appointment is not eligible for check-in")

            appointment.appointment_status = "CHECKED_IN"

            session.commit()

            return True

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    @staticmethod
    def start_consultation(appointment_id):

        session = get_session()

        try:

            appointment = session.execute(
                select(AppointmentMaster).where(
                    AppointmentMaster.appointment_id == appointment_id
                )
            ).scalar_one_or_none()

            if not appointment:
                raise ValueError("Appointment not found")

            if appointment.appointment_status != "CHECKED_IN":
                raise ValueError(
                    "Patient must be checked in before consultation"
                )
                
            existing = session.execute(
                select(ConsultationMaster).where(
                    ConsultationMaster.appointment_id
                    == appointment_id
                )
            ).scalar_one_or_none()

            if existing:
                raise ValueError(
                    "CONSULTATION ALREADY EXISTS FOR THIS APPOINTMENT"
                )

            consultation_id = generate_id(
                "CONSULTATION_MASTER",
                "CONSULTATION_ID",
                "C"
            )

            consultation = ConsultationMaster(
                consultation_id=consultation_id,
                appointment_id=appointment_id,
                consultation_start_time=datetime.now(),
                consultation_status="IN_PROGRESS"
            )

            session.add(consultation)

            appointment.appointment_status = "CONSULTING"

            session.commit()

            return consultation_id

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
            
    @staticmethod
    def search_consultation(
        consultation_id
    ):

        session = get_session()

        try:

            consultation = session.execute(
                select(ConsultationMaster).where(
                    ConsultationMaster.consultation_id
                    == consultation_id
                )
            ).scalar_one_or_none()

            return consultation

        finally:
            session.close()
    
    @staticmethod
    def get_all_consultations():

        session = get_session()

        try:

            consultations = session.execute(
                select(
                    ConsultationMaster
                )
                .order_by(
                    ConsultationMaster.consultation_id
                )
            ).scalars().all()

            return consultations

        finally:
            session.close()
    
    @staticmethod
    def end_consultation(
        consultation_id,
        symptoms,
        diagnosis,
        prescription,
        notes,
        followup_required,
        followup_date
    ):

        session = get_session()

        try:

            consultation = session.execute(
                select(ConsultationMaster).where(
                    ConsultationMaster.consultation_id == consultation_id
                )
            ).scalar_one_or_none()

            if not consultation:
                raise ValueError("Consultation not found")

            if consultation.consultation_status != "IN_PROGRESS":
                raise ValueError(
                    "Consultation is not in progress"
                )

            if not diagnosis.strip():
                raise ValueError(
                    "DIAGNOSIS CANNOT BE EMPTY"
                )

            if not prescription.strip():
                raise ValueError(
                    "PRESCRIPTION CANNOT BE EMPTY"
                )

            consultation.consultation_end_time = datetime.now()

            consultation.symptoms = symptoms
            consultation.diagnosis = diagnosis
            consultation.prescription = prescription
            consultation.notes = notes

            consultation.followup_required = (
                followup_required
            )

            consultation.followup_date = (
                followup_date
            )

            consultation.consultation_status = "COMPLETED"

            appointment = session.execute(
                select(AppointmentMaster).where(
                    AppointmentMaster.appointment_id ==
                    consultation.appointment_id
                )
            ).scalar_one_or_none()

            if appointment:
                appointment.appointment_status = "COMPLETED"

            session.commit()

            return True

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()