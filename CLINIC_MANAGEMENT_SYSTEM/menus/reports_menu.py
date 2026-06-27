from services.reports_service import ReportsService
from utils.export_helper import ExportHelper
from utils.input_helper import (
    InputHelper,
    OperationCancelled
)


class ReportsMenu:

    REPORTS_FOLDER = (
        "downloads/reports"
    )
    @staticmethod
    def download_report(
        data,
        file_name
    ):

        print("\n==========================================")
        print("         SELECT FILE FORMAT")
        print("==========================================")

        print("1. CSV")
        print("2. EXCEL")
        print("3. JSON")
        print("4. TXT")
        print("5. BACK")

        choice = InputHelper.get_input(
            "ENTER CHOICE: "
        )

        if choice == "1":

            path = ExportHelper.export_to_csv(
                data,
                ReportsMenu.REPORTS_FOLDER,
                file_name
            )

        elif choice == "2":

            path = ExportHelper.export_to_excel(
                data,
                ReportsMenu.REPORTS_FOLDER,
                file_name
            )

        elif choice == "3":

            path = ExportHelper.export_to_json(
                data,
                ReportsMenu.REPORTS_FOLDER,
                file_name
            )

        elif choice == "4":

            path = ExportHelper.export_to_txt(
                data,
                ReportsMenu.REPORTS_FOLDER,
                file_name
            )

        elif choice == "5":

            return

        else:

            print(
                "INVALID CHOICE"
            )

            return

        print("\n==========================================")
        print("REPORT EXPORTED SUCCESSFULLY")
        print("==========================================")

        print(
            "LOCATION :",
            path
        )

    @staticmethod
    def view_or_download_report(
        data,
        file_name
    ):

        while True:

            print("\n==========================================")
            print("          REPORT OPTIONS")
            print("==========================================")

            print("1. VIEW REPORT")
            print("2. DOWNLOAD REPORT")
            print("3. BACK")

            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                if not data:

                    print(
                        "NO DATA FOUND"
                    )

                    continue

                print("\n====================================================================================================")

                headers = list(

                    data[0].keys()

                )

                for header in headers:

                    print(

                        f"{header.upper():<25}",

                        end=""

                    )

                print()

                print(

                    "=" * (25 * len(headers))

                )

                for row in data:

                    for value in row.values():

                        print(

                            f"{str(value):<25}",

                            end=""

                        )

                    print()

                print(

                    "=" * (25 * len(headers))

                )

            elif choice == "2":

                ReportsMenu.download_report(
                    data,
                    file_name
                )

            elif choice == "3":

                return

            else:

                print(
                    "INVALID CHOICE"
                )
                
    @staticmethod
    def doctor_wise_appointment_count():

        data = (
            ReportsService.doctor_wise_appointment_count()
        )

        ReportsMenu.view_or_download_report(
            data,
            "doctor_wise_appointment_count"
        )

    @staticmethod
    def city_wise_patient_count():

        data = (
            ReportsService.city_wise_patient_count()
        )

        ReportsMenu.view_or_download_report(
            data,
            "city_wise_patient_count"
        )

    @staticmethod
    def doctor_wise_revenue():

        data = (
            ReportsService.doctor_wise_revenue()
        )

        ReportsMenu.view_or_download_report(
            data,
            "doctor_wise_revenue"
        )

    @staticmethod
    def daily_appointment_summary():

        data = (
            ReportsService.daily_appointment_summary()
        )

        ReportsMenu.view_or_download_report(
            data,
            "daily_appointment_summary"
        )
        
    @staticmethod
    def show():

        while True:

            print(
                "\n=========================================="
            )

            print(
                "               REPORTS"
            )

            print(
                "=========================================="
            )

            print(
                "1. DOCTOR-WISE APPOINTMENT COUNT"
            )

            print(
                "2. CITY-WISE PATIENT COUNT"
            )

            print(
                "3. REVENUE GENERATED DOCTOR-WISE"
            )

            print(
                "4. DAILY APPOINTMENT SUMMARY"
            )

            print(
                "5. BACK"
            )

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

            except OperationCancelled as e:

                print(e)

                break

            if choice == "1":

                ReportsMenu.doctor_wise_appointment_count()

            elif choice == "2":

                ReportsMenu.city_wise_patient_count()

            elif choice == "3":

                ReportsMenu.doctor_wise_revenue()

            elif choice == "4":

                ReportsMenu.daily_appointment_summary()

            elif choice == "5":

                break

            else:

                print(
                    "INVALID CHOICE"
                )