from menus.session_menu import SessionMenu
from menus.doctor_availability_menu import DoctorAvailabilityMenu
from utils.input_helper import InputHelper, OperationCancelled
from services.doctor_service import (
    DoctorService
)
from services.doctor_availability_service import (
    DoctorAvailabilityService
)
from utils.display_constants import (
    TABLE_LINE
)

class SessionManagementMenu:

    @staticmethod
    def view_weekly_schedule():

        try:

            doctors = DoctorService.view_active_doctors()

            print("\n")

            print("==============================================")
            print("            ACTIVE DOCTORS")
            print("==============================================")

            print(

                f"{'ID':<10}"
                f"{'DOCTOR NAME':<30}"
                f"{'SPECIALIZATION':<25}"

            )

            print(TABLE_LINE)

            for doctor in doctors:

                print(

                    f"{doctor.doctor_id:<10}"
                    f"{doctor.doctor_name:<30}"
                    f"{doctor.specialization:<25}"

                )

            print(TABLE_LINE)

            doctor_id = InputHelper.get_input(

                "ENTER DOCTOR ID : "

            ).strip().upper()

            schedules = (
                DoctorAvailabilityService.get_doctor_schedule(
                    doctor_id
                )
            )

            if not schedules:

                print(
                    "\nNO SCHEDULE FOUND"
                )

                return

            print("\n==============================================================")
            print("                DOCTOR WEEKLY SCHEDULE")
            print("==============================================================")

            print(
                f"{'DAY':<12}"
                f"{'SESSION':<15}"
                f"{'ROOM':<8}"
                f"{'TIME':<22}"
                f"{'MAX':<5}"
            )

            print(TABLE_LINE)

            for availability, session in schedules:

                print(
                    f"{availability.available_day:<12}"
                    f"{session.session_name:<15}"
                    f"{session.room_id:<8}"
                    f"{session.start_time} - {session.end_time:<12}"
                    f"{availability.max_patients:<5}"
                )

            print(TABLE_LINE)

        except OperationCancelled as e:

            print(
                e
            )

        except Exception as e:

            print(
                "ERROR:",
                e
            )

    @staticmethod
    def show():

        while True:

            print("\n==========================================")
            print("         SESSION MANAGEMENT")
            print("==========================================")
            print("1. SESSION MASTER")
            print("2. DOCTOR AVAILABILITY")
            print("3. VIEW WEEKLY SCHEDULE")
            print("4. BACK")

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

                SessionManagementMenu.view_weekly_schedule()

            elif choice == "4":

                break

            else:

                print("INVALID CHOICE")