from services.consultation_service import ConsultationService
from datetime import datetime
from utils.input_helper import (InputHelper,OperationCancelled)

class ConsultationMenu:

    @staticmethod
    def check_in_patient():

        try:
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            appointment_id = InputHelper.get_input(
                "ENTER APPOINTMENT ID: "
            ).strip().upper()

            ConsultationService.check_in_patient(
                appointment_id
            )

            print(
                "PATIENT CHECKED-IN SUCCESSFULLY"
            )
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

            appointment_id = InputHelper.get_input(
                "ENTER APPOINTMENT ID: "
            ).strip().upper()

            consultation_id = (
                ConsultationService.start_consultation(
                    appointment_id
                )
            )

            print(
                f"CONSULTATION STARTED SUCCESSFULLY. ID: {consultation_id}"
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
            
            followup_required = InputHelper.get_input(
                "FOLLOW-UP REQUIRED (YES/NO): "
            ).strip().upper()

            if followup_required not in [
                "YES",
                "NO"
            ]:

                print(
                    "ENTER YES OR NO ONLY"
                )

                return

            followup_date = None

            if followup_required == "YES":

                followup_date = datetime.strptime(
                    InputHelper.get_input(
                        "ENTER FOLLOW-UP DATE (YYYY-MM-DD): "
                    ),
                    "%Y-%m-%d"
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

            print(
                "CONSULTATION COMPLETED SUCCESSFULLY"
            )
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)
    
    @staticmethod
    def search_consultation():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            consultation_id = InputHelper.get_input(
                "ENTER CONSULTATION ID: "
            ).strip().upper()

            consultation = (
                ConsultationService.search_consultation(
                    consultation_id
                )
            )

            if not consultation:

                print(
                    "CONSULTATION NOT FOUND"
                )

                return

            print(
                "\n===== CONSULTATION DETAILS ====="
            )

            print(
                "CONSULTATION ID :",
                consultation.consultation_id
            )

            print(
                "APPOINTMENT ID :",
                consultation.appointment_id
            )

            print(
                "SYMPTOMS :",
                consultation.symptoms
            )

            print(
                "DIAGNOSIS :",
                consultation.diagnosis
            )

            print(
                "PRESCRIPTION :",
                consultation.prescription
            )

            print(
                "FOLLOW-UP REQUIRED :",
                consultation.followup_required
            )

            print(
                "FOLLOW-UP DATE :",
                consultation.followup_date
            )

            print(
                "STATUS :",
                consultation.consultation_status
            )
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)
        
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

            print(
                "\n===== ALL CONSULTATIONS ====="
            )

            for consultation in consultations:

                print(
                    consultation.consultation_id,
                    "|",
                    consultation.appointment_id,
                    "|",
                    consultation.diagnosis,
                    "|",
                    consultation.consultation_status
                )

        except Exception as e:
            print("ERROR:", e)
    
    @staticmethod
    def show():

        while True:

            print(
                "\n===== CONSULTATION MANAGEMENT ====="
            )
            print("1. CHECK-IN PATIENT")
            print("2. START CONSULTATION")
            print("3. END CONSULTATION")
            print("4. SEARCH CONSULTATION")
            print("5. VIEW ALL CONSULTATIONS")
            print("6. BACK")

            choice = input("ENTER CHOICE: ")

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