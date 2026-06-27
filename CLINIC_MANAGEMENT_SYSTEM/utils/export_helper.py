import csv
import json
import os

from datetime import datetime

from openpyxl import Workbook


class ExportHelper:

    @staticmethod
    def generate_file_path(
        folder_path,
        file_name,
        extension
    ):

        os.makedirs(
            folder_path,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_name = (
            f"{file_name}_{timestamp}.{extension}"
        )

        return os.path.join(
            folder_path,
            file_name
        )

    @staticmethod
    def export_to_csv(
        data,
        folder_path,
        file_name
    ):

        if not data:

            raise ValueError(
                "NO DATA AVAILABLE TO EXPORT"
            )

        file_path = (
            ExportHelper.generate_file_path(
                folder_path,
                file_name,
                "csv"
            )
        )

        with open(
            file_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=data[0].keys()
            )

            writer.writeheader()

            writer.writerows(
                data
            )

        return file_path
    
    @staticmethod
    def export_to_excel(
        data,
        folder_path,
        file_name
    ):

        if not data:

            raise ValueError(
                "NO DATA AVAILABLE TO EXPORT"
            )

        file_path = (
            ExportHelper.generate_file_path(
                folder_path,
                file_name,
                "xlsx"
            )
        )

        workbook = Workbook()

        worksheet = workbook.active

        worksheet.append(
            list(data[0].keys())
        )

        for row in data:

            worksheet.append(
                list(row.values())
            )

        workbook.save(
            file_path
        )

        return file_path
    
    @staticmethod
    def export_to_json(
        data,
        folder_path,
        file_name
    ):

        if not data:

            raise ValueError(
                "NO DATA AVAILABLE TO EXPORT"
            )

        file_path = (
            ExportHelper.generate_file_path(
                folder_path,
                file_name,
                "json"
            )
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                default=str
            )

        return file_path
    
    @staticmethod
    def export_to_txt(
        data,
        folder_path,
        file_name
    ):

        if not data:

            raise ValueError(
                "NO DATA AVAILABLE TO EXPORT"
            )

        file_path = (
            ExportHelper.generate_file_path(
                folder_path,
                file_name,
                "txt"
            )
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            for record in data:

                for key, value in record.items():

                    file.write(
                        f"{key} : {value}\n"
                    )

                file.write(
                    "-" * 50
                )

                file.write(
                    "\n"
                )

        return file_path