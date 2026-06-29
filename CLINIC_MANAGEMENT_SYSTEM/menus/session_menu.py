from services.session_service import SessionService
from utils.input_helper import (
    InputHelper,
    OperationCancelled
)


class SessionMenu:

    @staticmethod
    def add_session():

        try:

            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            session_name = InputHelper.get_input(
                "ENTER SESSION NAME: "
            ).strip().upper()

            room_id = InputHelper.get_room_choice()

            start_time = InputHelper.get_input(
                "ENTER START TIME (HH:MM AM/PM): "
            )

            end_time = InputHelper.get_input(
                "ENTER END TIME (HH:MM AM/PM): "
            )

            max_patients = InputHelper.get_integer(
                "ENTER MAX PATIENTS: "
            )

            confirm = InputHelper.get_confirmation()

            if confirm == "N":

                print("SESSION CREATION CANCELLED")
                return

            session_id = SessionService.add_session(
                session_name,
                room_id,
                start_time,
                end_time,
                max_patients
            )

            print(
                f"\nSESSION ADDED SUCCESSFULLY. ID: {session_id}"
            )

        except OperationCancelled as e:

            print(e)

        except Exception as e:

            print("ERROR:", e)

    @staticmethod
    def search_session():

        while True:

            print(
                "\n===== SEARCH SESSION ====="
            )

            print("1. SEARCH BY SESSION ID")
            print("2. SEARCH BY SESSION NAME")
            print("3. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

                if choice == "1":

                    session = (
                        SessionService.search_session_by_id(
                            InputHelper.get_input(
                                "ENTER SESSION ID: "
                            ).strip().upper()
                        )
                    )

                elif choice == "2":

                    session = (
                        SessionService.search_session_by_name(
                            InputHelper.get_input(
                                "ENTER SESSION NAME: "
                            ).strip().upper()
                        )
                    )

                elif choice == "3":

                    return

                else:

                    print(
                        "INVALID CHOICE"
                    )

                    continue

                if not session:

                    print(
                        "SESSION NOT FOUND"
                    )

                    continue

                print(
                    "\n===== SESSION DETAILS ====="
                )

                print(
                    "SESSION ID :",
                    session.session_id
                )

                print(
                    "SESSION NAME :",
                    session.session_name
                )

                print(
                    "ROOM :",
                    session.room_id
                )

                print(
                    "START TIME :",
                    session.start_time
                )

                print(
                    "END TIME :",
                    session.end_time
                )

                print(
                    "MAX PATIENTS :",
                    session.max_patients
                )

                print(
                    "STATUS :",
                    session.status
                )

            except OperationCancelled as e:

                print(e)

            except Exception as e:

                print(
                    "ERROR:",
                    e
                )

    @staticmethod
    def view_all_sessions():

        try:

            sessions = SessionService.view_all_sessions()

            if not sessions:

                print("NO SESSIONS FOUND")
                return

            print("\n===== SESSION LIST =====")

            for session in sessions:

                print(
                    session.session_id,
                    session.session_name,
                    session.room_id,
                    session.start_time,
                    session.end_time,
                    session.max_patients,
                    session.status
                )

        except Exception as e:

            print(
                "ERROR:",
                e
            )

    @staticmethod
    def update_session():

        try:

            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            session_id = InputHelper.get_input(
                "ENTER SESSION ID: "
            ).strip().upper()

            session = SessionService.search_session_by_id(
                session_id
            )

            if not session:

                print(
                    "SESSION NOT FOUND"
                )
                return

            session_name = InputHelper.get_update_input(
                "ENTER SESSION NAME",
                session.session_name
            ).strip().upper()

            print("\nSELECT ROOM")
            print("1. CR1")
            print("2. CR2")
            print("PRESS ENTER TO KEEP CURRENT ROOM")

            room_choice = input(
                f"ENTER CHOICE [{'1' if session.room_id == 'CR1' else '2'}]: "
            ).strip()

            if room_choice.upper() == "CANCEL":

                raise OperationCancelled(
                    "OPERATION CANCELLED"
                )

            if room_choice == "":

                room_id = session.room_id

            elif room_choice == "1":

                room_id = "CR1"

            elif room_choice == "2":

                room_id = "CR2"

            else:

                print("INVALID ROOM CHOICE")
                return

            start_time = InputHelper.get_update_time(
                "ENTER START TIME (HH:MM AM/PM)",
                session.start_time
            )

            end_time = InputHelper.get_update_time(
                "ENTER END TIME (HH:MM AM/PM)",
                session.end_time
            )

            max_patients = InputHelper.get_update_integer(
                "ENTER MAX PATIENTS",
                session.max_patients
            )

            confirm = InputHelper.get_confirmation()

            if confirm == "N":

                print(
                    "SESSION UPDATE CANCELLED"
                )
                return

            SessionService.update_session(
                session_id,
                session_name,
                room_id,
                start_time,
                end_time,
                max_patients
            )

            print(
                "SESSION UPDATED SUCCESSFULLY"
            )

        except OperationCancelled as e:

            print(e)

            return

        except Exception as e:

            print(
                "ERROR:",
                e
            )

    @staticmethod
    def change_session_status():

        try:

            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            session_id = InputHelper.get_input(
                "ENTER SESSION ID: "
            ).strip().upper()

            session = SessionService.search_session_by_id(
                session_id
            )

            if not session:

                print(
                    "SESSION NOT FOUND"
                )

                return

            status = InputHelper.get_status_choice(
                session.status
            )

            if status == session.status:

                print(
                    "SESSION IS ALREADY",
                    status
                )

                return

            confirm = InputHelper.get_confirmation()

            if confirm == "N":

                print(
                    "STATUS CHANGE CANCELLED"
                )

                return

            SessionService.change_session_status(
                session_id,
                status
            )

            print(
                "SESSION STATUS UPDATED SUCCESSFULLY"
            )

        except OperationCancelled as e:

            print(e)

            return

        except Exception as e:

            print(
                "ERROR:",
                e
            )

    @staticmethod
    def show():

        while True:

            print("\n==========================================")
            print("            SESSION MASTER")
            print("==========================================")
            print("1. ADD SESSION")
            print("2. SEARCH SESSION")
            print("3. VIEW ALL SESSIONS")
            print("4. UPDATE SESSION")
            print("5. CHANGE SESSION STATUS")
            print("6. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

            except OperationCancelled as e:

                print(e)
                break

            if choice == "1":

                SessionMenu.add_session()

            elif choice == "2":

                SessionMenu.search_session()

            elif choice == "3":

                SessionMenu.view_all_sessions()

            elif choice == "4":

                SessionMenu.update_session()

            elif choice == "5":

                SessionMenu.change_session_status()

            elif choice == "6":

                break

            else:

                print("INVALID CHOICE")