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


def validate_positive_number(
    value,
    field_name,
    allow_zero=False
):

    if value is None:

        raise ValueError(
            f"{field_name} CANNOT BE EMPTY"
        )

    if allow_zero:

        if value < 0:

            raise ValueError(
                f"{field_name} CANNOT BE NEGATIVE"
            )

    else:

        if value <= 0:

            raise ValueError(
                f"{field_name} MUST BE GREATER THAN 0"
            )

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
            "%I:%M %p"
        )

    except ValueError:

        raise ValueError(
            "TIME MUST BE IN HH:MM AM/PM FORMAT"
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
    
def validate_appointment_date(
    appointment_date
):

    if appointment_date < date.today():

        raise ValueError(
            "APPOINTMENT DATE CANNOT BE IN THE PAST"
        )
        
def validate_name(
    name
):

    if len(
        name
    ) < 3:

        raise ValueError(
            "NAME MUST CONTAIN AT LEAST 3 LETTERS"
        )

    if not all(

        character.isalpha()

        or

        character in " .'-"

        for character in name

    ):

        raise ValueError(
            "NAME CAN CONTAIN ONLY LETTERS"
        )
        
def validate_address(
    address
):

    if len(
        address
    ) < 10:

        raise ValueError(
            "ADDRESS MUST CONTAIN AT LEAST 10 CHARACTERS"
        )

    if not all(

        character.isalnum()

        or

        character in " ,./#-"

        for character in address

    ):

        raise ValueError(
            "ADDRESS CONTAINS INVALID CHARACTERS"
        )
        
def validate_city(
    city
):

    if len(
        city
    ) < 2:

        raise ValueError(
            "CITY NAME MUST CONTAIN AT LEAST 2 CHARACTERS"
        )

    if not all(

        character.isalpha()

        or

        character in " -"

        for character in city

    ):

        raise ValueError(
            "CITY NAME CAN CONTAIN ONLY LETTERS"
        )
        
def validate_specialization(
    specialization
):

    if len(
        specialization
    ) < 3:

        raise ValueError(
            "SPECIALIZATION MUST CONTAIN AT LEAST 3 CHARACTERS"
        )

    if not all(

        character.isalnum()

        or

        character in " .&-/"

        for character in specialization

    ):

        raise ValueError(
            "INVALID SPECIALIZATION"
        )
        
def validate_qualification(
    qualification
):

    if len(
        qualification
    ) < 2:

        raise ValueError(
            "QUALIFICATION MUST CONTAIN AT LEAST 2 CHARACTERS"
        )

    if not all(

        character.isalnum()

        or

        character in " .-/"

        for character in qualification

    ):

        raise ValueError(
            "INVALID QUALIFICATION"
        )
        
def validate_license_number(
    license_number
):

    if len(
        license_number
    ) < 5:

        raise ValueError(
            "INVALID LICENSE NUMBER"
        )

    if not all(

        character.isalnum()

        or

        character == "-"

        for character in license_number

    ):

        raise ValueError(
            "LICENSE NUMBER CAN CONTAIN ONLY LETTERS, NUMBERS AND '-'"
        )

def validate_occupation(
    occupation
):

    if len(
        occupation
    ) < 2:

        raise ValueError(
            "OCCUPATION MUST CONTAIN AT LEAST 2 CHARACTERS"
        )

    if not all(

        character.isalnum()

        or

        character in " .&/-"

        for character in occupation

    ):

        raise ValueError(
            "INVALID OCCUPATION"
        )
        
def validate_reason(
    reason
):

    if len(
        reason
    ) < 5:

        raise ValueError(
            "REASON MUST CONTAIN AT LEAST 5 CHARACTERS"
        )

    if len(
        reason
    ) > 200:

        raise ValueError(
            "REASON CANNOT EXCEED 200 CHARACTERS"
        )

    if not all(

        character.isalnum()

        or

        character in " .,()/-"

        for character in reason

    ):

        raise ValueError(
            "REASON CONTAINS INVALID CHARACTERS"
        )
        
def validate_symptoms(
    symptoms
):

    if len(
        symptoms
    ) < 3:

        raise ValueError(
            "SYMPTOMS MUST CONTAIN AT LEAST 3 CHARACTERS"
        )

    if len(
        symptoms
    ) > 500:

        raise ValueError(
            "SYMPTOMS CANNOT EXCEED 500 CHARACTERS"
        )

    if not all(

        character.isalnum()

        or

        character in " .,()-/"

        for character in symptoms

    ):

        raise ValueError(
            "SYMPTOMS CONTAIN INVALID CHARACTERS"
        )
        
def validate_diagnosis(
    diagnosis
):

    if len(
        diagnosis
    ) < 3:

        raise ValueError(
            "DIAGNOSIS MUST CONTAIN AT LEAST 3 CHARACTERS"
        )

    if len(
        diagnosis
    ) > 500:

        raise ValueError(
            "DIAGNOSIS CANNOT EXCEED 500 CHARACTERS"
        )

    if not all(

        character.isalnum()

        or

        character in " .,()-/"

        for character in diagnosis

    ):

        raise ValueError(
            "DIAGNOSIS CONTAINS INVALID CHARACTERS"
        )
        
def validate_prescription(
    prescription
):

    if len(
        prescription
    ) < 3:

        raise ValueError(
            "PRESCRIPTION MUST CONTAIN AT LEAST 3 CHARACTERS"
        )

    if len(
        prescription
    ) > 1000:

        raise ValueError(
            "PRESCRIPTION CANNOT EXCEED 1000 CHARACTERS"
        )
        
def validate_transaction_reference(
    transaction_reference
):

    if len(
        transaction_reference
    ) < 4:

        raise ValueError(
            "TRANSACTION REFERENCE MUST CONTAIN AT LEAST 4 CHARACTERS"
        )

    if len(
        transaction_reference
    ) > 30:

        raise ValueError(
            "TRANSACTION REFERENCE CANNOT EXCEED 30 CHARACTERS"
        )

    if not transaction_reference.replace(
        "-",
        ""
    ).isalnum():

        raise ValueError(
            "INVALID TRANSACTION REFERENCE"
        )