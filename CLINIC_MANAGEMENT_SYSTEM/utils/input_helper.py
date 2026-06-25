class OperationCancelled(
    Exception
):
    pass


class InputHelper:

    @staticmethod
    def get_input(
        message
    ):

        value = input(
            message
        ).strip()

        if value.upper() == "CANCEL":

            raise OperationCancelled(
                "OPERATION CANCELLED"
            )

        return value

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