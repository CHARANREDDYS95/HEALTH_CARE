from datetime import datetime
from services.doctor_service import DoctorService
from utils.input_helper import (InputHelper,OperationCancelled)

class DoctorMenu:

    @staticmethod
    def add_doctor():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )
            
            doctor_name = InputHelper.get_input(
                "ENTER DOCTOR NAME: "
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

            specialization = InputHelper.get_input(
                "ENTER SPECIALIZATION: "
            )

            qualification = InputHelper.get_input(
                "ENTER QUALIFICATION: "
            )

            license_no = InputHelper.get_input(
                "ENTER LICENSE NUMBER: "
            )

            experience_years = int(
                InputHelper.get_input(
                    "ENTER EXPERIENCE YEARS: "
                )
            )

            phone = InputHelper.get_input(
                "ENTER PHONE NUMBER: "
            )

            email = InputHelper.get_input(
                "ENTER EMAIL: "
            )

            address = InputHelper.get_input(
                "ENTER ADDRESS: "
            )

            consultation_fee = float(
                InputHelper.get_input(
                    "ENTER CONSULTATION FEE: "
                )
            )

            consultation_duration = int(
                InputHelper.get_input(
                    "ENTER CONSULTATION DURATION: "
                )
            )

            doctor_status = InputHelper.get_input(
                "ENTER STATUS (ACTIVE/INACTIVE): "
            ).strip().upper()

            joining_date = datetime.strptime(
                InputHelper.get_input(
                    "ENTER JOINING DATE (YYYY-MM-DD): "
                ),
                "%Y-%m-%d"
            ).date()

            doctor_id = DoctorService.add_doctor(
                doctor_name,
                gender,
                dob,
                specialization,
                qualification,
                license_no,
                experience_years,
                phone,
                email,
                address,
                consultation_fee,
                consultation_duration,
                doctor_status,
                joining_date
            )

            print(
                f"DOCTOR ADDED SUCCESSFULLY. ID: {doctor_id}"
            )
            
        except OperationCancelled as e:

            print(e)

            return

        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def search_doctor():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            doctor_id = InputHelper.get_input(
                "ENTER DOCTOR ID: "
            ).strip().upper()

            doctor = DoctorService.search_doctor(
                doctor_id
            )

            if doctor:

                print("\n===== DOCTOR DETAILS =====")
                print("DOCTOR ID :", doctor.doctor_id)
                print("DOCTOR NAME :", doctor.doctor_name)
                print("GENDER :", doctor.gender)
                print("PHONE :", doctor.phone)
                print("EMAIL :", doctor.email)
                print("SPECIALIZATION :", doctor.specialization)
                print("STATUS :", doctor.doctor_status)

            else:
                print("DOCTOR NOT FOUND")
        
        except OperationCancelled as e:

            print(e)

            return
        
        except Exception as e:
            print("ERROR:", e)
            
    @staticmethod
    def view_all_doctors():

        try:

            doctors = DoctorService.view_all_doctors()

            if not doctors:
                print("NO DOCTORS FOUND")
                return

            print("\n===== DOCTOR LIST =====")
            
            for doctor in doctors:

                print(
                    doctor.doctor_id,
                    doctor.doctor_name,
                    doctor.specialization,
                    doctor.phone,
                    doctor.doctor_status
                )

        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def update_doctor():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            doctor_id = InputHelper.get_input(
                "ENTER DOCTOR ID: "
            ).strip().upper()

            doctor = DoctorService.search_doctor(
                doctor_id
            )

            if not doctor:
                print("DOCTOR NOT FOUND")
                return

            doctor_name = InputHelper.get_update_input(
                "ENTER DOCTOR NAME",
                doctor.doctor_name
            )

            phone = InputHelper.get_update_input(
                "ENTER PHONE",
                doctor.phone
            )

            email = InputHelper.get_update_input(
                "ENTER EMAIL",
                doctor.email
            )

            address = InputHelper.get_update_input(
                "ENTER ADDRESS",
                doctor.address
            )

            consultation_fee = float(
                InputHelper.get_update_input(
                    "ENTER CONSULTATION FEE",
                    doctor.consultation_fee
                )
            )

            consultation_duration = int(
                InputHelper.get_update_input(
                    "ENTER CONSULTATION DURATION",
                    doctor.consultation_duration
                )
            )

            doctor_status = InputHelper.get_update_input(
                "ENTER STATUS",
                doctor.doctor_status
            ).upper()

            DoctorService.update_doctor(
                doctor_id,
                doctor_name,
                phone,
                email,
                address,
                consultation_fee,
                consultation_duration,
                doctor_status
            )

            print("DOCTOR UPDATED SUCCESSFULLY")
        
        except OperationCancelled as e:

            print(e)

            return
        
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def delete_doctor():

        try:

            doctor_id = InputHelper.get_input(
                "ENTER DOCTOR ID: "
            ).strip().upper()

            DoctorService.delete_doctor(
                doctor_id
            )

            print(
                "DOCTOR STATUS CHANGED TO INACTIVE"
            )
        
        except OperationCancelled as e:

            print(e)

            return
        
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def show():

        while True:

            print("\n===== DOCTOR MANAGEMENT =====")
            print("1. ADD DOCTOR")
            print("2. SEARCH DOCTOR")
            print("3. VIEW ALL DOCTORS")
            print("4. UPDATE DOCTOR")
            print("5. DELETE DOCTOR")
            print("6. BACK")

            choice = input("ENTER CHOICE: ")

            if choice == "1":
                DoctorMenu.add_doctor()

            elif choice == "2":
                DoctorMenu.search_doctor()
                
            elif choice == "3":
                DoctorMenu.view_all_doctors()

            elif choice == "4":
                DoctorMenu.update_doctor()

            elif choice == "5":
                DoctorMenu.delete_doctor()

            elif choice == "6":
                break

            else:
                print("INVALID CHOICE")