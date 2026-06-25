from datetime import datetime, timedelta
from services.appointment_service import AppointmentService
from services.patient_service import PatientService
from services.doctor_service import DoctorService
from utils.token_helper import TokenHelper
from services.doctor_availability_service import (DoctorAvailabilityService)
from utils.input_helper import (InputHelper,OperationCancelled)


class AppointmentMenu:

    @staticmethod
    def book_appointment():

        try:
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            print("\n===== ACTIVE PATIENTS =====")
            
            patients = (
                PatientService.get_active_patients()
            )

            for patient in patients:

                print(
                    patient.patient_id,
                    "-",
                    patient.patient_name
                )

            patient_id = InputHelper.get_input(
                "\nENTER PATIENT ID: "
            ).strip().upper()
            
            print("\n===== ACTIVE DOCTORS =====")

            doctors = (
                DoctorService.get_active_doctors()
            )

            for doctor in doctors:

                print(
                    doctor.doctor_id,
                    "-",
                    doctor.doctor_name,
                    "-",
                    doctor.specialization
                )

            doctor_id = InputHelper.get_input(
                "\nENTER DOCTOR ID: "
            ).strip().upper()
            
            
            available_dates = (
                DoctorAvailabilityService
                .get_next_available_dates(
                    doctor_id
                )
            )

            print(
                "\n===== NEXT AVAILABLE DATES ====="
            )

            for index, date in enumerate(
                    available_dates,
                    start=1
            ):

                print(
                    f"{index}. "
                    f"{date.strftime('%A').upper()} "
                    f"({date})"
                )
                
            print("4. ENTER ANOTHER DATE")

            date_option = InputHelper.get_input(
                "\nSELECT OPTION: "
            )
            
            if date_option in ["1", "2", "3"]:

                appointment_date = (
                    available_dates[
                        int(date_option) - 1
                    ]
                )

            elif date_option == "4":

                appointment_date = datetime.strptime(
                    InputHelper.get_input(
                        "ENTER APPOINTMENT DATE (YYYY-MM-DD): "
                    ),
                    "%Y-%m-%d"
                ).date()

            else:

                print(
                    "INVALID OPTION"
                )

                return
            
            availability = (
                DoctorAvailabilityService
                .get_available_sessions(
                    doctor_id,
                    appointment_date
                )
            )

            if not availability:

                print(
                    "\nDOCTOR NOT AVAILABLE "
                    "ON SELECTED DATE"
                )

                return

            print(
                "\n===== AVAILABLE SESSIONS ====="
            )

            for item in availability:

                print(
                    item.session_id,
                    "-",
                    item.start_time,
                    "TO",
                    item.end_time
                )

            session_id = InputHelper.get_input(
                "\nENTER SESSION ID: "
            ).strip().upper()
            
            booked_tokens = (
                AppointmentService.get_booked_tokens(
                    doctor_id,
                    session_id,
                    appointment_date
                )
            )

            print(
                "\n===== AVAILABLE TOKENS ====="
            )
            
            valid_sessions = [
                item.session_id
                for item in availability
            ]

            if session_id not in valid_sessions:

                print(
                    "INVALID SESSION ID"
                    )

                return
            session_details = (
                AppointmentService.get_session_details(
                    session_id
                )
            )

            start_time = datetime.strptime(
                session_details.start_time,
                "%I:%M %p"
            )

            for token_no in range(1, 11):

                token_start = (
                    start_time +
                    timedelta(
                        minutes=(token_no - 1) * 12
                    )
                )

                token_end = (
                    token_start +
                    timedelta(minutes=12)
                )

                if token_no in booked_tokens:

                    print(
                        f"TOKEN {token_no} - BOOKED"
                    )

                else:

                    print(
                        f"TOKEN {token_no} "
                        f"({token_start.strftime('%I:%M %p')} - "
                        f"{token_end.strftime('%I:%M %p')})"
                    )
                
            selected_token = int(
                InputHelper.get_input(
                    "\nENTER TOKEN NUMBER: "
                )
            )

            reason_for_visit = InputHelper.get_input(
                "ENTER REASON FOR VISIT: "
            )

            confirm = InputHelper.get_input(
                "\nCONFIRM APPOINTMENT (Y/N): "
            ).strip().upper()
            
            if selected_token in booked_tokens:

                print(
                    "TOKEN ALREADY BOOKED"
                )

                return

            if selected_token < 1 or selected_token > 10:

                print(
                    "INVALID TOKEN NUMBER"
                )

                return

            if confirm != "Y":

                print(
                    "APPOINTMENT BOOKING CANCELLED"
                )

                return

            appointment_id = (
                AppointmentService.book_appointment(
                    patient_id,
                    doctor_id,
                    session_id,
                    appointment_date,
                    selected_token,
                    reason_for_visit
                )
            )

            print(
                f"APPOINTMENT BOOKED SUCCESSFULLY. ID: {appointment_id}"
            )
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("MESSAGE:", e)

    @staticmethod
    def search_appointment():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            appointment_id = InputHelper.get_input(
                "ENTER APPOINTMENT ID: "
            ).strip().upper()

            appointment = (
                AppointmentService.search_appointment(
                    appointment_id
                )
            )

            if appointment:

                print(
                    "\n===== APPOINTMENT DETAILS ====="
                )

                print(
                    "APPOINTMENT ID :",
                    appointment.appointment_id
                )

                patient = PatientService.search_patient(
                    appointment.patient_id
                )

                print(
                    "PATIENT :",
                    appointment.patient_id,
                    "-",
                    patient.patient_name
                )

                doctor = DoctorService.search_doctor(
                    appointment.doctor_id
                )

                print(
                    "DOCTOR :",
                    appointment.doctor_id,
                    "-",
                    doctor.doctor_name
                )

                session_obj = (
                    AppointmentService.get_session_details(
                        appointment.session_id
                    )
                )

                print(
                    "SESSION :",
                    appointment.session_id,
                    "-",
                    session_obj.session_name
                    )

                print(
                    "APPOINTMENT DATE :",
                    appointment.appointment_date
                )

                print(
                    "TOKEN NO :",
                    appointment.token_no
                )
                
                token_start,token_end = (
                    TokenHelper.get_token_time(
                        session_obj.start_time,
                        appointment.token_no
                    )
                )

                print(
                    "TOKEN TIME :",
                    token_start,
                    "TO",
                    token_end
                )

                print(
                    "STATUS :",
                    appointment.appointment_status
                )

                print(
                    "REASON :",
                    appointment.reason_for_visit
                )

            else:
                print("APPOINTMENT NOT FOUND")
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("MESSAGE:", e)

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
                AppointmentService.search_appointment(
                    appointment_id
                )
            )

            if not appointment:
                print("APPOINTMENT NOT FOUND")
                return

            patient = PatientService.search_patient(
                appointment.patient_id
            )

            doctor = DoctorService.search_doctor(
                appointment.doctor_id
            )

            print(
                "\n===== CURRENT APPOINTMENT ====="
            )

            print(
                "PATIENT :",
                appointment.patient_id,
                "-",
                patient.patient_name
            )

            print(
                "DOCTOR :",
                appointment.doctor_id,
                "-",
                doctor.doctor_name
            )

            print(
                "SESSION ID :",
                appointment.session_id
            )

            print(
                "APPOINTMENT DATE :",
                appointment.appointment_date
            )

            print(
                "TOKEN NO :",
                appointment.token_no
            )

            print(
                "REASON :",
                appointment.reason_for_visit
            )

            session_obj = (
                AppointmentService.get_session_details(
                    appointment.session_id
                )
            )

            print(
                "CURRENT SESSION :",
                appointment.session_id,
                "-",
                session_obj.session_name
            )

            available_dates = (
                DoctorAvailabilityService
                .get_next_available_dates(
                    appointment.doctor_id
                )
            )

            print(
                "\n===== NEXT AVAILABLE DATES ====="
            )

            for index, date in enumerate(
                available_dates,
                start=1
            ):

                print(
                    f"{index}. "
                    f"{date.strftime('%A').upper()} "
                    f"({date})"
                )

            print("4. ENTER ANOTHER DATE")

            date_option = InputHelper.get_input(
                "\nSELECT OPTION: "
            )

            if date_option in ["1", "2", "3"]:

                appointment_date = (
                    available_dates[
                        int(date_option) - 1
                    ]
                )

            elif date_option == "4":

                appointment_date = datetime.strptime(
                    InputHelper.get_input(
                        "ENTER APPOINTMENT DATE (YYYY-MM-DD): "
                    ),
                    "%Y-%m-%d"
                ).date()

            else:

                print(
                    "INVALID OPTION"
                )

                return

            availability = (
                DoctorAvailabilityService
                .get_available_sessions(
                    appointment.doctor_id,
                    appointment_date
                )
            )

            if not availability:

                print(
                    "DOCTOR NOT AVAILABLE ON SELECTED DATE"
                )

                return

            print(
                "\n===== AVAILABLE SESSIONS ====="
            )

            for item in availability:

                print(
                    item.session_id,
                    "-",
                    item.start_time,
                    "TO",
                    item.end_time
                )

            session_id = InputHelper.get_update_input(
                "ENTER SESSION ID",
                appointment.session_id
            ).strip().upper()

            valid_sessions = [
                item.session_id
                for item in availability
            ]

            if session_id not in valid_sessions:

                print(
                    "INVALID SESSION ID"
                )

                return

            booked_tokens = (
                AppointmentService.get_booked_tokens(
                    appointment.doctor_id,
                    session_id,
                    appointment_date
                )
            )

            print(
                "\n===== AVAILABLE TOKENS ====="
            )

            for token in range(1, 11):

                if token == appointment.token_no:

                    print(
                        f"TOKEN {token} - CURRENT"
                    )

                elif token in booked_tokens:

                    print(
                        f"TOKEN {token} - BOOKED"
                    )

                else:

                    print(
                        f"TOKEN {token} - AVAILABLE"
                    )

            token_no = int(
                InputHelper.get_update_input(
                    "ENTER TOKEN NO",
                    appointment.token_no
                )
            )       

            reason_for_visit = InputHelper.get_update_input(
                "ENTER REASON FOR VISIT",
                appointment.reason_for_visit
            )

            confirm = InputHelper.get_input(
                "\nCONFIRM UPDATE (Y/N): "
            ).strip().upper()


            if confirm != "Y":

                print(
                    "APPOINTMENT UPDATE CANCELLED"
                )

                return

            AppointmentService.update_appointment(
                appointment_id,
                session_id,
                appointment_date,
                token_no,
                reason_for_visit
            )

            print(
                "APPOINTMENT UPDATED SUCCESSFULLY"
            )
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("MESSAGE:", e)

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
                AppointmentService.search_appointment(
                    appointment_id
                )
            )

            if not appointment:

                print(
                    "APPOINTMENT NOT FOUND"
                )

                return

            patient = PatientService.search_patient(
                appointment.patient_id
            )

            doctor = DoctorService.search_doctor(
                appointment.doctor_id
            )

            print(
                "\n===== APPOINTMENT DETAILS ====="
            )

            print(
                "PATIENT :",
                appointment.patient_id,
                "-",
                patient.patient_name
            )

            print(
                "DOCTOR :",
                appointment.doctor_id,
                "-",
                doctor.doctor_name
            )

            print(
                "APPOINTMENT DATE :",
                appointment.appointment_date
            )

            print(
                "TOKEN NO :",
                appointment.token_no
            )

            print(
                "STATUS :",
                appointment.appointment_status
            )

            if appointment.appointment_status == "CANCELLED":

                print(
                    "APPOINTMENT IS ALREADY CANCELLED"
                )

                return

            confirm = InputHelper.get_input(
                "\nCONFIRM CANCELLATION (Y/N): "
            ).strip().upper()

            if confirm != "Y":

                print(
                    "APPOINTMENT CANCELLATION CANCELLED"
                )

                return

            AppointmentService.cancel_appointment(
                appointment_id
            )

            print(
                "APPOINTMENT CANCELLED SUCCESSFULLY"
            )
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("MESSAGE:", e)
     
    @staticmethod
    def view_all_appointments():

        try:

            appointments = (
                AppointmentService.get_all_appointments()
            )

            if not appointments:

                print(
                    "NO APPOINTMENTS FOUND"
                )

                return

            print(
                "\n===== ALL APPOINTMENTS ====="
            )

            for appointment in appointments:

                print(
                    appointment.appointment_id,
                    "|",
                    appointment.patient_id,
                    "|",
                    appointment.doctor_id,
                    "|",
                    appointment.appointment_date,
                    "|",
                    appointment.token_no,
                    "|",
                    appointment.appointment_status
                )

        except Exception as e:
            print("MESSAGE:", e)
    
    @staticmethod
    def show():

        while True:

            print(
                "\n===== APPOINTMENT MANAGEMENT ====="
            )
            print("1. BOOK APPOINTMENT")
            print("2. SEARCH APPOINTMENT")
            print("3. UPDATE APPOINTMENT")
            print("4. CANCEL APPOINTMENT")
            print("5. VIEW ALL APPOINTMENTS")
            print("6. BACK")

            choice = input("ENTER CHOICE: ")

            if choice == "1":
                AppointmentMenu.book_appointment()

            elif choice == "2":
                AppointmentMenu.search_appointment()

            elif choice == "3":
                AppointmentMenu.update_appointment()

            elif choice == "4":
                AppointmentMenu.cancel_appointment()

            elif choice == "5":
                AppointmentMenu.view_all_appointments()

            elif choice == "6":
                break
