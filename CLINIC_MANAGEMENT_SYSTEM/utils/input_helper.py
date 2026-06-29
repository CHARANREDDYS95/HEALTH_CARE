from datetime import datetime


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
    def get_date(message):

        while True:

            value = InputHelper.get_input(
                message
            )

            try:

                return datetime.strptime(
                    value,
                    "%Y-%m-%d"
                ).date()

            except ValueError:

                print(
                    "ENTER DATE AS YYYY-MM-DD"
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

            print(f"\nCURRENT STATUS : {current_status}")
            
            print("\nSELECT NEW STATUS")
            print("1. ACTIVE")
            print("2. INACTIVE")
            
            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                return "ACTIVE"

            elif choice == "2":
                
                return "INACTIVE"

            print("INVALID CHOICE. PLEASE ENTER 1 OR 2.")
            
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

                return "MONDAY"

            elif choice == "2":

                return "TUESDAY"

            elif choice == "3":

                return "WEDNESDAY"

            elif choice == "4":

                return "THURSDAY"

            elif choice == "5":

                return "FRIDAY"

            elif choice == "6":

                return "SATURDAY"

            elif choice == "7":

                return "SUNDAY"

            print(
                "INVALID CHOICE"
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

            value = input(
                f"ENTER CHOICE [{current_day}]: "
            ).strip()

            if value.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if value == "":

                return current_day

            if value == "1":

                return "MONDAY"

            elif value == "2":

                return "TUESDAY"

            elif value == "3":

                return "WEDNESDAY"

            elif value == "4":

                return "THURSDAY"

            elif value == "5":

                return "FRIDAY"

            elif value == "6":

                return "SATURDAY"

            elif value == "7":

                return "SUNDAY"

            print(
                "INVALID CHOICE"
            )

    @staticmethod
    def get_time(message):

        while True:

            value = InputHelper.get_input(
                message
            )

            try:

                datetime.strptime(
                    value,
                    "%I:%M %p"
                )

                return value

            except ValueError:

                print(
                    "ENTER TIME AS HH:MM AM/PM"
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

                datetime.strptime(
                    value,
                    "%I:%M %p"
                )

                return value

            except ValueError:

                print(
                    "ENTER TIME AS HH:MM AM/PM"
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

                return "CR1"

            elif choice == "2":

                return "CR2"

            print(
                "INVALID CHOICE"
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
    def get_update_date(
        message,
        current_date
    ):

        while True:

            value = InputHelper.get_input(
                f"{message} [{current_date}]: "
            ).strip()

            if value == "":

                return current_date

            try:

                from datetime import datetime

                return datetime.strptime(
                    value,
                    "%Y-%m-%d"
                ).date()

            except ValueError:

                print(
                    "INVALID DATE (YYYY-MM-DD)"
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

                return "M"

            elif choice == "2":

                return "F"

            elif choice == "3":

                return "O"

            print(
                "INVALID CHOICE. PLEASE ENTER 1, 2 OR 3."
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

                return "A+"

            elif choice == "2":

                return "A-"

            elif choice == "3":

                return "B+"

            elif choice == "4":

                return "B-"

            elif choice == "5":

                return "AB+"

            elif choice == "6":

                return "AB-"

            elif choice == "7":

                return "O+"

            elif choice == "8":

                return "O-"

            print(
                "INVALID CHOICE. PLEASE ENTER 1 TO 8."
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