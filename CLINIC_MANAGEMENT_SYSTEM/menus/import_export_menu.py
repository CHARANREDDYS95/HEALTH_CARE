import os
from services.import_export_service import (
    ImportExportService
)

from utils.input_helper import (
    OperationCancelled
)
from utils.file_selector import (
    FileSelector
)
from utils.import_log import (
    ImportLog
)



class ImportExportMenu:

    @staticmethod
    def show():

        while True:

            print("\n===================================")
            print("     IMPORT / EXPORT MENU")
            print("===================================")

            print("1. PATIENTS")
            print("2. DOCTORS")
            print("3. BACK")

            choice = input(
                "ENTER CHOICE : "
            ).strip()

            if choice == "1":

                ImportExportMenu.patient_menu()

            elif choice == "2":

                ImportExportMenu.doctor_menu()

            elif choice == "3":

                break

            else:

                print(
                    "INVALID CHOICE"
                )
                
    @staticmethod
    def patient_menu():

        while True:

            print("\n===================================")
            print("    PATIENT IMPORT / EXPORT")
            print("===================================")

            print("1. IMPORT PATIENTS")
            print("2. EXPORT PATIENTS")
            print("3. BACK")

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
    def doctor_menu():

        while True:

            print("\n===================================")
            print("     DOCTOR IMPORT / EXPORT")
            print("===================================")

            print("1. IMPORT DOCTORS")
            print("2. EXPORT DOCTORS")
            print("3. BACK")

            choice = input(
                "ENTER CHOICE : "
            ).strip()

            if choice == "1":

                ImportExportMenu.import_doctors()

            elif choice == "2":

                ImportExportMenu.export_doctors()

            elif choice == "3":

                break

            else:

                print(
                    "INVALID CHOICE"
                )
                
    @staticmethod
    def import_doctors():

        try:

            print("\n===================================")
            print("      IMPORT DOCTORS")
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

            extension_map = {

                "CSV": ".csv",
                "EXCEL": ".xlsx",
                "JSON": ".json",
                "TXT": ".txt"

            }

            selected_files = FileSelector.select_files(

                "imports/doctors",

                extension_map[
                    file_format
                ],

                file_format

            )

            if not selected_files:

                return

            grand_total = 0

            grand_imported = 0

            grand_skipped = 0

            total_files = len(
                selected_files
            )

            all_errors = []

            print("\n==============================================================")
            print("                    IMPORT SUMMARY")
            print("==============================================================")

            print(
                f"FILES SELECTED : {total_files}"
            )

            print()

            print(
                f"{'FILE NAME':30}"
                f"{'TOTAL':>8}"
                f"{'IMPORTED':>12}"
                f"{'SKIPPED':>10}"
            )

            print("-" * 62)

            for file_path in selected_files:

                result = (
                    ImportExportService.import_doctors(
                        file_path,
                        file_format
                    )
                )

                grand_total += result[
                    "total"
                ]

                grand_imported += result[
                    "imported"
                ]

                grand_skipped += result[
                    "skipped"
                ]

                print(

                    f"{os.path.basename(file_path):30}"

                    f"{result['total']:>8}"

                    f"{result['imported']:>12}"

                    f"{result['skipped']:>10}"

                )

                if result["errors"]:

                    all_errors.append({

                        "file":

                        os.path.basename(
                            file_path
                        ),

                        "errors":

                        result["errors"]

                    })
                        
            print("-" * 62)

            print(

                f"{'GRAND TOTAL':30}"

                f"{grand_total:>8}"

                f"{grand_imported:>12}"

                f"{grand_skipped:>10}"

            )

            print("=" * 62)

            if all_errors:

                print("\n==============================================================")
                print("                    ERROR DETAILS")
                print("==============================================================")

                for item in all_errors:

                    print()

                    print(
                        f"FILE : {item['file']}"
                    )

                    print()

                    for error in item["errors"]:

                        print(
                            error
                        )

                log_file = ImportLog.save_log(

                    "DOCTOR",

                    all_errors

                )

                if log_file:

                    print()

                    print("==============================================================")
                    print("                     IMPORT LOG")
                    print("==============================================================")

                    print(
                        f"LOG FILE : {log_file}"
                    )

                    print("=" * 62)

            else:

                print()

                print(
                    "ALL RECORDS IMPORTED SUCCESSFULLY."
                )

            print()

            input(
                "PRESS ENTER TO CONTINUE..."
            )

        except OperationCancelled:

            print(
                "IMPORT CANCELLED"
            )

        except Exception as e:

            print(
                f"ERROR : {e}"
            )
            

                
    @staticmethod
    def export_doctors():

        try:

            print("\n===================================")
            print("      EXPORT DOCTORS")
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

            result = (
                ImportExportService.export_doctors(
                    file_format
                )
            )

            print("\n==============================================================")
            print("                    EXPORT SUMMARY")
            print("==============================================================")

            print(
                f"MODULE        : {result['module']}"
            )

            print(
                f"FORMAT        : {result['format']}"
            )

            print(
                f"TOTAL RECORDS : {result['total_records']}"
            )

            print(
                f"FILE NAME     : {os.path.basename(result['file_path'])}"
            )

            print(
                f"LOCATION      : {os.path.dirname(result['file_path'])}"
            )

            print("==============================================================")

            print()

            print(
                "EXPORT COMPLETED SUCCESSFULLY."
            )

            print()

            input(
                "PRESS ENTER TO CONTINUE..."
            )

        except OperationCancelled:

            print(
                "EXPORT CANCELLED"
            )

        except Exception as e:

            print(
                f"ERROR : {e}"
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

            extension_map = {

                "CSV": ".csv",
                "EXCEL": ".xlsx",
                "JSON": ".json",
                "TXT": ".txt"

            }

            selected_files = FileSelector.select_files(

                "imports/patients",

                extension_map[
                    file_format
                ],

                file_format

            )

            if not selected_files:

                return

            grand_total = 0

            grand_imported = 0

            grand_skipped = 0

            total_files = len(
                selected_files
            )

            all_errors = []

            print("\n==============================================================")
            print("                    IMPORT SUMMARY")
            print("==============================================================")

            print(
                f"FILES SELECTED : {total_files}"
            )

            print()

            print(
                f"{'FILE NAME':30}"
                f"{'TOTAL':>8}"
                f"{'IMPORTED':>12}"
                f"{'SKIPPED':>10}"
            )

            print("-" * 62)

            for file_path in selected_files:

                result = (
                    ImportExportService.import_patients(
                        file_path,
                        file_format
                    )
                )

                grand_total += result[
                    "total"
                ]

                grand_imported += result[
                    "imported"
                ]

                grand_skipped += result[
                    "skipped"
                ]

                print(

                    f"{os.path.basename(file_path):30}"

                    f"{result['total']:>8}"

                    f"{result['imported']:>12}"

                    f"{result['skipped']:>10}"

                )

                if result["errors"]:

                    all_errors.append({

                        "file":

                        os.path.basename(
                            file_path
                        ),

                        "errors":

                        result["errors"]

                    })
                        
            print("-" * 62)

            print(

                f"{'GRAND TOTAL':30}"

                f"{grand_total:>8}"

                f"{grand_imported:>12}"

                f"{grand_skipped:>10}"

            )

            print("=" * 62)

            if all_errors:

                print("\n==============================================================")
                print("                    ERROR DETAILS")
                print("==============================================================")

                for item in all_errors:

                    print()

                    print(
                        f"FILE : {item['file']}"
                    )

                    print()

                    for error in item["errors"]:

                        print(
                            error
                        )

                log_file = ImportLog.save_log(

                    "DOCTOR",

                    all_errors

                )

                if log_file:

                    print()

                    print("==============================================================")
                    print("                      IMPORT LOG")
                    print("==============================================================")

                    print(
                        f"LOG FILE : {log_file}"
                    )

                    print("=" * 62)

            else:

                print()

                print(
                    "ALL RECORDS IMPORTED SUCCESSFULLY."
                )

            print()

            input(
                "PRESS ENTER TO CONTINUE..."
            )

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

            result = (
                ImportExportService.export_patients(
                    file_format
                )
            )

            print("\n==============================================================")
            print("                    EXPORT SUMMARY")
            print("==============================================================")

            print(
                f"MODULE        : {result['module']}"
            )

            print(
                f"FORMAT        : {result['format']}"
            )

            print(
                f"TOTAL RECORDS : {result['total_records']}"
            )

            print(
                f"FILE NAME     : {os.path.basename(result['file_path'])}"
            )

            print(
                f"LOCATION      : {os.path.dirname(result['file_path'])}"
            )

            print("==============================================================")

            print()

            print(
                "EXPORT COMPLETED SUCCESSFULLY."
            )

            print()

            input(
                "PRESS ENTER TO CONTINUE..."
            )

        except OperationCancelled:

            print(
                "EXPORT CANCELLED"
            )

        except Exception as e:

            print(
                f"ERROR : {e}"
            )