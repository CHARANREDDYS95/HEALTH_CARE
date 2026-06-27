from services.import_export_service import (
    ImportExportService
)

from utils.input_helper import (
    InputHelper,
    OperationCancelled
)

class ImportExportMenu:

    @staticmethod
    def show():

        while True:

            print("\n===================================")
            print("     IMPORT / EXPORT MENU")
            print("===================================")
            print("1. Import Patients")
            print("2. Export Patients")
            print("3. Back")

            choice = input(
                "ENTER CHOICE : "
            ).strip()

            if choice == "1":

                ImportExportMenu.import_patients()

            elif choice == "2":

                ImportExportMenu.export_patients()

            elif choice == "3":

                break

            else:

                print(
                    "INVALID CHOICE"
                )
                
    @staticmethod
    def import_patients():

        try:

            print("\n===================================")
            print("      IMPORT PATIENTS")
            print("===================================")

            print("1. CSV")
            print("2. EXCEL")
            print("3. JSON")
            print("4. TXT")

            choice = input(
                "SELECT FILE FORMAT : "
            ).strip()

            format_map = {

                "1": "CSV",
                "2": "EXCEL",
                "3": "JSON",
                "4": "TXT"

            }

            if choice not in format_map:

                print(
                    "INVALID FILE FORMAT"
                )

                return

            file_format = format_map[
                choice
            ]

            file_path = input(
                "ENTER FILE PATH : "
            ).strip()

            result = (
                ImportExportService.import_patients(
                    file_path,
                    file_format
                )
            )

            print("\n===================================")
            print("        IMPORT SUMMARY")
            print("===================================")

            print(
                f"TOTAL     : {result['total']}"
            )

            print(
                f"IMPORTED  : {result['imported']}"
            )

            print(
                f"SKIPPED   : {result['skipped']}"
            )

            if result["errors"]:

                print("\nERRORS")

                for error in result["errors"]:

                    print(error)

        except OperationCancelled:

            print(
                "IMPORT CANCELLED"
            )

        except Exception as e:

            print(
                f"ERROR : {e}"
            )
            
    @staticmethod
    def export_patients():

        try:

            print("\n===================================")
            print("      EXPORT PATIENTS")
            print("===================================")

            print("1. CSV")
            print("2. EXCEL")
            print("3. JSON")
            print("4. TXT")

            choice = input(
                "SELECT FILE FORMAT : "
            ).strip()

            format_map = {

                "1": "CSV",
                "2": "EXCEL",
                "3": "JSON",
                "4": "TXT"

            }

            if choice not in format_map:

                print(
                    "INVALID FILE FORMAT"
                )

                return

            file_format = format_map[
                choice
            ]

            file_path = (
                ImportExportService.export_patients(
                    file_format
                )
            )

            print("\n===================================")
            print("      EXPORT SUCCESSFUL")
            print("===================================")

            print(
                f"FILE SAVED TO : {file_path}"
            )

        except OperationCancelled:

            print(
                "EXPORT CANCELLED"
            )

        except Exception as e:

            print(
                f"ERROR : {e}"
            )