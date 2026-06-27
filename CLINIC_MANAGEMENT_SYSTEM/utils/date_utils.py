from datetime import (
    date,
    datetime
)


class DateUtils:

    @staticmethod
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

    @staticmethod
    def today():

        return date.today()

    @staticmethod
    def now():

        return datetime.now()

    @staticmethod
    def format_date(
        date_value,
        date_format="%Y-%m-%d"
    ):

        if date_value is None:

            return ""

        return date_value.strftime(
            date_format
        )