from datetime import datetime, timedelta


class TokenHelper:

    @staticmethod
    def get_token_time(
        start_time,
        token_no,
        token_duration=12
    ):

        start = datetime.strptime(
            start_time,
            "%I:%M %p"
        )

        token_start = start + timedelta(
            minutes=(token_no - 1)
            * token_duration
        )

        token_end = token_start + timedelta(
            minutes=token_duration
        )

        return (
            token_start.strftime(
                "%I:%M %p"
            ),
            token_end.strftime(
                "%I:%M %p"
            )
        )