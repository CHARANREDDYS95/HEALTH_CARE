from services.doctor_service import DoctorService
from utils.input_helper import (InputHelper,OperationCancelled)
from utils.display_constants import (

    TABLE_LINE
)
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

            gender = InputHelper.get_choice(
                "ENTER GENDER (M/F/O): ",
                ["M", "F", "O"]
            )

            dob = InputHelper.get_date(
                "ENTER DOB (YYYY-MM-DD): "
            )

            specialization = InputHelper.get_input(
                "ENTER SPECIALIZATION: "
            )

            qualification = InputHelper.get_input(
                "ENTER QUALIFICATION: "
            )

            license_no = InputHelper.get_input(
                "ENTER LICENSE NUMBER: "
            )

            experience_years = InputHelper.get_integer(
                "ENTER EXPERIENCE YEARS: "
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

            consultation_fee = InputHelper.get_float(
                "ENTER CONSULTATION FEE: "
            )

            doctor_status = InputHelper.get_choice(
                "ENTER STATUS (ACTIVE/INACTIVE): ",
                ["ACTIVE", "INACTIVE"]
            )

            joining_date = InputHelper.get_date(
                "ENTER JOINING DATE (YYYY-MM-DD): "
            )

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
                doctor_status,
                joining_date
            )
            
            print("\n==========================================")
            print("      DOCTOR ADDED SUCCESSFULLY")
            print("==========================================")

            print(
                "DOCTOR ID :",
                doctor_id
            )

            print("==========================================")
            
        except OperationCancelled as e:

            print(e)

            return

        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def search_doctor():

        while True:

            print("\n==========================================")
            print("           SEARCH DOCTOR")
            print("==========================================")

            print("1. SEARCH BY DOCTOR ID")
            print("2. SEARCH BY PHONE NUMBER")
            print("3. SEARCH BY LICENSE NUMBER")
            print("4. BACK")

            

            try:
                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

                if choice == "1":

                    doctor = (
                        DoctorService.search_doctor_by_id(
                            InputHelper.get_input(
                                "ENTER DOCTOR ID: "
                            ).strip().upper()
                        )
                    )

                elif choice == "2":

                    doctor = (
                        DoctorService.search_doctor_by_phone(
                            InputHelper.get_input(
                                "ENTER PHONE NUMBER: "
                            )
                        )
                    )

                elif choice == "3":

                    doctor = (
                        DoctorService.search_doctor_by_license(
                            InputHelper.get_input(
                                "ENTER LICENSE NUMBER: "
                            ).strip().upper()
                        )
                    )

                elif choice == "4":

                    return

                else:

                    print(
                        "INVALID CHOICE"
                    )

                    continue

                if not doctor:

                    print(
                        "DOCTOR NOT FOUND"
                    )

                    continue

                print("\n==========================================")
                print("           DOCTOR DETAILS")
                print("==========================================")

                print(
                    "DOCTOR ID       :",
                    doctor.doctor_id
                )

                print(
                    "NAME            :",
                    doctor.doctor_name
                )

                print(
                    "GENDER          :",
                    doctor.gender
                )

                print(
                    "DATE OF BIRTH   :",
                    doctor.dob
                )

                print(
                    "SPECIALIZATION  :",
                    doctor.specialization
                )

                print(
                    "QUALIFICATION   :",
                    doctor.qualification
                )

                print(
                    "LICENSE NUMBER  :",
                    doctor.license_no
                )

                print(
                    "EXPERIENCE      :",
                    f"{doctor.experience_years} Years"
                )

                print(
                    "PHONE           :",
                    doctor.phone
                )

                print(
                    "EMAIL           :",
                    doctor.email
                )

                print(
                    "ADDRESS         :",
                    doctor.address
                )

                print(
                    "CONSULTATION FEE:",
                    doctor.consultation_fee
                )

                print(
                    "JOINING DATE    :",
                    doctor.joining_date
                )

                print(
                    "STATUS          :",
                    doctor.doctor_status
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
    def view_all_doctors():

        try:

            doctors = DoctorService.view_all_doctors()

            if not doctors:

                print("\n==========================================")
                print("            DOCTOR LIST")
                print("==========================================")
                print("NO DOCTORS FOUND")

                return

            print("\n===============================================================================")
            print("                                DOCTOR LIST")
            print("===============================================================================")

            print(
                f"{'ID':<8}"
                f"{'NAME':<30}"
                f"{'SPECIALIZATION':<25}"
                f"{'PHONE':<15}"
                f"{'STATUS':<10}"
            )

            print(TABLE_LINE)

            for doctor in doctors:

                print(
                    f"{doctor.doctor_id:<8}"
                    f"{doctor.doctor_name:<30}"
                    f"{doctor.specialization:<25}"
                    f"{doctor.phone:<15}"
                    f"{doctor.doctor_status:<10}"
                )

            print(TABLE_LINE)

            print(
                f"TOTAL RECORDS : {len(doctors)}"
            )

        except Exception as e:

            print(
                "ERROR:",
                e
            )

    @staticmethod
    def update_doctor():

        try:
            
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            doctor_id = InputHelper.get_input(
                "ENTER DOCTOR ID: "
            ).strip().upper()

            doctor = DoctorService.search_doctor_by_id(
                doctor_id
            )

            if not doctor:
                print("\n==========================================")
                print("        DOCTOR NOT FOUND")
                print("==========================================")
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

            consultation_fee = InputHelper.get_update_float(
                "ENTER CONSULTATION FEE",
                doctor.consultation_fee
            )

            DoctorService.update_doctor(
                doctor_id,
                doctor_name,
                phone,
                email,
                address,
                consultation_fee

            )

            print("\n==========================================")
            print("     DOCTOR UPDATED SUCCESSFULLY")
            print("==========================================")

            print(
                "DOCTOR ID :",
                doctor_id
            )

            print(
                "NAME      :",
                doctor_name
            )

            print("==========================================")
        
        except OperationCancelled as e:

            print(e)

            return
        
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def change_doctor_status():

        try:

            print("\n==========================================")
            print("        CHANGE DOCTOR STATUS")
            print("==========================================")
            print("Type 'cancel' at any time to stop the operation.\n")

            doctor_id = InputHelper.get_input(
                "ENTER DOCTOR ID: "
            ).strip().upper()

            doctor = DoctorService.search_doctor_by_id(
                doctor_id
            )

            if not doctor:

                print("\n==========================================")
                print("        DOCTOR NOT FOUND")
                print("==========================================")
                return

            print("\n==========================================")
            print("        CURRENT DOCTOR DETAILS")
            print("==========================================")

            print("DOCTOR ID      :", doctor.doctor_id)
            print("DOCTOR NAME    :", doctor.doctor_name)
            print("CURRENT STATUS :", doctor.doctor_status)
            
            print("\nSELECT NEW STATUS")

            new_status = InputHelper.get_status_choice(
                doctor.doctor_status
            )

            if new_status == doctor.doctor_status:

                print(
                    f"\nDOCTOR IS ALREADY {doctor.doctor_status}"
                )
                return

            confirm = InputHelper.get_confirmation(
                "CONFIRM STATUS CHANGE (Y/N): "
            )

            if confirm == "N":

                print("STATUS CHANGE CANCELLED")
                return

            DoctorService.change_doctor_status(
                doctor_id,
                new_status
            )

            print("\n==========================================")
            print("DOCTOR STATUS UPDATED SUCCESSFULLY")
            print("==========================================")

            print("DOCTOR ID      :", doctor.doctor_id)
            print("DOCTOR NAME    :", doctor.doctor_name)
            print("OLD STATUS     :", doctor.doctor_status)
            print("NEW STATUS     :", new_status)

        except OperationCancelled as e:

            print(e)
            return

        except Exception as e:

            print("ERROR:", e)

    @staticmethod
    def show():

        while True:

            print("\n==========================================")
            print("         DOCTOR MANAGEMENT")
            print("==========================================")
            print("1. ADD DOCTOR")
            print("2. SEARCH DOCTOR")
            print("3. VIEW ALL DOCTORS")
            print("4. UPDATE DOCTOR")
            print("5. CHANGE DOCTOR STATUS")
            print("6. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

            except OperationCancelled as e:

                print(e)

                break

            if choice == "1":
                DoctorMenu.add_doctor()

            elif choice == "2":
                DoctorMenu.search_doctor()

            elif choice == "3":
                DoctorMenu.view_all_doctors()

            elif choice == "4":
                DoctorMenu.update_doctor()

            elif choice == "5":
                DoctorMenu.change_doctor_status()

            elif choice == "6":
                break

            else:
                print("INVALID CHOICE")