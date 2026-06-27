from services.consultation_service import ConsultationService
from utils.input_helper import (InputHelper,OperationCancelled)
from services.appointment_service import (
    AppointmentService
)
from services.patient_service import (
    PatientService
)

from services.doctor_service import (
    DoctorService
)

class ConsultationMenu:

    @staticmethod
    def check_in_patient():

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
            appointment_id = InputHelper.get_input(
                "ENTER APPOINTMENT ID: "
            ).strip().upper()

            ConsultationService.check_in_patient(
                appointment_id
            )

            print("\n==========================================")
            print("PATIENT CHECKED-IN SUCCESSFULLY")
            print("==========================================")
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def start_consultation():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            appointments = (

                AppointmentService.view_all_appointments()

            )

            checked_in_appointments = [

                appointment

                for appointment in appointments

                if appointment.appointment_status
                == "CHECKED_IN"

            ]

            if not checked_in_appointments:

                print(

                    "NO CHECKED-IN PATIENTS FOUND"

                )

                return

            print("\n====================================================================================================")
            print("                                      CHECKED-IN PATIENTS")
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

            for appointment in checked_in_appointments:

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

            appointment_id = InputHelper.get_input(
                "ENTER APPOINTMENT ID: "
            ).strip().upper()

            consultation_id = (
                ConsultationService.start_consultation(
                    appointment_id
                )
            )

            print("\n==========================================")
            print("CONSULTATION STARTED SUCCESSFULLY")
            print("==========================================")
            print(
                "CONSULTATION ID :",
                consultation_id
            )
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def end_consultation():

        try:
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            consultations = (

                ConsultationService.get_all_consultations()

            )

            active_consultations = [

                consultation

                for consultation in consultations

                if consultation.consultation_status
                == "IN_PROGRESS"

            ]

            if not active_consultations:

                print(

                    "NO ACTIVE CONSULTATIONS FOUND"

                )

                return

            print("\n====================================================================================================")
            print("                                      ACTIVE CONSULTATIONS")
            print("====================================================================================================")

            print(

                f"{'CONSULT ID':<15}"
                f"{'APP ID':<12}"
                f"{'STATUS':<20}"

            )

            print(

                "=" * 50

            )

            for consultation in active_consultations:

                print(

                    f"{consultation.consultation_id:<15}"
                    f"{consultation.appointment_id:<12}"
                    f"{consultation.consultation_status:<20}"

                )

            print(

                "=" * 50

            )

            consultation_id = InputHelper.get_input(
                "ENTER CONSULTATION ID: "
                ).strip().upper()

            symptoms = InputHelper.get_input(
                "ENTER SYMPTOMS: "
                )

            diagnosis = InputHelper.get_input(
                "ENTER DIAGNOSIS: "
                )

            prescription = InputHelper.get_input(
                "ENTER PRESCRIPTION: "
                )

            notes = InputHelper.get_input(
                "ENTER NOTES: "
                )
            
            followup_required = InputHelper.get_yes_no(
                "FOLLOW-UP REQUIRED (YES/NO): "
            )

            followup_date = None

            if followup_required == "YES":

                followup_date = InputHelper.get_date(
                    "ENTER FOLLOW-UP DATE (YYYY-MM-DD): "
                )

            ConsultationService.end_consultation(
                consultation_id,
                symptoms,
                diagnosis,
                prescription,
                notes,
                followup_required,
                followup_date
            )

            print("\n==========================================")
            print("CONSULTATION COMPLETED SUCCESSFULLY")
            print("==========================================")
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)
    
    @staticmethod
    def search_consultation():

        while True:

            print("\n==========================================")
            print("       CONSULTATION DETAILS")
            print("==========================================")

            print("1. SEARCH BY CONSULTATION ID")
            print("2. SEARCH BY APPOINTMENT")
            print("3. SEARCH BY PATIENT")
            print("4. SEARCH BY DOCTOR")
            print("5. BACK")

            try:
                
                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

                if choice == "1":

                    consultation = (
                        ConsultationService.search_consultation_by_id(
                            InputHelper.get_input(
                                "ENTER CONSULTATION ID: "
                            ).strip().upper()
                        )
                    )

                elif choice == "2":

                    appointments = (

                        AppointmentService.view_all_appointments()

                    )

                    if not appointments:

                        print(

                            "NO APPOINTMENTS FOUND"

                        )

                        continue

                    print("\n================================================================================")
                    print("                              APPOINTMENTS")
                    print("================================================================================")

                    print(

                        f"{'APP ID':<12}"
                        f"{'PATIENT ID':<15}"
                        f"{'DATE':<15}"
                        f"{'STATUS':<15}"

                    )

                    print(

                        "=" * 60

                    )

                    for appointment in appointments:

                        print(

                            f"{appointment.appointment_id:<12}"
                            f"{appointment.patient_id:<15}"
                            f"{str(appointment.appointment_date):<15}"
                            f"{appointment.appointment_status:<15}"

                        )

                    print(

                        "=" * 60

                    )

                    appointment_id = InputHelper.get_input(

                        "\nENTER APPOINTMENT ID: "

                    ).strip().upper()

                    consultation = (

                        ConsultationService.search_consultation_by_appointment(

                            appointment_id

                        )

                    )
                elif choice == "3":

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

                    consultations = (

                        ConsultationService.search_consultations_by_patient(

                            patient_id

                        )

                    )

                    if not consultations:

                        print(

                            "NO CONSULTATIONS FOUND"

                        )

                        continue

                    print("\n==============================================================================================")
                    print("                                  CONSULTATIONS")
                    print("==============================================================================================")

                    print(

                        f"{'CONSULT ID':<15}"
                        f"{'APP ID':<12}"
                        f"{'STATUS':<20}"

                    )

                    print(

                        "=" * 50

                    )

                    for consultation in consultations:

                        print(

                            f"{consultation.consultation_id:<15}"
                            f"{consultation.appointment_id:<12}"
                            f"{consultation.consultation_status:<20}"

                        )

                    print(

                        "=" * 50

                    )

                    continue
                
                elif choice == "4":

                    doctors = (

                        DoctorService.view_active_doctors()

                    )

                    if not doctors:

                        print(

                            "NO ACTIVE DOCTORS FOUND"

                        )

                        continue

                    print("\n============================================================")
                    print("                    ACTIVE DOCTORS")
                    print("============================================================")

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

                    consultations = (

                        ConsultationService.search_consultations_by_doctor(

                            doctor_id

                        )

                    )

                    if not consultations:

                        print(

                            "NO CONSULTATIONS FOUND"

                        )

                        continue

                    print("\n==============================================================================================")
                    print("                                  CONSULTATIONS")
                    print("==============================================================================================")

                    print(

                        f"{'CONSULT ID':<15}"
                        f"{'APP ID':<12}"
                        f"{'STATUS':<20}"

                    )

                    print(

                        "=" * 50

                    )

                    for consultation in consultations:

                        print(

                            f"{consultation.consultation_id:<15}"
                            f"{consultation.appointment_id:<12}"
                            f"{consultation.consultation_status:<20}"

                        )

                    print(

                        "=" * 50

                    )

                    continue
                
                elif choice == "5":

                    return
                
                else:

                    print(

                        "INVALID CHOICE"

                    )

            except OperationCancelled as e:

                print(e)

            except Exception as e:

                print("ERROR:",e)
        
    @staticmethod
    def view_all_consultations():

        try:
            
            consultations = (
                ConsultationService.get_all_consultations()
            )

            if not consultations:

                print(
                    "NO CONSULTATIONS FOUND"
                )

                return

            print("\n========================================================================================================")
            print("                                      ALL CONSULTATIONS")
            print("========================================================================================================")

            print(

                f"{'CONSULT ID':<15}"
                f"{'APP ID':<12}"
                f"{'DIAGNOSIS':<30}"
                f"{'FOLLOW-UP':<15}"
                f"{'STATUS':<20}"

            )

            print(

                "=" * 95

            )

            for consultation in consultations:

                print(

                    f"{consultation.consultation_id:<15}"
                    f"{consultation.appointment_id:<12}"
                    f"{str(consultation.diagnosis):<30}"
                    f"{consultation.followup_required:<15}"
                    f"{consultation.consultation_status:<20}"

                )

            print(

                "=" * 95

            )

        except Exception as e:
            print("ERROR:", e)
    
    @staticmethod
    def show():

        while True:

            print("\n==========================================")
            print("       CONSULTATION MANAGEMENT")
            print("==========================================")
            print("1. CHECK-IN PATIENT")
            print("2. START CONSULTATION")
            print("3. COMPLETE CONSULTATION")
            print("4. SEARCH CONSULTATION")
            print("5. VIEW ALL CONSULTATIONS")
            print("6. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

            except OperationCancelled as e:

                print(e)

                break

            if choice == "1":
                ConsultationMenu.check_in_patient()

            elif choice == "2":
                ConsultationMenu.start_consultation()

            elif choice == "3":
                ConsultationMenu.end_consultation()

            elif choice == "4":
                ConsultationMenu.search_consultation()

            elif choice == "5":
                ConsultationMenu.view_all_consultations()

            elif choice == "6":
                break

            else:
                print("INVALID CHOICE")