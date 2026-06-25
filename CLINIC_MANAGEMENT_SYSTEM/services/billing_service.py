from datetime import date
from sqlalchemy import select
from models.billing_master import BillingMaster
from models.consultation_master import ConsultationMaster
from connection import get_session
from utils.id_generator import generate_id
from models.payment_master import PaymentMaster
from models.appointment_master import AppointmentMaster
from models.doctor_master import DoctorMaster

class BillingService:

    @staticmethod
    def create_bill(
        consultation_id,
        consultation_fee,
        discount_amount,
        tax_amount
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

            if consultation.consultation_status != "COMPLETED":
                raise ValueError(
                    "Consultation must be completed before billing"
                )

            bill_id = generate_id(
                "BILLING_MASTER",
                "BILL_ID",
                "B"
            )

            total_amount = (
                consultation_fee
                - discount_amount
                + tax_amount
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

            session.add(bill)
            session.commit()

            return bill_id

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

    @staticmethod
    def record_payment(
        bill_id,
        payment_mode,
        paid_amount,
        transaction_reference
    ):

        session = get_session()

        try:

            bill = session.execute(
                select(BillingMaster).where(
                    BillingMaster.bill_id == bill_id
                )
            ).scalar_one_or_none()

            if not bill:
                raise ValueError("Bill not found")

            payment_id = generate_id(
                "PAYMENT_MASTER",
                "PAYMENT_ID",
                "PM"
            )

            payment = PaymentMaster(
                payment_id=payment_id,
                bill_id=bill_id,
                payment_date=date.today(),
                payment_mode=payment_mode,
                paid_amount=paid_amount,
                transaction_reference=transaction_reference,
                payment_status="SUCCESS"
            )

            session.add(payment)

            if paid_amount >= bill.total_amount:
                bill.bill_status = "PAID"
            else:
                bill.bill_status = "PARTIAL"

            session.commit()

            return payment_id

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
            
    @staticmethod
    def generate_bill(
        consultation_id,
        discount_amount,
        tax_amount
    ):

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

            doctor = session.execute(
                select(
                    DoctorMaster
                ).where(
                    DoctorMaster.doctor_id
                    == appointment.doctor_id
                )
            ).scalar_one_or_none()

            consultation_fee = (
                doctor.consultation_fee
            )

            total_amount = (
                consultation_fee
                - discount_amount
                + tax_amount
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
    def search_bill(
        bill_id
    ):

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

            return bill

        finally:
            session.close()
            
    @staticmethod
    def search_bill_by_id(
        bill_id
    ):

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

            payment_id = generate_id(
                "PAYMENT_MASTER",
                "PAYMENT_ID",
                "PM"
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
                )
                .order_by(
                    BillingMaster.bill_id
                )
            ).scalars().all()

            return bills

        finally:
            session.close()