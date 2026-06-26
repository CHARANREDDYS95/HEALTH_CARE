from services.patient_service import PatientService
from utils.input_helper import (
    InputHelper,
    OperationCancelled
)

from utils.display_constants import (
    TABLE_LINE
)


class PatientMenu:

    @staticmethod
    def register_patient():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            patient_name = InputHelper.get_input(
                "ENTER PATIENT NAME: "
            )

            gender = InputHelper.get_choice(
                "ENTER GENDER (M/F/O): ",
                ["M", "F", "O"]
            )

            dob = InputHelper.get_date(
                "ENTER DOB (YYYY-MM-DD): "
            )

            phone = InputHelper.get_input(
                "ENTER PHONE NUMBER: "
            )

            address = InputHelper.get_input(
                "ENTER ADDRESS: "
            )

            city = InputHelper.get_input(
                "ENTER CITY: "
            )

            blood_group = InputHelper.get_input(
                "ENTER BLOOD GROUP: "
            )

            occupation = InputHelper.get_input(
                "ENTER OCCUPATION: "
            )

            marital_status = InputHelper.get_input(
                "ENTER MARITAL STATUS: "
            )

            allergies = InputHelper.get_input(
                "ENTER ALLERGIES: "
            )

            emergency_contact_name = InputHelper.get_input(
                "ENTER EMERGENCY CONTACT NAME: "
            )

            emergency_phone = InputHelper.get_input(
                "ENTER EMERGENCY PHONE: "
            )

            registration_date = InputHelper.get_date(
                "ENTER REGISTRATION DATE (YYYY-MM-DD): "
            )

            patient_status = InputHelper.get_choice(
                "ENTER STATUS (ACTIVE/INACTIVE): ",
                ["ACTIVE", "INACTIVE"]
            )

            patient_id = PatientService.register_patient(
                patient_name,
                gender,
                dob,
                phone,
                address,
                city,
                blood_group,
                occupation,
                marital_status,
                allergies,
                emergency_contact_name,
                emergency_phone,
                registration_date,
                patient_status
            )

            print("\n==========================================")
            print("    PATIENT REGISTERED SUCCESSFULLY")
            print("==========================================")

            print(
                "PATIENT ID :",
                patient_id
            )

            print("==========================================")
        
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def search_patient():

        while True:

            print("\n==========================================")
            print("          SEARCH PATIENT")
            print("==========================================")

            print("1. SEARCH BY PATIENT ID")
            print("2. SEARCH BY PHONE NUMBER")
            print("3. BACK")

            

            try:
                
                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

                if choice == "1":

                    patient = (
                        PatientService.search_patient_by_id(
                            InputHelper.get_input(
                                "ENTER PATIENT ID: "
                            ).strip().upper()
                        )
                    )

                elif choice == "2":

                    patient = (
                        PatientService.search_patient_by_phone(
                            InputHelper.get_input(
                                "ENTER PHONE NUMBER: "
                            )
                        )
                    )

                elif choice == "3":

                    return

                else:

                    print(
                        "INVALID CHOICE"
                    )

                    continue

                if not patient:

                    print("\n==========================================")
                    print("        PATIENT NOT FOUND")
                    print("==========================================")

                    continue

                print("\n==========================================")
                print("          PATIENT DETAILS")
                print("==========================================")

                print(
                    "PATIENT ID        :",
                    patient.patient_id
                )

                print(
                    "NAME              :",
                    patient.patient_name
                )

                print(
                    "GENDER            :",
                    patient.gender
                )

                print(
                    "DATE OF BIRTH     :",
                    patient.dob
                )

                print(
                    "PHONE             :",
                    patient.phone
                )

                print(
                    "ADDRESS           :",
                    patient.address
                )

                print(
                    "CITY              :",
                    patient.city
                )

                print(
                    "BLOOD GROUP       :",
                    patient.blood_group
                )

                print(
                    "OCCUPATION        :",
                    patient.occupation
                )

                print(
                    "MARITAL STATUS    :",
                    patient.marital_status
                )

                print(
                    "ALLERGIES         :",
                    patient.allergies
                )

                print(
                    "EMERGENCY CONTACT :",
                    patient.emergency_contact_name
                )

                print(
                    "EMERGENCY PHONE   :",
                    patient.emergency_phone
                )

                print(
                    "REGISTERED ON     :",
                    patient.registration_date
                )

                print(
                    "STATUS            :",
                    patient.patient_status
                )

                print("==========================================")

            except OperationCancelled as e:

                print(e)

            except Exception as e:

                print(
                    "ERROR:",
                    e
                )
            
    @staticmethod
    def view_all_patients():

        try:

            patients = PatientService.view_all_patients()

            if not patients:

                print("\n==========================================")
                print("            PATIENT LIST")
                print("==========================================")
                print("NO PATIENTS FOUND")

                return

            print("\n===============================================================================")
            print("                               PATIENT LIST")
            print("===============================================================================")

            print(
                f"{'ID':<8}"
                f"{'NAME':<30}"
                f"{'PHONE':<15}"
                f"{'BLOOD GROUP':<15}"
                f"{'STATUS':<10}"
            )

            print(TABLE_LINE)

            for patient in patients:

                print(
                    f"{patient.patient_id:<8}"
                    f"{patient.patient_name:<30}"
                    f"{patient.phone:<15}"
                    f"{patient.blood_group:<15}"
                    f"{patient.patient_status:<10}"
                )

            print(TABLE_LINE)

            print(
                f"TOTAL RECORDS : {len(patients)}"
            )

        except Exception as e:

            print(
                "ERROR:",
                e
            )

    @staticmethod
    def update_patient():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            patient_id = InputHelper.get_input(
                "ENTER PATIENT ID: "
            ).strip().upper()

            patient = PatientService.search_patient_by_id(
                patient_id
            )

            if not patient:
                print("\n==========================================")
                print("        PATIENT NOT FOUND")
                print("==========================================")
                return

            patient_name = InputHelper.get_update_input(
                "ENTER PATIENT NAME",
                patient.patient_name
            )

            phone = InputHelper.get_update_input(
                "ENTER PHONE",
                patient.phone
            )

            address = InputHelper.get_update_input(
                "ENTER ADDRESS",
                patient.address
            )

            city = InputHelper.get_update_input(
                "ENTER CITY",
                patient.city
            )

            occupation = InputHelper.get_update_input(
                "ENTER OCCUPATION",
                patient.occupation
            )

            marital_status = InputHelper.get_update_input(
                "ENTER MARITAL STATUS",
                patient.marital_status
            )

            allergies = InputHelper.get_update_input(
                "ENTER ALLERGIES",
                patient.allergies
            )

            emergency_contact_name = InputHelper.get_update_input(
                "ENTER EMERGENCY CONTACT NAME",
                patient.emergency_contact_name
            )

            emergency_phone = InputHelper.get_update_input(
                "ENTER EMERGENCY PHONE",
                patient.emergency_phone
            )

            patient_status = InputHelper.get_update_choice(
                "ENTER STATUS",
                patient.patient_status,
                ["ACTIVE", "INACTIVE"]
            )

            PatientService.update_patient(
                patient_id,
                patient_name,
                phone,
                address,
                city,
                occupation,
                marital_status,
                allergies,
                emergency_contact_name,
                emergency_phone,
                patient_status
            )

            print("\n==========================================")
            print("      PATIENT UPDATED SUCCESSFULLY")
            print("==========================================")

            print(
                "PATIENT ID :",
                patient_id
            )

            print(
                "NAME       :",
                patient_name
            )

            print("==========================================")
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def delete_patient():

        try:
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )
            patient_id = InputHelper.get_input(
                "ENTER PATIENT ID: "
            ).strip().upper()

            
            
            confirm = InputHelper.get_confirmation(
                "CONFIRM PATIENT DEACTIVATION (Y/N): "
            )

            if confirm == "N":

                print(
                    "DELETE OPERATION CANCELLED"
                )

                return
            PatientService.delete_patient(
                patient_id
            )

            print("\n==========================================")
            print("   PATIENT STATUS UPDATED SUCCESSFULLY")
            print("==========================================")

            print(
                "PATIENT ID :",
                patient_id
            )

            print(
                "NEW STATUS : INACTIVE"
            )

            print("==========================================")
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def show():

        while True:

            print("\n==========================================")
            print("         PATIENT MANAGEMENT")
            print("==========================================")
            print("1. REGISTER PATIENT")
            print("2. SEARCH PATIENT")
            print("3. VIEW ALL PATIENTS")
            print("4. UPDATE PATIENT")
            print("5. DELETE PATIENT")
            print("6. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

            except OperationCancelled as e:

                print(e)

                break

            if choice == "1":
                PatientMenu.register_patient()

            elif choice == "2":
                PatientMenu.search_patient()
                
            elif choice == "3":
                PatientMenu.view_all_patients()

            elif choice == "4":
                PatientMenu.update_patient()

            elif choice == "5":
                PatientMenu.delete_patient()

            elif choice == "6":
                break

            else:
                print("INVALID CHOICE")