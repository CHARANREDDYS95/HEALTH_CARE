import re
from datetime import date, datetime


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
def validate_time(value):

    try:

        datetime.strptime(
            value,
            "%H:%M"
        )

    except ValueError:

        raise ValueError(
            "Time must be in HH:MM (24-hour) format"
        )

def validate_future_date(
    appointment_date
):

    if appointment_date < date.today():

        raise ValueError(
            "APPOINTMENT DATE CANNOT BE IN THE PAST"
        )
        
def validate_room(room):

    valid_rooms = [
        "CR1",
        "CR2"
    ]

    if room not in valid_rooms:

        raise ValueError(
            "Room must be CR1 or CR2"
        )

def validate_day(
    day
):

    valid_days = [
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY"
    ]

    if day not in valid_days:

        raise ValueError(
            "INVALID DAY"
        )
        
def parse_date(
    date_value
):

    if date_value is None:

        raise ValueError(
            "DATE CANNOT BE EMPTY"
        )

    if isinstance(
        date_value,
        date
    ):

        return date_value

    if isinstance(
        date_value,
        datetime
    ):

        return date_value.date()

    date_value = str(
        date_value
    ).strip()

    if not date_value:

        raise ValueError(
            "DATE CANNOT BE EMPTY"
        )

    date_formats = [

        "%Y-%m-%d",

        "%d-%m-%Y",

        "%d/%m/%Y",

        "%Y/%m/%d",

        "%d.%m.%Y",

        "%Y.%m.%d",

        "%d %b %Y",

        "%d %B %Y",

        "%b %d %Y",

        "%B %d %Y"

    ]

    for date_format in date_formats:

        try:

            return datetime.strptime(
                date_value,
                date_format
            ).date()

        except ValueError:

            continue

    raise ValueError(
        f"INVALID DATE FORMAT : {date_value}"
    )