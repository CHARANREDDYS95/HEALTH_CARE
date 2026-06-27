import csv
import json

from openpyxl import load_workbook


class ImportHelper:

    @staticmethod
    def import_from_csv(
        file_path
    ):

        with open(
            file_path,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(
                file
            )

            return list(
                reader
            )

    @staticmethod
    def import_from_excel(
        file_path
    ):

        workbook = load_workbook(
            file_path
        )

        worksheet = workbook.active

        rows = list(
            worksheet.values
        )

        headers = rows[0]

        data = []

        for row in rows[1:]:

            data.append(

                dict(

                    zip(
                        headers,
                        row
                    )

                )

            )

        return data

    @staticmethod
    def import_from_json(
        file_path
    ):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(
                file
            )

    @staticmethod
    def import_from_txt(
        file_path
    ):

        data = []

        record = {}

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            for line in file:

                line = line.strip()

                if not line:

                    continue

                if line.startswith(
                    "-"
                ):

                    if record:

                        data.append(
                            record
                        )

                        record = {}

                    continue

                key, value = line.split(
                    ":",
                    1
                )

                record[
                    key.strip()
                ] = value.strip()

        if record:

            data.append(
                record
            )

        return data