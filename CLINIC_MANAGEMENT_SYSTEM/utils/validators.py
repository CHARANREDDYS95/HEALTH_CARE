import re
from datetime import date


def validate_required(value, field_name):
    if value is None or str(value).strip() == "":
        raise ValueError(f"{field_name} is required")


def validate_phone(phone):
    if not re.fullmatch(r"\d{10}", phone):
        raise ValueError("Phone number must be 10 digits")


def validate_email(email):
    if email:
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(pattern, email):
            raise ValueError("Invalid email format")


def validate_gender(gender):
    valid_genders = ["M", "F", "O"]

    if gender not in valid_genders:
        raise ValueError("Gender must be M, F or O")


def validate_status(status):
    valid_status = ["ACTIVE", "INACTIVE"]

    if status.upper() not in valid_status:
        raise ValueError("Status must be ACTIVE or INACTIVE")


def validate_positive_number(value, field_name):
    if value is None or value <= 0:
        raise ValueError(f"{field_name} must be greater than 0")


def validate_date_not_future(input_date):
    if input_date > date.today():
        raise ValueError("Future date is not allowed")


def validate_blood_group(blood_group):
    valid_groups = [
        "A+","A-",
        "B+","B-",
        "AB+","AB-",
        "O+","O-"
    ]

    if blood_group and blood_group.upper() not in valid_groups:
        raise ValueError("Invalid blood group")