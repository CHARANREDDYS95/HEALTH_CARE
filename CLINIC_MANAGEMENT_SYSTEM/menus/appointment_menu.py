from services.appointment_service import AppointmentService
from utils.input_helper import (
    InputHelper,
    OperationCancelled
)
from services.patient_service import PatientService
from services.doctor_availability_service import (
    DoctorAvailabilityService
)


class AppointmentMenu:

    @staticmethod
    def show():

        while True:

            print("\n==========================================")
            print("         APPOINTMENT MANAGEMENT")
            print("==========================================")
            print("1. BOOK APPOINTMENT")
            print("2. SEARCH APPOINTMENT")
            print("3. VIEW ALL APPOINTMENTS")
            print("4. UPDATE APPOINTMENT")
            print("5. CANCEL APPOINTMENT")
            print("6. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

            except OperationCancelled:

                break

            if choice == "1":

                AppointmentMenu.book_appointment()

            elif choice == "2":

                AppointmentMenu.search_appointment()

            elif choice == "3":

                AppointmentMenu.view_all_appointments()

            elif choice == "4":

                AppointmentMenu.update_appointment()

            elif choice == "5":

                AppointmentMenu.cancel_appointment()

            elif choice == "6":

                break

            else:

                print(
                    "INVALID CHOICE"
                )
    @staticmethod
    def book_appointment():

        try:

            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            print("\n==========================================")
            print("          ACTIVE PATIENTS")
            print("==========================================")

            patients = (
                PatientService.get_active_patients()
            )

            if not patients:

                print(
                    "NO ACTIVE PATIENTS FOUND"
                )

                return

            for patient in patients:

                print(
                    patient.patient_id,
                    "-",
                    patient.patient_name
                )

            patient_id = InputHelper.get_input(
                "\nENTER PATIENT ID: "
            ).strip().upper()

            appointment_date = InputHelper.get_date(
                "ENTER APPOINTMENT DATE (YYYY-MM-DD): "
            )

            availability_list = (
                DoctorAvailabilityService.get_available_by_date(
                    appointment_date
                )
            )

            if not availability_list:

                print(
                    "NO DOCTORS AVAILABLE ON THIS DATE"
                )

                return

            print("\n==========================================")
            print("      AVAILABLE DOCTORS")
            print("==========================================")

            for (
                availability,
                doctor_name,
                session_name,
                room_id,
                start_time,
                end_time
            ) in availability_list:

                print("------------------------------------------")
                print(
                    "AVAILABILITY ID :",
                    availability.availability_id
                )
                print(
                    "DOCTOR          :",
                    doctor_name
                )
                print(
                    "SESSION         :",
                    session_name
                )
                print(
                    "ROOM            :",
                    room_id
                )
                print(
                    "TIME            :",
                    f"{start_time} - {end_time}"
                )
                print(
                    "DAY             :",
                    availability.available_day
                )

            availability_id = InputHelper.get_input(
                "\nENTER AVAILABILITY ID: "
            ).strip().upper()

            reason_for_visit = InputHelper.get_input(
                "ENTER REASON FOR VISIT: "
            )

            confirm = InputHelper.get_confirmation()

            if confirm != "Y":

                print(
                    "BOOKING CANCELLED"
                )

                return

            appointment_id, token_no = (
                AppointmentService.book_appointment(
                    patient_id,
                    availability_id,
                    appointment_date,
                    reason_for_visit
                )
            )

            print("\n==========================================")
            print("APPOINTMENT BOOKED SUCCESSFULLY")
            print("==========================================")
            print(
                "APPOINTMENT ID :",
                appointment_id
            )
            print(
                "TOKEN NUMBER   :",
                token_no
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
    def search_appointment():

        while True:

            print("\n==========================================")
            print("         SEARCH APPOINTMENT")
            print("==========================================")
            print("1. SEARCH BY APPOINTMENT ID")
            print("2. SEARCH BY PATIENT ID")
            print("3. SEARCH BY AVAILABILITY ID")
            print("4. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

                if choice == "1":

                    appointment_id = InputHelper.get_input(
                        "ENTER APPOINTMENT ID: "
                    ).strip().upper()

                    appointment = (
                        AppointmentService.search_appointment_by_id(
                            appointment_id
                        )
                    )

                    if not appointment:

                        print(
                            "APPOINTMENT NOT FOUND"
                        )

                        continue

                    print("\n==========================================")
                    print("       APPOINTMENT DETAILS")
                    print("==========================================")
                    print(
                        "APPOINTMENT ID   :",
                        appointment.appointment_id
                    )
                    print(
                        "PATIENT ID       :",
                        appointment.patient_id
                    )
                    print(
                        "AVAILABILITY ID  :",
                        appointment.availability_id
                    )
                    print(
                        "APPOINTMENT DATE :",
                        appointment.appointment_date
                    )
                    print(
                        "TOKEN NUMBER     :",
                        appointment.token_no
                    )
                    print(
                        "STATUS           :",
                        appointment.appointment_status
                    )
                    print(
                        "REASON           :",
                        appointment.reason_for_visit
                    )

                elif choice == "2":

                    patient_id = InputHelper.get_input(
                        "ENTER PATIENT ID: "
                    ).strip().upper()

                    appointments = (
                        AppointmentService.search_appointments_by_patient(
                            patient_id
                        )
                    )

                    if not appointments:

                        print(
                            "NO APPOINTMENTS FOUND"
                        )

                        continue

                    print("\n==========================================")
                    print("          APPOINTMENTS")
                    print("==========================================")

                    for appointment in appointments:

                        print("------------------------------------------")
                        print(
                            "APPOINTMENT ID :",
                            appointment.appointment_id
                        )
                        print(
                            "DATE           :",
                            appointment.appointment_date
                        )
                        print(
                            "AVAILABILITY   :",
                            appointment.availability_id
                        )
                        print(
                            "TOKEN          :",
                            appointment.token_no
                        )
                        print(
                            "STATUS         :",
                            appointment.appointment_status
                        )

                elif choice == "3":

                    availability_id = InputHelper.get_input(
                        "ENTER AVAILABILITY ID: "
                    ).strip().upper()

                    appointments = (
                        AppointmentService.search_appointments_by_availability(
                            availability_id
                        )
                    )

                    if not appointments:

                        print(
                            "NO APPOINTMENTS FOUND"
                        )

                        continue

                    print("\n==========================================")
                    print("          APPOINTMENTS")
                    print("==========================================")

                    for appointment in appointments:

                        print("------------------------------------------")
                        print(
                            "APPOINTMENT ID :",
                            appointment.appointment_id
                        )
                        print(
                            "PATIENT ID     :",
                            appointment.patient_id
                        )
                        print(
                            "DATE           :",
                            appointment.appointment_date
                        )
                        print(
                            "TOKEN          :",
                            appointment.token_no
                        )
                        print(
                            "STATUS         :",
                            appointment.appointment_status
                        )

                elif choice == "4":

                    return

                else:

                    print(
                        "INVALID CHOICE"
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
    def view_all_appointments():

        try:

            appointments = (
                AppointmentService.view_all_appointments()
            )

            if not appointments:

                print(
                    "NO APPOINTMENTS FOUND"
                )

                return

            print("\n==========================================")
            print("         ALL APPOINTMENTS")
            print("==========================================")

            for appointment in appointments:

                print("------------------------------------------")
                print(
                    "APPOINTMENT ID   :",
                    appointment.appointment_id
                )
                print(
                    "PATIENT ID       :",
                    appointment.patient_id
                )
                print(
                    "AVAILABILITY ID  :",
                    appointment.availability_id
                )
                print(
                    "DATE             :",
                    appointment.appointment_date
                )
                print(
                    "TOKEN NUMBER     :",
                    appointment.token_no
                )
                print(
                    "STATUS           :",
                    appointment.appointment_status
                )
                print(
                    "REASON           :",
                    appointment.reason_for_visit
                )

        except Exception as e:

            print(
                "ERROR:",
                e
            )
            
    @staticmethod
    def update_appointment():

        try:

            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            appointment_id = InputHelper.get_input(
                "ENTER APPOINTMENT ID: "
            ).strip().upper()

            appointment = (
                AppointmentService.search_appointment_by_id(
                    appointment_id
                )
            )

            if not appointment:

                print(
                    "APPOINTMENT NOT FOUND"
                )

                return

            print("\n==========================================")
            print("      CURRENT APPOINTMENT")
            print("==========================================")
            print(
                "PATIENT ID       :",
                appointment.patient_id
            )
            print(
                "AVAILABILITY ID  :",
                appointment.availability_id
            )
            print(
                "DATE             :",
                appointment.appointment_date
            )
            print(
                "TOKEN NUMBER     :",
                appointment.token_no
            )
            print(
                "REASON           :",
                appointment.reason_for_visit
            )

            appointment_date = InputHelper.get_update_date(
                "ENTER APPOINTMENT DATE",
                appointment.appointment_date
            )

            availability_list = (
                DoctorAvailabilityService.get_available_by_date(
                    appointment_date
                )
            )

            if not availability_list:

                print(
                    "NO DOCTORS AVAILABLE ON THIS DATE"
                )

                return

            print("\n==========================================")
            print("      AVAILABLE DOCTORS")
            print("==========================================")

            for (
                availability,
                doctor_name,
                session_name,
                room_id,
                start_time,
                end_time
            ) in availability_list:

                print("------------------------------------------")
                print(
                    "AVAILABILITY ID :",
                    availability.availability_id
                )
                print(
                    "DOCTOR          :",
                    doctor_name
                )
                print(
                    "SESSION         :",
                    session_name
                )
                print(
                    "ROOM            :",
                    room_id
                )
                print(
                    "TIME            :",
                    f"{start_time} - {end_time}"
                )
                print(
                    "DAY             :",
                    availability.available_day
                )

            availability_id = InputHelper.get_update_input(
                "ENTER AVAILABILITY ID",
                appointment.availability_id
            ).strip().upper()

            reason_for_visit = InputHelper.get_update_input(
                "ENTER REASON FOR VISIT",
                appointment.reason_for_visit
            )

            confirm = InputHelper.get_confirmation()

            if confirm != "Y":

                print(
                    "UPDATE CANCELLED"
                )

                return

            AppointmentService.update_appointment(
                appointment_id,
                availability_id,
                appointment_date,
                reason_for_visit
            )

            print(
                "APPOINTMENT UPDATED SUCCESSFULLY"
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
    def cancel_appointment():

        try:

            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            appointment_id = InputHelper.get_input(
                "ENTER APPOINTMENT ID: "
            ).strip().upper()

            appointment = (
                AppointmentService.search_appointment_by_id(
                    appointment_id
                )
            )

            if not appointment:

                print(
                    "APPOINTMENT NOT FOUND"
                )

                return

            print("\n==========================================")
            print("      APPOINTMENT DETAILS")
            print("==========================================")
            print(
                "APPOINTMENT ID   :",
                appointment.appointment_id
            )
            print(
                "PATIENT ID       :",
                appointment.patient_id
            )
            print(
                "AVAILABILITY ID  :",
                appointment.availability_id
            )
            print(
                "DATE             :",
                appointment.appointment_date
            )
            print(
                "TOKEN NUMBER     :",
                appointment.token_no
            )
            print(
                "STATUS           :",
                appointment.appointment_status
            )
            print(
                "REASON           :",
                appointment.reason_for_visit
            )

            confirm = InputHelper.get_confirmation()

            if confirm != "Y":

                print(
                    "CANCELLATION ABORTED"
                )

                return

            AppointmentService.cancel_appointment(
                appointment_id
            )

            print("\n==========================================")
            print("APPOINTMENT CANCELLED SUCCESSFULLY")
            print("==========================================")

        except OperationCancelled as e:

            print(
                e
            )

        except Exception as e:

            print(
                "ERROR:",
                e
            )