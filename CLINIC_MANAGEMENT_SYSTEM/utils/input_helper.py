from datetime import datetime
from utils.validators import (
    validate_name,
    validate_phone,
    validate_email,
    validate_gender,
    validate_status,
    validate_positive_number,
    validate_date_not_future,
    validate_time,
    validate_future_date,
    validate_room,
    validate_day,
    validate_blood_group,
    validate_address,
    validate_city,
    validate_specialization,
    validate_qualification,
    validate_license_number,
    validate_occupation,
    validate_reason,
    validate_symptoms,
    validate_diagnosis,
    validate_prescription,
    validate_transaction_reference
)

class OperationCancelled(
    Exception
):
    pass


class InputHelper:

    @staticmethod
    def get_input(message):

        while True:

            value = input(
                message
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                print(
                    "INPUT CANNOT BE EMPTY"
                )
                continue

            return value
        

        
    @staticmethod
    def get_integer(message):

        while True:

            value = InputHelper.get_input(
                message
            )

            try:

                return int(value)

            except ValueError:

                print(
                    "ENTER A VALID INTEGER"
                )
    @staticmethod
    def get_float(message):

        while True:

            value = InputHelper.get_input(
                message
            )

            try:

                return float(value)

            except ValueError:

                print(
                    "ENTER A VALID NUMBER"
                )
                
    @staticmethod
    def get_phone(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                )

                validate_phone(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_email(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_email(
                    value
                )

                return value.lower()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_qualification(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_qualification(
                    value
                )

                return value.upper()

            except ValueError as e:

                print(
                    e
                )
    
    @staticmethod
    def get_specialization(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_specialization(
                    value
                )

                return value.upper()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_license_number(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip().upper()

                validate_license_number(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_name(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_name(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_address(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_address(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_city(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_city(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_occupation(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_occupation(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_allergies(message):

        value = InputHelper.get_input(
            message
        ).strip()

        return value.title()
    
    @staticmethod
    def get_reason(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_reason(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_update_reason(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_reason(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_appointment_id(
        message
    ):

        while True:

            appointment_id = InputHelper.get_input(
                message
            ).strip().upper()

            if not appointment_id.startswith(
                "A"
            ):

                print(
                    "APPOINTMENT ID MUST START WITH 'A'"
                )

                continue

            if len(
                appointment_id
            ) < 2:

                print(
                    "INVALID APPOINTMENT ID"
                )

                continue

            if not appointment_id[1:].isdigit():

                print(
                    "INVALID APPOINTMENT ID"
                )

                continue

            return appointment_id
        
    @staticmethod
    def get_consultation_id(
        message
    ):

        while True:

            consultation_id = InputHelper.get_input(
                message
            ).strip().upper()

            if not consultation_id.startswith(
                "C"
            ):

                print(
                    "CONSULTATION ID MUST START WITH 'C'"
                )

                continue

            if len(
                consultation_id
            ) < 2:

                print(
                    "INVALID CONSULTATION ID"
                )

                continue

            if not consultation_id[1:].isdigit():

                print(
                    "INVALID CONSULTATION ID"
                )

                continue

            return consultation_id
        
    @staticmethod
    def get_patient_id(
        message
    ):

        while True:

            patient_id = InputHelper.get_input(
                message
            ).strip().upper()

            if not patient_id.startswith(
                "P"
            ):

                print(
                    "PATIENT ID MUST START WITH 'P'"
                )

                continue

            if len(
                patient_id
            ) < 2:

                print(
                    "INVALID PATIENT ID"
                )

                continue

            if not patient_id[1:].isdigit():

                print(
                    "INVALID PATIENT ID"
                )

                continue

            return patient_id
        
    @staticmethod
    def get_doctor_id(
        message
    ):

        while True:

            doctor_id = InputHelper.get_input(
                message
            ).strip().upper()

            if not doctor_id.startswith(
                "D"
            ):

                print(
                    "DOCTOR ID MUST START WITH 'D'"
                )

                continue

            if len(
                doctor_id
            ) < 2:

                print(
                    "INVALID DOCTOR ID"
                )

                continue

            if not doctor_id[1:].isdigit():

                print(
                    "INVALID DOCTOR ID"
                )

                continue

            return doctor_id
        
    @staticmethod
    def get_symptoms(
        message
    ):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_symptoms(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
                
    @staticmethod
    def get_update_symptoms(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_symptoms(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_diagnosis(
        message
    ):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_diagnosis(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
                
    @staticmethod
    def get_update_diagnosis(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_diagnosis(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_prescription(
        message
    ):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                validate_prescription(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_update_prescription(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_prescription(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_consultation_notes(
        message
    ):

        while True:

            value = InputHelper.get_input(
                message
            ).strip()

            if len(
                value
            ) > 1000:

                print(
                    "NOTES CANNOT EXCEED 1000 CHARACTERS"
                )

                continue

            return value
    
    @staticmethod
    def get_update_allergies(
        message,
        current_value
    ):

        value = input(
            f"{message} [{current_value}]: "
        ).strip()

        if value.upper() == "CANCEL":

            raise OperationCancelled(
                "OPERATION CANCELLED"
            )

        if value == "":

            return current_value

        return value.title()
        
    @staticmethod
    def get_update_occupation(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_occupation(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_update_city(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_city(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_experience(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                )

                experience = int(
                    value
                )

                validate_positive_number(
                    experience,
                    "EXPERIENCE",
                    allow_zero=True
                )

                if experience > 60:

                    print(
                        "EXPERIENCE CANNOT BE GREATER THAN 60 YEARS"
                    )

                    continue

                return experience

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_date(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                )

                input_date = datetime.strptime(
                    value,
                    "%Y-%m-%d"
                ).date()

                validate_date_not_future(
                    input_date
                )

                return input_date

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_future_date(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                )

                appointment_date = datetime.strptime(
                    value,
                    "%Y-%m-%d"
                ).date()

                validate_future_date(
                    appointment_date
                )

                return appointment_date

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_consultation_fee(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                )

                consultation_fee = float(
                    value
                )

                validate_positive_number(
                    consultation_fee,
                    "CONSULTATION FEE"
                )

                if consultation_fee > 100000:

                    print(
                        "CONSULTATION FEE IS TOO HIGH"
                    )

                    continue

                return consultation_fee

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_yes_no(
        message
    ):

        while True:

            value = InputHelper.get_input(
                message
            ).upper()

            if value in [
                    "YES",
                    "NO"
            ]:

                return value

            print(
                "ENTER YES OR NO ONLY"
            )
            
    @staticmethod
    def get_update_integer(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
                ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                return int(value)

            except ValueError:

                print(
                    "ENTER A VALID INTEGER"
                )
    @staticmethod
    def get_update_float(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                return float(value)

            except ValueError:

                print(
                    "ENTER A VALID NUMBER"
                )

    @staticmethod
    def get_update_choice(
        message,
        current_value,
        choices
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            value = value.upper()

            if value in choices:

                return value

            print(
                f"ENTER {'/'.join(choices)} ONLY"
            )
    @staticmethod
    def get_choice(
        message,
        choices
    ):

        while True:

            value = InputHelper.get_input(
                message
            ).upper()

            if value in choices:
                
                return value

            print(
                f"ENTER {'/'.join(choices)} ONLY"
            )

    @staticmethod
    def get_status_choice(current_status):

        while True:

            print(
                f"\nCURRENT STATUS : {current_status}"
            )

            print("\nSELECT NEW STATUS")
            print("1. ACTIVE")
            print("2. INACTIVE")

            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                status = "ACTIVE"

            elif choice == "2":

                status = "INACTIVE"

            else:

                print(
                    "INVALID CHOICE. PLEASE ENTER 1 OR 2."
                )

                continue

            try:

                validate_status(
                    status
                )

                return status

            except ValueError as e:

                print(
                    e
                )
            
    @staticmethod
    def get_day_choice():

        while True:

            print("\nSELECT DAY")
            print("1. MONDAY")
            print("2. TUESDAY")
            print("3. WEDNESDAY")
            print("4. THURSDAY")
            print("5. FRIDAY")
            print("6. SATURDAY")
            print("7. SUNDAY")

            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                day = "MONDAY"

            elif choice == "2":

                day = "TUESDAY"

            elif choice == "3":

                day = "WEDNESDAY"

            elif choice == "4":

                day = "THURSDAY"

            elif choice == "5":

                day = "FRIDAY"

            elif choice == "6":

                day = "SATURDAY"

            elif choice == "7":

                day = "SUNDAY"

            else:

                print(
                    "INVALID CHOICE"
                )

                continue

            try:

                validate_day(
                    day
                )

                return day

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_update_day_choice(
        current_day
    ):

        while True:

            print("\nSELECT DAY")
            print("1. MONDAY")
            print("2. TUESDAY")
            print("3. WEDNESDAY")
            print("4. THURSDAY")
            print("5. FRIDAY")
            print("6. SATURDAY")
            print("7. SUNDAY")
            print("PRESS ENTER TO KEEP CURRENT DAY")

            choice = input(
                "ENTER CHOICE: "
            ).strip()

            if choice.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if choice == "":

                return current_day

            if choice == "1":

                day = "MONDAY"

            elif choice == "2":

                day = "TUESDAY"

            elif choice == "3":

                day = "WEDNESDAY"

            elif choice == "4":

                day = "THURSDAY"

            elif choice == "5":

                day = "FRIDAY"

            elif choice == "6":

                day = "SATURDAY"

            elif choice == "7":

                day = "SUNDAY"

            else:

                print(
                    "INVALID CHOICE"
                )

                continue

            try:

                validate_day(
                    day
                )

                return day

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_time(message):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                )

                validate_time(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_update_time(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_time(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_update_transaction_reference(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip().upper()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_transaction_reference(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )

    @staticmethod
    def get_room_choice():

        while True:

            print("\nSELECT CONSULTATION ROOM")
            print("1. CR1")
            print("2. CR2")

            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                room = "CR1"

            elif choice == "2":

                room = "CR2"

            else:

                print(
                    "INVALID CHOICE"
                )

                continue

            try:

                validate_room(
                    room
                )

                return room

            except ValueError as e:

                print(
                    e
                )
            
    @staticmethod
    def get_confirmation(
        message="CONFIRM ACTION"
    ):

        while True:

            print(f"\n{message}")

            print("1. YES")
            print("2. NO")

            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                return "Y"

            elif choice == "2":

                return "N"

            print(
                "INVALID CHOICE. PLEASE ENTER 1 OR 2."
            )
            
    @staticmethod
    def get_update_input(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            return value
        
    @staticmethod
    def get_update_name(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            if len(value) < 3:

                print(
                    "NAME MUST CONTAIN AT LEAST 3 LETTERS"
                )

                continue

            if not all(

                character.isalpha()

                or

                character in " .'-"

                for character in value

            ):

                print(
                    "NAME CAN CONTAIN ONLY LETTERS"
                )

                continue

            return value.title()
    
    @staticmethod
    def get_update_phone(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_phone(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_update_email(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_email(
                    value
                )

                return value.lower()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_update_specialization(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_specialization(
                    value
                )

                return value.upper()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_update_qualification(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_qualification(
                    value
                )

                return value.upper()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_update_license_number(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip().upper()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_license_number(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_update_address(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                validate_address(
                    value
                )

                return value.title()

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_update_experience(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                experience = int(
                    value
                )

                validate_positive_number(
                    experience,
                    "EXPERIENCE",
                    allow_zero=True
                )

                if experience > 60:

                    print(
                        "EXPERIENCE CANNOT BE GREATER THAN 60 YEARS"
                    )

                    continue

                return experience

            except ValueError as e:

                print(
                    e
                )
                
    @staticmethod
    def get_update_consultation_fee(
        message,
        current_value
    ):

        while True:

            value = input(
                f"{message} [{current_value}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_value

            try:

                consultation_fee = float(
                    value
                )

                validate_positive_number(
                    consultation_fee,
                    "CONSULTATION FEE"
                )

                if consultation_fee > 100000:

                    print(
                        "CONSULTATION FEE IS TOO HIGH"
                    )

                    continue

                return consultation_fee

            except ValueError as e:

                print(
                    e
                )
    
    @staticmethod
    def get_update_date(
        message,
        current_date
    ):

        while True:

            value = input(
                f"{message} [{current_date}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_date

            try:

                input_date = datetime.strptime(
                    value,
                    "%Y-%m-%d"
                ).date()

                validate_date_not_future(
                    input_date
                )

                return input_date

            except ValueError as e:

                print(
                    e
                )
                
    @staticmethod
    def get_gender_choice():

        while True:

            print("\nSELECT GENDER")
            print("1. MALE")
            print("2. FEMALE")
            print("3. OTHER")

            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                gender = "M"

            elif choice == "2":

                gender = "F"

            elif choice == "3":

                gender = "O"

            else:

                print(
                    "INVALID CHOICE. PLEASE ENTER 1, 2 OR 3."
                )

                continue

            try:

                validate_gender(
                    gender
                )

                return gender

            except ValueError as e:

                print(
                    e
                )
            
    @staticmethod
    def get_update_gender_choice(
        current_gender
    ):

        while True:

            print(
                f"\nCURRENT GENDER : {current_gender}"
            )

            print(
                "PRESS ENTER TO KEEP CURRENT VALUE"
            )

            print("1. MALE")
            print("2. FEMALE")
            print("3. OTHER")

            choice = input(
                "ENTER CHOICE: "
            ).strip()

            if choice.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if choice == "":

                return current_gender

            if choice == "1":

                gender = "M"

            elif choice == "2":

                gender = "F"

            elif choice == "3":

                gender = "O"

            else:

                print(
                    "INVALID CHOICE. PLEASE ENTER 1, 2 OR 3."
                )

                continue

            try:

                validate_gender(
                    gender
                )

                return gender

            except ValueError as e:

                print(
                    e
                )
            
    @staticmethod
    def get_blood_group_choice():

        while True:

            print("\nSELECT BLOOD GROUP")

            print("1. A+")
            print("2. A-")
            print("3. B+")
            print("4. B-")
            print("5. AB+")
            print("6. AB-")
            print("7. O+")
            print("8. O-")

            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                blood_group = "A+"

            elif choice == "2":

                blood_group = "A-"

            elif choice == "3":

                blood_group = "B+"

            elif choice == "4":

                blood_group = "B-"

            elif choice == "5":

                blood_group = "AB+"

            elif choice == "6":

                blood_group = "AB-"

            elif choice == "7":

                blood_group = "O+"

            elif choice == "8":

                blood_group = "O-"

            else:

                print(
                    "INVALID CHOICE. PLEASE ENTER 1 TO 8."
                )

                continue

            try:

                validate_blood_group(
                    blood_group
                )

                return blood_group

            except ValueError as e:

                print(
                    e
                )
                
    @staticmethod
    def get_update_blood_group_choice(
        current_blood_group
    ):

        while True:

            print("\nSELECT BLOOD GROUP")

            print("1. A+")
            print("2. A-")
            print("3. B+")
            print("4. B-")
            print("5. AB+")
            print("6. AB-")
            print("7. O+")
            print("8. O-")
            print("PRESS ENTER TO KEEP CURRENT BLOOD GROUP")

            choice = input(
                "ENTER CHOICE: "
            ).strip()

            if choice.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if choice == "":

                return current_blood_group

            if choice == "1":

                blood_group = "A+"

            elif choice == "2":

                blood_group = "A-"

            elif choice == "3":

                blood_group = "B+"

            elif choice == "4":

                blood_group = "B-"

            elif choice == "5":

                blood_group = "AB+"

            elif choice == "6":

                blood_group = "AB-"

            elif choice == "7":

                blood_group = "O+"

            elif choice == "8":

                blood_group = "O-"

            else:

                print(
                    "INVALID CHOICE. PLEASE ENTER 1 TO 8."
                )

                continue

            try:

                validate_blood_group(
                    blood_group
                )

                return blood_group

            except ValueError as e:

                print(
                    e
                )
            
    @staticmethod
    def get_marital_status_choice():

        while True:

            print("\nSELECT MARITAL STATUS")

            print("1. SINGLE")
            print("2. MARRIED")
            print("3. DIVORCED")
            print("4. WIDOWED")

            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                return "SINGLE"

            elif choice == "2":

                return "MARRIED"

            elif choice == "3":

                return "DIVORCED"

            elif choice == "4":

                return "WIDOWED"

            print(
                "INVALID CHOICE. PLEASE ENTER 1 TO 4."
            )
            
    @staticmethod
    def get_update_marital_status(
        current_value
    ):

        while True:

            print(
                f"\nCURRENT MARITAL STATUS : {current_value}"
            )

            print("PRESS ENTER TO KEEP THE CURRENT VALUE")

            print("1. SINGLE")
            print("2. MARRIED")
            print("3. DIVORCED")
            print("4. WIDOWED")

            choice = input(
                "ENTER CHOICE: "
            ).strip()

            if choice.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if choice == "":

                return current_value

            elif choice == "1":

                return "SINGLE"

            elif choice == "2":

                return "MARRIED"

            elif choice == "3":

                return "DIVORCED"

            elif choice == "4":

                return "WIDOWED"

            print(
                "INVALID CHOICE"
            )
            
    @staticmethod
    def get_bill_id(
        message
    ):

        while True:

            bill_id = InputHelper.get_input(
                message
            ).strip().upper()

            if not bill_id.startswith(
                "B"
            ):

                print(
                    "BILL ID MUST START WITH 'B'"
                )

                continue

            if len(
                bill_id
            ) < 2:

                print(
                    "INVALID BILL ID"
                )

                continue

            if not bill_id[1:].isdigit():

                print(
                    "INVALID BILL ID"
                )

                continue

            return bill_id
        
    @staticmethod
    def get_discount_amount(
        message
    ):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip()

                discount = float(
                    value
                )

                if discount < 0:

                    print(
                        "DISCOUNT CANNOT BE NEGATIVE"
                    )

                    continue

                return discount

            except ValueError:

                print(
                    "ENTER A VALID DISCOUNT AMOUNT"
                )
                
    @staticmethod
    def get_payment_mode():

        while True:

            print()

            print(
                "=========================================="
            )

            print(
                "            PAYMENT MODE"
            )

            print(
                "=========================================="
            )

            print(
                "1. CASH"
            )

            print(
                "2. UPI"
            )

            print(
                "3. CARD"
            )

            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                return "CASH"

            elif choice == "2":

                return "UPI"

            elif choice == "3":

                return "CARD"

            print()

            print(
                "INVALID CHOICE"
            )
            
    @staticmethod
    def get_transaction_reference(
        message
    ):

        while True:

            try:

                value = InputHelper.get_input(
                    message
                ).strip().upper()

                validate_transaction_reference(
                    value
                )

                return value

            except ValueError as e:

                print(
                    e
                )
        
    @staticmethod
    def get_update_room_choice(
        current_room
    ):

        while True:

            print("\nSELECT CONSULTATION ROOM")
            print("1. CR1")
            print("2. CR2")
            print("PRESS ENTER TO KEEP CURRENT ROOM")

            choice = input(
                "ENTER CHOICE: "
            ).strip()

            if choice.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if choice == "":

                return current_room

            if choice == "1":

                room = "CR1"

            elif choice == "2":

                room = "CR2"

            else:

                print(
                    "INVALID CHOICE"
                )

                continue

            try:

                validate_room(
                    room
                )

                return room

            except ValueError as e:

                print(
                    e
                )