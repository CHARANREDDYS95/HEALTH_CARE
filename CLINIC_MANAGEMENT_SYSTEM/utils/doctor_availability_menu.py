from services.doctor_availability_service import DoctorAvailabilityService
from utils.input_helper import (
    InputHelper,
    OperationCancelled
)


class DoctorAvailabilityMenu:

    @staticmethod
    def show():

        while True:

            print("\n==========================================")
            print("        DOCTOR AVAILABILITY")
            print("==========================================")
            print("1. ASSIGN DOCTOR")
            print("2. SEARCH AVAILABILITY")
            print("3. VIEW ALL AVAILABILITY")
            print("4. UPDATE AVAILABILITY")
            print("5. CHANGE AVAILABILITY STATUS")
            print("6. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

            except OperationCancelled:

                break

            if choice == "1":

                DoctorAvailabilityMenu.assign_doctor()

            elif choice == "2":

                DoctorAvailabilityMenu.search_availability()

            elif choice == "3":

                DoctorAvailabilityMenu.view_all_availability()

            elif choice == "4":

                DoctorAvailabilityMenu.update_availability()

            elif choice == "5":

                DoctorAvailabilityMenu.change_availability_status()

            elif choice == "6":

                break

            else:

                print(
                    "INVALID CHOICE"
                )
    @staticmethod
    def assign_doctor():

        try:

            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            doctor_id = InputHelper.get_input(
                "ENTER DOCTOR ID: "
            ).strip().upper()

            session_id = InputHelper.get_input(
                "ENTER SESSION ID: "
            ).strip().upper()

            available_day = InputHelper.get_day_choice()

            max_patients = InputHelper.get_integer(
                "ENTER MAX PATIENTS: "
            )

            confirm = InputHelper.get_confirmation()

            if confirm == "N":

                print(
                    "DOCTOR ASSIGNMENT CANCELLED"
                )

                return

            availability_id = (
                DoctorAvailabilityService.assign_doctor(
                    doctor_id,
                    session_id,
                    available_day,
                    max_patients
                )
            )

            print(
                "DOCTOR ASSIGNED SUCCESSFULLY"
            )

            print(
                "AVAILABILITY ID :",
                availability_id
            )

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
    def search_availability():

        while True:

            print("\n==========================================")
            print("        SEARCH AVAILABILITY")
            print("==========================================")
            print("1. SEARCH BY AVAILABILITY ID")
            print("2. SEARCH BY DOCTOR ID")
            print("3. SEARCH BY SESSION ID")
            print("4. SEARCH BY DAY")
            print("5. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

                if choice == "1":

                    availability = (
                        DoctorAvailabilityService.search_availability_by_id(
                            InputHelper.get_input(
                                "ENTER AVAILABILITY ID: "
                            ).strip().upper()
                        )
                    )

                    if not availability:

                        print(
                            "AVAILABILITY NOT FOUND"
                        )

                        continue

                    print("\n==========================================")
                    print("      AVAILABILITY DETAILS")
                    print("==========================================")
                    print("AVAILABILITY ID :", availability.availability_id)
                    print("DOCTOR ID      :", availability.doctor_id)
                    print("SESSION ID     :", availability.session_id)
                    print("DAY            :", availability.available_day)
                    print("MAX PATIENTS   :", availability.max_patients)
                    print("STATUS         :", availability.status)

                elif choice == "2":

                    availability_list = (
                        DoctorAvailabilityService.search_availability_by_doctor(
                            InputHelper.get_input(
                                "ENTER DOCTOR ID: "
                            ).strip().upper()
                        )
                    )

                    if not availability_list:

                        print(
                            "NO RECORDS FOUND"
                        )

                        continue

                    for availability in availability_list:

                        print("------------------------------------------")
                        print("AVAILABILITY ID :", availability.availability_id)
                        print("SESSION ID      :", availability.session_id)
                        print("DAY             :", availability.available_day)
                        print("MAX PATIENTS    :", availability.max_patients)
                        print("STATUS          :", availability.status)

                elif choice == "3":

                    availability_list = (
                        DoctorAvailabilityService.search_availability_by_session(
                            InputHelper.get_input(
                                "ENTER SESSION ID: "
                            ).strip().upper()
                        )
                    )

                    if not availability_list:

                        print(
                            "NO RECORDS FOUND"
                        )

                        continue

                    for availability in availability_list:

                        print("------------------------------------------")
                        print("AVAILABILITY ID :", availability.availability_id)
                        print("DOCTOR ID       :", availability.doctor_id)
                        print("DAY             :", availability.available_day)
                        print("MAX PATIENTS    :", availability.max_patients)
                        print("STATUS          :", availability.status)

                elif choice == "4":

                    availability_list = (
                        DoctorAvailabilityService.search_availability_by_day(
                            InputHelper.get_input(
                                "ENTER DAY: "
                            ).strip().upper()
                        )
                    )

                    if not availability_list:

                        print(
                            "NO RECORDS FOUND"
                        )

                        continue

                    for availability in availability_list:

                        print("------------------------------------------")
                        print("AVAILABILITY ID :", availability.availability_id)
                        print("DOCTOR ID       :", availability.doctor_id)
                        print("SESSION ID      :", availability.session_id)
                        print("MAX PATIENTS    :", availability.max_patients)
                        print("STATUS          :", availability.status)

                elif choice == "5":

                    return

                else:

                    print(
                        "INVALID CHOICE"
                    )

            except OperationCancelled as e:

                print(e)

            except Exception as e:

                print(
                    "ERROR:",
                    e
                )
    @staticmethod
    def view_all_availability():

        try:

            availability_list = (
                DoctorAvailabilityService.view_all_availability()
            )

            if not availability_list:

                print(
                    "NO AVAILABILITY RECORDS FOUND"
                )

                return

            print("\n==========================================")
            print("      DOCTOR AVAILABILITY LIST")
            print("==========================================")

            for availability in availability_list:

                print("------------------------------------------")
                print(
                    "AVAILABILITY ID :",
                    availability.availability_id
                )
                print(
                    "DOCTOR ID      :",
                    availability.doctor_id
                )
                print(
                    "SESSION ID     :",
                    availability.session_id
                )
                print(
                    "AVAILABLE DAY  :",
                    availability.available_day
                )
                print(
                    "MAX PATIENTS   :",
                    availability.max_patients
                )
                print(
                    "STATUS         :",
                    availability.status
                )

        except Exception as e:

            print(
                "ERROR:",
                e
            )
    @staticmethod
    def update_availability():

        try:

            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            availability_id = InputHelper.get_input(
                "ENTER AVAILABILITY ID: "
            ).strip().upper()

            availability = (
                DoctorAvailabilityService.search_availability_by_id(
                    availability_id
                )
            )

            if not availability:

                print(
                    "AVAILABILITY NOT FOUND"
                )

                return

            doctor_id = InputHelper.get_update_input(
                "ENTER DOCTOR ID",
                availability.doctor_id
            ).strip().upper()

            session_id = InputHelper.get_update_input(
                "ENTER SESSION ID",
                availability.session_id
            ).strip().upper()

            available_day = InputHelper.get_update_day_choice(
                availability.available_day
            )

            max_patients = InputHelper.get_update_integer(
                "ENTER MAX PATIENTS",
                availability.max_patients
            )

            confirm = InputHelper.get_confirmation()

            if confirm == "N":

                print(
                    "UPDATE OPERATION CANCELLED"
                )

                return

            DoctorAvailabilityService.update_availability(
                availability_id,
                doctor_id,
                session_id,
                available_day,
                max_patients
            )

            print(
                "DOCTOR AVAILABILITY UPDATED SUCCESSFULLY"
            )

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
    def change_availability_status():

        try:

            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            availability_id = InputHelper.get_input(
                "ENTER AVAILABILITY ID: "
            ).strip().upper()

            availability = (
                DoctorAvailabilityService.search_availability_by_id(
                    availability_id
                )
            )

            if not availability:

                print(
                    "AVAILABILITY NOT FOUND"
                )

                return

            status = InputHelper.get_status_choice(
                availability.status
            )

            if status == availability.status:

                print(
                    "STATUS IS ALREADY",
                    status
                )

                return

            confirm = InputHelper.get_confirmation()

            if confirm == "N":

                print(
                    "STATUS CHANGE CANCELLED"
                )

                return

            DoctorAvailabilityService.change_availability_status(
                availability_id,
                status
            )

            print(
                "AVAILABILITY STATUS UPDATED SUCCESSFULLY"
            )

        except OperationCancelled as e:

            print(
                e
            )

        except Exception as e:

            print(
                "ERROR:",
                e
            )