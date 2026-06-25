from menus.doctor_menu import DoctorMenu
from menus.patient_menu import PatientMenu
from menus.appointment_menu import AppointmentMenu
from menus.consultation_menu import ConsultationMenu
from menus.billing_menu import BillingMenu


class MainMenu:

    @staticmethod
    def show():

        while True:

            print("\n===================================")
            print(" HEALTHCARE MANAGEMENT SYSTEM ")
            print("===================================")
            print("1. DOCTOR MANAGEMENT")
            print("2. PATIENT MANAGEMENT")
            print("3. APPOINTMENT MANAGEMENT")
            print("4. CONSULTATION MANAGEMENT")
            print("5. BILLING & PAYMENT MANAGEMENT")
            print("6. EXIT")

            choice = input("ENTER CHOICE: ")

            if choice == "1":
                DoctorMenu.show()

            elif choice == "2":
                PatientMenu.show()

            elif choice == "3":
                AppointmentMenu.show()

            elif choice == "4":
                ConsultationMenu.show()

            elif choice == "5":
                BillingMenu.show()

            elif choice == "6":
                print("THANK YOU")
                break

            else:
                print("INVALID CHOICE")