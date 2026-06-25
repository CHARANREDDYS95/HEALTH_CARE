from datetime import datetime
from services.patient_service import PatientService
from utils.input_helper import (InputHelper,OperationCancelled)


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

            gender = InputHelper.get_input(
                "ENTER GENDER (M/F/O): "
            ).strip().upper()

            dob = datetime.strptime(
                InputHelper.get_input(
                    "ENTER DOB (YYYY-MM-DD): "
                ),
                "%Y-%m-%d"
            ).date()

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

            registration_date = datetime.strptime(
                InputHelper.get_input(
                    "ENTER REGISTRATION DATE (YYYY-MM-DD): "
                ),
                "%Y-%m-%d"
            ).date()

            patient_status = InputHelper.get_input(
                "ENTER STATUS (ACTIVE/INACTIVE): "
            ).strip().upper()

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

            print(
                f"PATIENT REGISTERED SUCCESSFULLY. ID: {patient_id}"
            )
        
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def search_patient():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            search_value = InputHelper.get_input(
                "ENTER PATIENT ID OR PHONE NUMBER: "
            ).strip().upper()

            patient = PatientService.search_patient(
                search_value
            )

            if patient:

                print("\n===== PATIENT DETAILS =====")
                print("PATIENT ID :", patient.patient_id)
                print("PATIENT NAME :", patient.patient_name)
                print("GENDER :", patient.gender)
                print("PHONE :", patient.phone)
                print("CITY :", patient.city)
                print("BLOOD GROUP :", patient.blood_group)
                print("STATUS :", patient.patient_status)

            else:
                print("PATIENT NOT FOUND")
        
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)
            
    @staticmethod
    def view_all_patients():

        try:

            patients = PatientService.view_all_patients()

            if not patients:
                print("NO PATIENTS FOUND")
                return

            print("\n===== PATIENT LIST =====")
            
            for patient in patients:

                print(
                    f"{patient.patient_id} | "
                    f"{patient.patient_name} | "
                    f"{patient.phone} | "
                    f"{patient.blood_group} | "
                    f"{patient.patient_status}"
                )

        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def update_patient():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            patient_id = InputHelper.get_input(
                "ENTER PATIENT ID: "
            ).strip().upper()

            patient = PatientService.search_patient(
                patient_id
            )

            if not patient:
                print("PATIENT NOT FOUND")
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

            patient_status = InputHelper.get_update_input(
                "ENTER STATUS",
                patient.patient_status
            ).upper()

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

            print("PATIENT UPDATED SUCCESSFULLY")
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

            PatientService.delete_patient(
                patient_id
            )

            print(
                "PATIENT STATUS CHANGED TO INACTIVE"
            )
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def show():

        while True:

            print("\n===== PATIENT MANAGEMENT =====")
            print("1. REGISTER PATIENT")
            print("2. SEARCH PATIENT")
            print("3. VIEW ALL PATIENTS")
            print("4. UPDATE PATIENT")
            print("5. DELETE PATIENT")
            print("6. BACK")

            choice = input("ENTER CHOICE: ")

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