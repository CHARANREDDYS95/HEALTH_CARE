from menus.session_menu import SessionMenu
from menus.doctor_availability_menu import DoctorAvailabilityMenu
from utils.input_helper import InputHelper, OperationCancelled


class SessionManagementMenu:

    @staticmethod
    def show():

        while True:

            print("\n==========================================")
            print("         SESSION MANAGEMENT")
            print("==========================================")
            print("1. SESSION MASTER")
            print("2. DOCTOR AVAILABILITY")
            print("3. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

            except OperationCancelled:
                break

            if choice == "1":

                SessionMenu.show()

            elif choice == "2":

                DoctorAvailabilityMenu.show()

            elif choice == "3":

                break

            else:

                print("INVALID CHOICE")