from services.appointment_service import AppointmentService
from datetime import date

from utils.input_helper import (
    InputHelper,
    OperationCancelled
)
from services.patient_service import PatientService
from services.doctor_availability_service import (
    DoctorAvailabilityService
)
from services.doctor_service import (
    DoctorService
)
from utils.validators import (
    validate_appointment_date
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

            print(

                f"{'PATIENT ID':<15}"
                f"{'PATIENT NAME':<30}"

            )

            print(

                "=" * 45

            )

            for patient in patients:

                print(

                    f"{patient.patient_id:<15}"
                    f"{patient.patient_name:<30}"

                )

            print(

                "=" * 45

            )

            print("\n==========================================")
            print("          PATIENT TYPE")
            print("==========================================")
            print("1. EXISTING PATIENT")
            print("2. NEW PATIENT")
            print("3. BACK")

            patient_choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )
            
            if patient_choice == "1":

                while True:

                    patient_id = InputHelper.get_input(
                        "\nENTER PATIENT ID: "
                    ).strip().upper()

                    patient = (
                        PatientService.search_patient_by_id(
                            patient_id
                        )
                    )

                    if patient:

                        break

                    print()

                    print(
                        "INVALID PATIENT ID."
                    )

                    print(
                        "PLEASE ENTER A VALID PATIENT ID."
                    )

            elif patient_choice == "2":

                from menus.patient_menu import (
                    PatientMenu
                )

                patient_id = (
                    PatientMenu.register_patient()
                )

                if not patient_id:

                    return

                patient = (
                    PatientService.search_patient_by_id(
                        patient_id
                    )
                )

            elif patient_choice == "3":

                return

            else:

                print(
                    "INVALID CHOICE"
                )

                return
            
            doctors = (
                DoctorService.get_active_doctors()
            )

            if not doctors:

                print(
                    "NO ACTIVE DOCTORS FOUND"
                )

                return

            print(
                "\n========================================================================================="
            )

            print(
                "                              ACTIVE DOCTORS"
            )

            print(
                "========================================================================================="
            )

            print(

                f"{'NO.':<5}"
                f"{'DOCTOR ID':<15}"
                f"{'DOCTOR NAME':<30}"
                f"{'SPECIALIZATION':<30}"

            )

            print(

                "=" * 100

            )

            for index, doctor in enumerate(

                doctors,

                start=1

            ):

                print(

                    f"{index:<5}"
                    f"{doctor.doctor_id:<15}"
                    f"{doctor.doctor_name:<30}"
                    f"{doctor.specialization:<30}"

                )

            print(

                "=" * 100

            )

            while True:

                choice = InputHelper.get_integer(
                    "\nENTER CHOICE: "
                )

                if (

                    1
                    <=
                    choice
                    <=
                    len(
                        doctors
                    )

                ):

                    doctor = doctors[
                        choice - 1
                    ]

                    doctor_id = (
                        doctor.doctor_id
                    )

                    break

                print()

                print(
                    "INVALID CHOICE."
                )

                print(
                    "PLEASE SELECT A VALID DOCTOR."
                )
                
            next_dates = (
                DoctorAvailabilityService.get_next_available_dates(
                    doctor_id
                )
            )

            print(
                "\n============================================================"
            )

            print(
                "                NEXT AVAILABLE DATES"
            )

            print(
                "============================================================"
            )

            print(

                f"{'NO.':<6}"
                f"{'DATE':<15}"
                f"{'DAY':<15}"

            )

            print(
                "=" * 40
            )

            for index, available_date in enumerate(

                next_dates,

                start=1

            ):

                print(

                    f"{index:<6}"
                    f"{str(available_date):<15}"
                    f"{available_date.strftime('%A').upper():<15}"

                )

            print(
                "=" * 40
            )

            print()

            print(
                f"{len(next_dates) + 1}. ENTER ANOTHER DATE"
            )

            print()

            print(
                "============================================================"
            )

            while True:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

                if (

                    choice.isdigit()

                    and

                    1
                    <=
                    int(choice)
                    <=
                    len(next_dates)

                ):

                    appointment_date = (
                        next_dates[
                            int(choice) - 1
                        ]
                    )

                    break

                elif choice == str(
                    len(next_dates) + 1
                ):

                    while True:

                        try:

                            appointment_date = (
                                InputHelper.get_date(
                                    "ENTER APPOINTMENT DATE (YYYY-MM-DD): "
                                )
                            )

                            validate_appointment_date(
                                appointment_date
                            )

                            available_days = [

                                doctor.available_day

                                for doctor in

                                DoctorAvailabilityService.get_doctor_availability(
                                    doctor_id
                                )

                            ]

                            if (

                                appointment_date.strftime(
                                    "%A"
                                ).upper()

                                not in

                                available_days

                            ):

                                print()

                                print(
                                    "DOCTOR IS NOT AVAILABLE ON THE SELECTED DATE."
                                )

                                print(
                                    "PLEASE ENTER ANOTHER DATE."
                                )

                                continue

                            break

                        except ValueError as e:

                            print(
                                "ERROR:",
                                e
                            )

                    break

                else:

                    print(
                        "INVALID CHOICE."
                    )
                
            availability_list = (
                DoctorAvailabilityService.get_doctor_sessions_by_date(
                    doctor_id,
                    appointment_date
                )
            )

            if not availability_list:

                print()

                print(
                    "NO SESSIONS AVAILABLE."
                )

                return

            print(
                "\n============================================================"
            )

            print(
                "                  AVAILABLE SESSIONS"
            )

            print(
                "============================================================"
            )

            print(

                f"{'NO.':<5}"
                f"{'AVAILABILITY ID':<18}"
                f"{'SESSION':<15}"
                f"{'ROOM':<10}"
                f"{'TIME':<25}"

            )

            print(

                "=" * 70

            )

            for index, (

                availability,
                session_name,
                room_id,
                start_time,
                end_time

            ) in enumerate(

                availability_list,

                start=1

            ):

                print(

                    f"{index:<5}"
                    f"{availability.availability_id:<18}"
                    f"{session_name:<15}"
                    f"{room_id:<10}"
                    f"{str(start_time) + ' - ' + str(end_time):<25}"

                )

            print(

                "=" * 70

            )

            while True:

                choice = InputHelper.get_integer(
                    "\nENTER CHOICE: "
                )

                if (

                    1
                    <=
                    choice
                    <=
                    len(
                        availability_list
                    )

                ):

                    availability_id = (

                        availability_list[
                            choice - 1
                        ][0].availability_id

                    )

                    break

                print()

                print(
                    "INVALID CHOICE."
                )

                print(
                    "PLEASE SELECT A VALID SESSION."
                )

               
            tokens = (
                AppointmentService.get_session_tokens(
                    availability_id,
                    appointment_date
                )
            )

            print("\n========================================================")
            print("              SESSION TOKEN STATUS")
            print("========================================================")

            print(

                f"{'TOKEN NO.':<12}"
                f"{'CONSULTATION TIME':<22}"
                f"{'STATUS':<12}"

            )

            print(

                "=" * 50

            )

            for (

                token,
                consultation_time,
                status

            ) in tokens:

                print(

                    f"{token:<12}"
                    f"{consultation_time:<22}"
                    f"{status:<12}"

                )

            print(

                "=" * 50

            )

            available_tokens = [

                str(token)

                for (

                    token,
                    consultation_time,
                    status

                ) in tokens

                if status == "AVAILABLE"

            ]
            
            if not available_tokens:

                print(
                    "\n============================================================"
                )
                print(
                    "        NO TOKENS AVAILABLE FOR THIS SESSION"
                )
                print(
                    "============================================================"
                )
                print(
                    "PLEASE SELECT ANOTHER DOCTOR OR APPOINTMENT DATE."
                )
                print(
                    "============================================================"
                )
                return
            print()

            print(

                "AVAILABLE TOKENS :",

                ", ".join(
                    available_tokens
                )

            )

            print()

            print(

                "=" * 50

            )

            while True:

                token_no = InputHelper.get_integer(
                    "ENTER TOKEN NUMBER: "
                )

                selected_token = None

                for (

                    token,
                    consultation_time,
                    status

                ) in tokens:

                    if token == token_no:

                        selected_token = (
                            token,
                            consultation_time,
                            status
                        )

                        break

                if selected_token is None:

                    print(
                        "\nINVALID TOKEN NUMBER."
                    )

                    print(
                        "AVAILABLE TOKENS :",
                        ", ".join(
                            available_tokens
                        )
                    )

                    continue

                if selected_token[2] == "BOOKED":

                    print(
                        f"\nTOKEN {token_no} IS ALREADY BOOKED."
                    )

                    print(
                        "PLEASE SELECT AN AVAILABLE TOKEN."
                    )

                    print()

                    print(
                        "AVAILABLE TOKENS :",
                        ", ".join(
                            available_tokens
                        )
                    )

                    continue

                break

            reason_for_visit = InputHelper.get_reason(
                "ENTER REASON FOR VISIT: "
            )

            selected_availability = None

            for (

                availability,
                session_name,
                room_id,
                start_time,
                end_time

            ) in availability_list:

                if (

                    availability.availability_id
                    ==
                    availability_id

                ):

                    selected_availability = (

                        session_name,
                        room_id

                    )

                    break

            consultation_time = ""

            for (

                token,
                time,
                status

            ) in tokens:

                if token == token_no:

                    consultation_time = time

                    break

            print(
                "\n============================================================"
            )

            print(
                "                 CONFIRM APPOINTMENT"
            )

            print(
                "============================================================"
            )

            print(
                f"Patient ID         : {patient.patient_id}"
            )

            print(
                f"Patient Name       : {patient.patient_name}"
            )

            print()

            print(
                f"Doctor ID          : {doctor.doctor_id}"
            )

            print(
                f"Doctor Name        : {doctor.doctor_name}"
            )

            print(
                f"Specialization     : {doctor.specialization}"
            )

            print()

            print(
                f"Appointment Date   : {appointment_date}"
            )

            print(
                f"Session            : {selected_availability[0]}"
            )

            print(
                f"Room               : {selected_availability[1]}"
            )

            print(
                f"Consultation Time  : {consultation_time}"
            )

            print(
                f"Token Number       : {token_no}"
            )

            print()

            print(
                f"Reason For Visit   : {reason_for_visit}"
            )

            print(
                "============================================================"
            )

            confirm = InputHelper.get_confirmation()

            if confirm != "Y":

                print()

                print(
                    "BOOKING CANCELLED."
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

            selected_availability = None

            for (

                availability,
                session_name,
                room_id,
                start_time,
                end_time

            ) in availability_list:

                if (

                    availability.availability_id
                    ==
                    availability_id

                ):

                    selected_availability = (

                        session_name,
                        room_id

                    )

                    break

            consultation_time = ""

            for (

                token,
                time,
                status

            ) in tokens:

                if token == token_no:

                    consultation_time = time

                    break

            print(
                "\n============================================================"
            )

            print(
                "           APPOINTMENT BOOKED SUCCESSFULLY"
            )

            print(
                "============================================================"
            )

            print(
                f"Appointment ID     : {appointment_id}"
            )

            print(
                f"Booked On          : {date.today()}"
            )

            print()

            print(
                f"Patient ID         : {patient.patient_id}"
            )

            print(
                f"Patient Name       : {patient.patient_name}"
            )

            print()

            print(
                f"Doctor             : {doctor.doctor_name}"
            )

            print(
                f"Session            : {selected_availability[0]}"
            )

            print(
                f"Room               : {selected_availability[1]}"
            )
            print()

            print(
                f"Appointment Date   : {appointment_date}"
            )

            print(
                f"Consultation Time  : {consultation_time}"
            )

            print(
                f"Token Number       : {token_no}"
            )

            print(
                f"Reason For Visit   : {reason_for_visit}"
            )

            print(
                "Status             : BOOKED"
            )
            print()

            print(
                "============================================================"
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
            print("2. SEARCH BY PATIENT")
            print("3. SEARCH BY DOCTOR")
            print("4. SEARCH BY APPOINTMENT DATE")
            print("5. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

                if choice == "1":

                    appointment_id = InputHelper.get_appointment_id(
                        "\nENTER APPOINTMENT ID (Ex: A001): "
                    )

                    appointment = (
                        AppointmentService.search_appointment_by_id(
                            appointment_id
                        )
                    )

                    if not appointment:

                        print(
                            "\nAPPOINTMENT NOT FOUND"
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

                    patients = (

                        PatientService.get_active_patients()

                    )

                    if not patients:

                        print(

                            "NO ACTIVE PATIENTS FOUND"

                        )

                        continue

                    print("\n============================================================")
                    print("                    ACTIVE PATIENTS")
                    print("============================================================")

                    print(

                        f"{'PATIENT ID':<15}"
                        f"{'PATIENT NAME':<30}"

                    )

                    print(

                        "=" * 45

                    )

                    for patient in patients:

                        print(

                            f"{patient.patient_id:<15}"
                            f"{patient.patient_name:<30}"

                        )

                    print(

                        "=" * 45

                    )

                    patient_id = InputHelper.get_input(

                        "\nENTER PATIENT ID: "

                    ).strip().upper()

                    patient = (
                        PatientService.search_patient_by_id(
                            patient_id
                        )
                    )

                    if not patient:

                        print(
                            "PATIENT NOT FOUND"
                        )

                        continue

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

                    print("\n======================================================================================")
                    print("                                APPOINTMENTS")
                    print("======================================================================================")

                    print(

                        f"{'APP ID':<12}"
                        f"{'DATE':<15}"
                        f"{'AVAILABILITY':<15}"
                        f"{'TOKEN':<10}"
                        f"{'STATUS':<15}"

                    )

                    print(

                        "=" * 70

                    )

                    for appointment in appointments:

                        print(

                            f"{appointment.appointment_id:<12}"
                            f"{str(appointment.appointment_date):<15}"
                            f"{appointment.availability_id:<15}"
                            f"{appointment.token_no:<10}"
                            f"{appointment.appointment_status:<15}"

                        )

                    print(

                        "=" * 70

                    )

                elif choice == "3":

                    doctors = (
                        DoctorService.view_active_doctors()
                    )

                    if not doctors:

                        print(
                            "NO ACTIVE DOCTORS FOUND"
                        )

                        continue

                    print("\n==============================================")
                    print("             ACTIVE DOCTORS")
                    print("==============================================")

                    print(

                        f"{'DOCTOR ID':<15}"
                        f"{'DOCTOR NAME':<30}"

                    )

                    print(

                        "=" * 45

                    )

                    for doctor in doctors:

                        print(

                            f"{doctor.doctor_id:<15}"
                            f"{doctor.doctor_name:<30}"

                        )

                    print(

                        "=" * 45

                    )

                    doctor_id = InputHelper.get_input(

                        "\nENTER DOCTOR ID: "

                    ).strip().upper()

                    doctor = (
                        DoctorService.search_doctor_by_id(
                            doctor_id
                        )
                    )

                    if not doctor:

                        print(
                            "DOCTOR NOT FOUND"
                        )

                        continue

                    appointments = (

                        AppointmentService.search_appointments_by_doctor(

                            doctor_id

                        )

                    )

                    if not appointments:

                        print(

                            "NO APPOINTMENTS FOUND"

                        )

                        continue

                    print("\n==============================================================")
                    print("                    APPOINTMENTS")
                    print("==============================================================")

                    print(

                        f"{'APP ID':<12}"
                        f"{'PATIENT ID':<15}"
                        f"{'DATE':<15}"
                        f"{'TOKEN':<10}"
                        f"{'STATUS':<15}"

                    )

                    print(

                        "=" * 70

                    )

                    for appointment in appointments:

                        print(

                            f"{appointment.appointment_id:<12}"
                            f"{appointment.patient_id:<15}"
                            f"{str(appointment.appointment_date):<15}"
                            f"{appointment.token_no:<10}"
                            f"{appointment.appointment_status:<15}"

                        )

                    print(

                        "=" * 70

                    )

                elif choice == "4":

                    appointment_date = InputHelper.get_date(

                        "ENTER APPOINTMENT DATE (YYYY-MM-DD): "

                    )

                    appointments = (

                        AppointmentService.search_appointments_by_date(

                            appointment_date

                        )

                    )

                    if not appointments:

                        print(

                            "NO APPOINTMENTS FOUND"

                        )

                        continue

                    print("\n======================================================================")
                    print("                    APPOINTMENTS")
                    print("======================================================================")

                    print(

                        f"{'APP ID':<12}"
                        f"{'PATIENT ID':<15}"
                        f"{'AVAILABILITY':<15}"
                        f"{'TOKEN':<10}"
                        f"{'STATUS':<15}"

                    )

                    print(

                        "=" * 70

                    )

                    for appointment in appointments:

                        print(

                            f"{appointment.appointment_id:<12}"
                            f"{appointment.patient_id:<15}"
                            f"{appointment.availability_id:<15}"
                            f"{appointment.token_no:<10}"
                            f"{appointment.appointment_status:<15}"

                        )

                    print(

                        "=" * 70

                    )

                elif choice == "5":

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

            print("\n========================================================================================================")
            print("                                       ALL APPOINTMENTS")
            print("========================================================================================================")

            print(

                f"{'APP ID':<10}"
                f"{'PATIENT ID':<12}"
                f"{'AVAILABILITY':<15}"
                f"{'DATE':<15}"
                f"{'TOKEN':<8}"
                f"{'STATUS':<15}"
                f"{'REASON':<25}"

            )

            print(

                "=" * 100

            )

            for appointment in appointments:

                print(

                    f"{appointment.appointment_id:<10}"
                    f"{appointment.patient_id:<12}"
                    f"{appointment.availability_id:<15}"
                    f"{str(appointment.appointment_date):<15}"
                    f"{appointment.token_no:<8}"
                    f"{appointment.appointment_status:<15}"
                    f"{appointment.reason_for_visit:<25}"

                )

            print(

                "=" * 100

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
            
            appointments = (

                AppointmentService.view_all_appointments()

            )

            booked_appointments = [

                appointment

                for appointment in appointments

                if appointment.appointment_status
                == "BOOKED"

            ]

            if not booked_appointments:

                print(

                    "NO BOOKED APPOINTMENTS FOUND"

                )

                return

            print("\n====================================================================================================")
            print("                                        BOOKED APPOINTMENTS")
            print("====================================================================================================")

            print(

                f"{'APP ID':<10}"
                f"{'PATIENT ID':<15}"
                f"{'DATE':<15}"
                f"{'TOKEN':<10}"
                f"{'STATUS':<15}"

            )

            print(

                "=" * 70

            )

            for appointment in booked_appointments:

                print(

                    f"{appointment.appointment_id:<10}"
                    f"{appointment.patient_id:<15}"
                    f"{str(appointment.appointment_date):<15}"
                    f"{appointment.token_no:<10}"
                    f"{appointment.appointment_status:<15}"

                )

            print(

                "=" * 70

            )

            appointment_id = InputHelper.get_appointment_id(
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
            

            print("\n============================================================")
            print("LEAVE THE FIELD EMPTY AND PRESS ENTER TO KEEP THE CURRENT VALUE")
            print("TYPE A NEW VALUE AND PRESS ENTER TO UPDATE THE FIELD")
            print("============================================================")
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

            while True:

                try:

                    appointment_date = (
                        InputHelper.get_update_date(
                            "ENTER APPOINTMENT DATE",
                            appointment.appointment_date
                        )
                    )

                    validate_appointment_date(
                        appointment_date
                    )

                    break

                except ValueError as e:

                    print(
                        "ERROR:",
                        e
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

            print("\n====================================================================================================")
            print("                                         AVAILABLE DOCTORS")
            print("====================================================================================================")

            print(

                f"{'AVAILABILITY':<15}"
                f"{'DOCTOR':<25}"
                f"{'SESSION':<15}"
                f"{'ROOM':<10}"
                f"{'TIME':<22}"
                f"{'DAY':<12}"

            )

            print(

                "=" * 100

            )

            for (

                availability,
                doctor_name,
                session_name,
                room_id,
                start_time,
                end_time

            ) in availability_list:

                print(

                    f"{availability.availability_id:<15}"
                    f"{doctor_name:<25}"
                    f"{session_name:<15}"
                    f"{room_id:<10}"
                    f"{str(start_time) + ' - ' + str(end_time):<22}"
                    f"{availability.available_day:<12}"

                )

            print(

                "=" * 100

            )

            while True:

                choice = InputHelper.get_integer(
                    "ENTER CHOICE: "
                )

                if (

                    1
                    <=
                    choice
                    <=
                    len(
                        availability_list
                    )

                ):

                    availability_id = (

                        availability_list[
                            choice - 1
                        ][0].availability_id

                    )

                    break

                print()

                print(
                    "INVALID CHOICE."
                )

                print(
                    "PLEASE SELECT A VALID DOCTOR SESSION."
                )
            
            tokens = (
                AppointmentService.get_session_tokens(
                    availability_id,
                    appointment_date
                )
            )

            print("\n========================================================")
            print("              SESSION TOKEN STATUS")
            print("========================================================")

            print(

                f"{'TOKEN NO.':<12}"
                f"{'CONSULTATION TIME':<22}"
                f"{'STATUS':<12}"

            )

            print(

                "=" * 50

            )

            for (

                token,
                consultation_time,
                status

            ) in tokens:

                print(

                    f"{token:<12}"
                    f"{consultation_time:<22}"
                    f"{status:<12}"

                )

            print(

                "=" * 50

            )

            available_tokens = [

                str(token)

                for (

                    token,
                    consultation_time,
                    status

                ) in tokens

                if status == "AVAILABLE"

            ]

            if not available_tokens:

                print()

                print(
                    "NO TOKENS AVAILABLE."
                )

                return

            print()

            print(
                "AVAILABLE TOKENS :",
                ", ".join(
                    available_tokens
                )
            )
            
            reason_for_visit = InputHelper.get_update_reason(
                "ENTER REASON FOR VISIT",
                appointment.reason_for_visit
            )

            while True:

                token_no = InputHelper.get_integer(
                    "ENTER TOKEN NUMBER: "
                )

                if str(token_no) in available_tokens:

                    break

                print()

                print(
                    "INVALID TOKEN NUMBER."
                )

                print()

                print(
                    "AVAILABLE TOKENS :",
                    ", ".join(
                        available_tokens
                    )
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
                token_no,
                reason_for_visit
            )

            print(
                "\n============================================================"
            )

            print(
                "          APPOINTMENT UPDATED SUCCESSFULLY"
            )

            print(
                "============================================================"
            )

            print(
                f"Appointment ID    : {appointment_id}"
            )

            print(
                f"Patient ID        : {appointment.patient_id}"
            )

            print(
                f"Availability ID   : {availability_id}"
            )

            print(
                f"Appointment Date  : {appointment_date}"
            )

            print(
                f"Token Number      : {token_no}"
            )

            print(
                f"Reason For Visit  : {reason_for_visit}"
            )

            print(
                "============================================================"
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

            appointments = (

                AppointmentService.view_all_appointments()

            )

            booked_appointments = [

                appointment

                for appointment in appointments

                if appointment.appointment_status
                == "BOOKED"

            ]

            if not booked_appointments:

                print(

                    "NO BOOKED APPOINTMENTS FOUND"

                )

                return

            print("\n====================================================================================================")
            print("                                        BOOKED APPOINTMENTS")
            print("====================================================================================================")

            print(

                f"{'APP ID':<10}"
                f"{'PATIENT ID':<15}"
                f"{'DATE':<15}"
                f"{'TOKEN':<10}"
                f"{'STATUS':<15}"

            )

            print(

                "=" * 70

            )

            for appointment in booked_appointments:

                print(

                    f"{appointment.appointment_id:<10}"
                    f"{appointment.patient_id:<15}"
                    f"{str(appointment.appointment_date):<15}"
                    f"{appointment.token_no:<10}"
                    f"{appointment.appointment_status:<15}"

                )

            print(

                "=" * 70

            )
            
            appointment_id = InputHelper.get_appointment_id(
                "ENTER APPOINTMENT ID: "
            )

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

                print()

                print(
                    "UPDATE CANCELLED."
                )

                return

            AppointmentService.cancel_appointment(
                appointment_id
            )

            print(
                "\n============================================================"
            )

            print(
                "        APPOINTMENT CANCELLED SUCCESSFULLY"
            )

            print(
                "============================================================"
            )

            print(
                f"Appointment ID    : {appointment.appointment_id}"
            )

            print(
                f"Patient ID        : {appointment.patient_id}"
            )

            print(
                f"Availability ID   : {appointment.availability_id}"
            )

            print(
                f"Appointment Date  : {appointment.appointment_date}"
            )

            print(
                f"Token Number      : {appointment.token_no}"
            )

            print(
                "Status            : CANCELLED"
            )

            print(
                "============================================================"
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
            
