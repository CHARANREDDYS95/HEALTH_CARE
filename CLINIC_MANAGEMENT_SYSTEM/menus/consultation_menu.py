from services.consultation_service import ConsultationService
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
            print("2. SEARCH BY APPOINTMENT ID")
            print("3. BACK")

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

                    consultation = (
                        ConsultationService.search_consultation_by_appointment(
                            InputHelper.get_input(
                                "ENTER APPOINTMENT ID: "
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

                if not consultation:

                    print(
                        "CONSULTATION NOT FOUND"
                    )

                    continue

                print("\n==========================================")
                print("       SEARCH CONSULTATION")
                print("==========================================")

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

            print(
                "\n===== ALL CONSULTATIONS ====="
            )

            for consultation in consultations:

                print("------------------------------------------")
                print(
                    "CONSULTATION ID :",
                    consultation.consultation_id
                )
                print(
                    "APPOINTMENT ID  :",
                    consultation.appointment_id
                )
                print(
                    "DIAGNOSIS       :",
                    consultation.diagnosis
                )
                print(
                    "STATUS          :",
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