from sqlalchemy import Column, String, Date, Numeric
from models.base import Base


class BillingMaster(Base):
    __tablename__ = "BILLING_MASTER"

    bill_id = Column(
        "BILL_ID",
        String(10),
        primary_key=True
    )

    consultation_id = Column(
        "CONSULTATION_ID",
        String(10),
        nullable=False
    )

    consultation_fee = Column(
        "CONSULTATION_FEE",
        Numeric(10, 2),
        nullable=False
    )

    discount_amount = Column(
        "DISCOUNT_AMOUNT",
        Numeric(10, 2)
    )

    tax_amount = Column(
        "TAX_AMOUNT",
        Numeric(10, 2)
    )

    total_amount = Column(
        "TOTAL_AMOUNT",
        Numeric(10, 2),
        nullable=False
    )

    bill_date = Column(
        "BILL_DATE",
        Date
    )

    bill_status = Column(
        "BILL_STATUS",
        String(20)
    )
    
    payment_status = Column(
        "PAYMENT_STATUS",
        String(20)
    )