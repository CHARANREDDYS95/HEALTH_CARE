from datetime import date
from sqlalchemy import select
from models.billing_master import BillingMaster
from models.consultation_master import ConsultationMaster
from connection import get_session
from utils.id_generator import generate_id
from utils.validators import (
    validate_required,
    validate_positive_number
)
from models.payment_master import PaymentMaster
from models.appointment_master import AppointmentMaster
from models.doctor_master import DoctorMaster
from models.doctor_availability import DoctorAvailability
from models.patient_master import PatientMaster

class BillingService:

    @staticmethod
    def generate_bill(
        consultation_id,
        discount_amount
    ):
        validate_required(
            consultation_id,
            "Consultation ID"
        )

        validate_positive_number(
            discount_amount,
            "Discount Amount",
            allow_zero=True
        )

        session = get_session()

        try:

            consultation = session.execute(
                select(
                    ConsultationMaster
                ).where(
                    ConsultationMaster.consultation_id
                    == consultation_id
                )
            ).scalar_one_or_none()

            if not consultation:
                raise ValueError(
                    "CONSULTATION NOT FOUND"
                )

            if consultation.consultation_status != "COMPLETED":
                raise ValueError(
                    "CONSULTATION NOT COMPLETED"
                )

            existing_bill = session.execute(
                select(
                    BillingMaster
                ).where(
                    BillingMaster.consultation_id
                    == consultation_id
                )
            ).scalar_one_or_none()

            if existing_bill:
                raise ValueError(
                    "BILL ALREADY GENERATED"
                )

            appointment = session.execute(
                select(
                    AppointmentMaster
                ).where(
                    AppointmentMaster.appointment_id
                    == consultation.appointment_id
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
                    == appointment.availability_id
                )
            ).scalar_one_or_none()

            if not availability:

                raise ValueError(
                    "DOCTOR AVAILABILITY NOT FOUND"
                )
                    
            doctor = session.execute(
                select(
                    DoctorMaster
                ).where(
                    DoctorMaster.doctor_id
                    == availability.doctor_id
                )
            ).scalar_one_or_none()

            if not doctor:

                raise ValueError(
                    "DOCTOR NOT FOUND"
                )
                    
            consultation_fee = (
                doctor.consultation_fee
            )

            consultation_fee = (
                doctor.consultation_fee
            )

            taxable_amount = (
                consultation_fee
                - discount_amount
            )

            tax_amount = round(

                taxable_amount
                * 0.18,

                2

            )

            total_amount = round(

                taxable_amount
                + tax_amount,

                2

            )
            
            if total_amount <= 0:

                raise ValueError(
                    "TOTAL BILL AMOUNT MUST BE GREATER THAN ZERO"
                )

            bill_id = generate_id(
                "BILLING_MASTER",
                "BILL_ID",
                "B"
            )

            bill = BillingMaster(
                bill_id=bill_id,
                consultation_id=consultation_id,
                consultation_fee=consultation_fee,
                discount_amount=discount_amount,
                tax_amount=tax_amount,
                total_amount=total_amount,
                bill_date=date.today(),
                bill_status="UNPAID"
            )

            session.add(
                bill
            )

            session.commit()

            return bill_id

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
            
    @staticmethod
    def calculate_bill(
        consultation_id,
        discount_amount
    ):

        validate_required(
            consultation_id,
            "Consultation ID"
        )

        validate_positive_number(
            discount_amount,
            "Discount Amount",
            allow_zero=True
        )

        session = get_session()

        try:

            consultation = session.execute(
                select(
                    ConsultationMaster
                ).where(
                    ConsultationMaster.consultation_id
                    == consultation_id
                )
            ).scalar_one_or_none()

            if not consultation:

                raise ValueError(
                    "CONSULTATION NOT FOUND"
                )

            if consultation.consultation_status != "COMPLETED":

                raise ValueError(
                    "CONSULTATION NOT COMPLETED"
                )

            appointment = session.execute(
                select(
                    AppointmentMaster
                ).where(
                    AppointmentMaster.appointment_id
                    == consultation.appointment_id
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
                    == appointment.availability_id
                )
            ).scalar_one_or_none()

            if not availability:

                raise ValueError(
                    "DOCTOR AVAILABILITY NOT FOUND"
                )

            doctor = session.execute(
                select(
                    DoctorMaster
                ).where(
                    DoctorMaster.doctor_id
                    == availability.doctor_id
                )
            ).scalar_one_or_none()

            if not doctor:

                raise ValueError(
                    "DOCTOR NOT FOUND"
                )

            consultation_fee = (
                doctor.consultation_fee
            )

            taxable_amount = (
                consultation_fee
                - discount_amount
            )

            tax_amount = round(

                taxable_amount
                * 0.18,

                2

            )

            total_amount = round(

                taxable_amount
                + tax_amount,

                2

            )

            if total_amount <= 0:

                raise ValueError(
                    "TOTAL BILL AMOUNT MUST BE GREATER THAN ZERO"
                )

            patient = session.execute(
                select(
                    PatientMaster
                ).where(
                    PatientMaster.patient_id
                    == appointment.patient_id
                )
            ).scalar_one_or_none()

            return {

                "consultation_id": consultation.consultation_id,

                "appointment_id": appointment.appointment_id,

                "patient_id": patient.patient_id,

                "patient_name": patient.patient_name,

                "doctor_name": doctor.doctor_name,

                "consultation_fee": consultation_fee,

                "discount_amount": discount_amount,

                "tax_amount": tax_amount,

                "total_amount": total_amount

            }

        finally:

            session.close()
            
    @staticmethod
    def search_bill_by_id(
        bill_id
    ):
        validate_required(
            bill_id,
            "Bill ID"
        )
        session = get_session()

        try:

            bill = session.execute(
                select(BillingMaster).where(
                    BillingMaster.bill_id == bill_id
                )
            ).scalar_one_or_none()

            return bill

        finally:
            session.close()
        
    @staticmethod
    def search_bill_by_consultation(
        consultation_id
    ):
        validate_required(
            consultation_id,
            "Consultation ID"
        )
        session = get_session()

        try:

            bill = session.execute(
                select(BillingMaster).where(
                    BillingMaster.consultation_id == consultation_id
                )
            ).scalar_one_or_none()

            return bill

        finally:
            session.close()
            
    @staticmethod
    def process_payment(
        bill_id,
        payment_mode,
        transaction_reference
    ):
        validate_required(
            bill_id,
            "Bill ID"
        )

        validate_required(
            payment_mode,
            "Payment Mode"
        )
        
        payment_mode = (
            payment_mode.strip().upper()
        )

        if payment_mode not in (
            "CASH",
            "CARD",
            "UPI"
        ):

            raise ValueError(
                "INVALID PAYMENT MODE"
            )
        
        if payment_mode != "CASH":

            validate_required(
                transaction_reference,
                "Transaction Reference"
            )

        else:

            transaction_reference = ""
        
        session = get_session()

        try:

            bill = session.execute(
                select(
                    BillingMaster
                ).where(
                    BillingMaster.bill_id
                    == bill_id
                )
            ).scalar_one_or_none()

            if not bill:
                raise ValueError(
                    "BILL NOT FOUND"
                )

            if bill.bill_status == "PAID":

                raise ValueError(
                    "BILL ALREADY PAID"
                )

            existing_payment = session.execute(
                select(
                    PaymentMaster
                ).where(
                    PaymentMaster.bill_id
                    == bill_id,

                    PaymentMaster.payment_status
                    == "SUCCESS"
                )
            ).scalar_one_or_none()

            if existing_payment:

                raise ValueError(
                    "PAYMENT HAS ALREADY BEEN RECORDED"
                )

            payment_id = generate_id(
                "PAYMENT_MASTER",
                "PAYMENT_ID",
                "PAY"
            )

            payment = PaymentMaster(
                payment_id=payment_id,
                bill_id=bill.bill_id,
                payment_date=date.today(),
                payment_mode=payment_mode,
                paid_amount=bill.total_amount,
                transaction_reference=transaction_reference,
                payment_status="SUCCESS"
            )

            session.add(payment)

            bill.bill_status = "PAID"

            session.commit()

            return payment_id

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
            
    @staticmethod
    def get_all_bills():

        session = get_session()

        try:

            bills = session.execute(

                select(

                    BillingMaster

                ).order_by(

                    BillingMaster.bill_id

                )

            ).scalars().all()

            return bills

        finally:
            session.close()