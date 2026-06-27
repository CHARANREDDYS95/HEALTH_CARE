from menus.doctor_menu import DoctorMenu
from menus.patient_menu import PatientMenu
from menus.appointment_menu import AppointmentMenu
from menus.consultation_menu import ConsultationMenu
from menus.billing_menu import BillingMenu
from menus.reports_menu import ReportsMenu
from menus.session_management_menu import (
    SessionManagementMenu
)
from menus.import_export_menu import (
    ImportExportMenu
)


class MainMenu:

    @staticmethod
    def show():

        while True:

            print("\n===================================")
            print(" HEALTHCARE MANAGEMENT SYSTEM ")
            print("===================================")
            print("1. DOCTOR MANAGEMENT")
            print("2. PATIENT MANAGEMENT")
            print("3. SESSION MANAGEMENT")
            print("4. APPOINTMENT MANAGEMENT")
            print("5. CONSULTATION MANAGEMENT")
            print("6. BILLING MANAGEMENT")
            print("7. REPORTS")
            print("8. FILE IMPORT & EXPORT")
            print("9. EXIT")

            choice = input(
                "ENTER CHOICE : "
            ).strip()

            if choice == "1":

                DoctorMenu.show()

            elif choice == "2":

                PatientMenu.show()

            elif choice == "3":

                SessionManagementMenu.show()

            elif choice == "4":

                AppointmentMenu.show()

            elif choice == "5":

                ConsultationMenu.show()

            elif choice == "6":

                BillingMenu.show()

            elif choice == "7":

                ReportsMenu.show()

            elif choice == "8":

                ImportExportMenu.show()

            elif choice == "9":

                print(
                    "THANK YOU"
                )

                break
            else:

                print(
                    "INVALID CHOICE"
                )