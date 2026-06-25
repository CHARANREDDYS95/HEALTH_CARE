from sqlalchemy import Column, String, Date, Numeric
from models.base import Base


class PaymentMaster(Base):
    __tablename__ = "PAYMENT_MASTER"

    payment_id = Column(
        "PAYMENT_ID",
        String(10),
        primary_key=True
    )

    bill_id = Column(
        "BILL_ID",
        String(10),
        nullable=False
    )

    payment_date = Column(
        "PAYMENT_DATE",
        Date
    )

    payment_mode = Column(
        "PAYMENT_MODE",
        String(20)
    )

    paid_amount = Column(
        "PAID_AMOUNT",
        Numeric(10, 2)
    )

    transaction_reference = Column(
        "TRANSACTION_REFERENCE",
        String(100)
    )

    payment_status = Column(
        "PAYMENT_STATUS",
        String(20)
    )