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
    def get_update_input(
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

        return value
    @staticmethod
    def get_confirmation(
        message="CONFIRM (Y/N): "
    ):

        while True:

            value = InputHelper.get_input(
                message
            ).upper()

            if value in ["Y", "N"]:

                return value

            print(
                "ENTER Y OR N ONLY"
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
    def get_update_date(
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

                return datetime.strptime(
                    value,
                    "%Y-%m-%d"
                    ).date()

            except ValueError:

                print(
                    "ENTER DATE AS YYYY-MM-DD"
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