from services.billing_service import BillingService
from utils.input_helper import (InputHelper,OperationCancelled)
from services.consultation_service import (
    ConsultationService
)

class BillingMenu:
          
    @staticmethod
    def search_bill():

        while True:

            print("\n==========================================")
            print("           SEARCH BILL")
            print("==========================================")

            print("1. SEARCH BY BILL ID")
            print("2. SEARCH BY CONSULTATION ID")
            print("3. BACK")

            

            try:
                
                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

                if choice == "1":

                    bill = (
                        BillingService.search_bill_by_id(
                            InputHelper.get_input(
                                "ENTER BILL ID: "
                            ).strip().upper()
                        )
                    )

                elif choice == "2":

                    consultations = (

                        ConsultationService.get_all_consultations()

                    )

                    completed_consultations = [

                        consultation

                        for consultation in consultations

                        if consultation.consultation_status
                        == "COMPLETED"

                    ]

                    if not completed_consultations:

                        print(

                            "NO COMPLETED CONSULTATIONS FOUND"

                        )

                        continue

                    print("\n====================================================================================================")
                    print("                                   COMPLETED CONSULTATIONS")
                    print("====================================================================================================")

                    print(

                        f"{'CONSULT ID':<15}"
                        f"{'APP ID':<12}"
                        f"{'DIAGNOSIS':<30}"

                    )

                    print(

                        "=" * 60

                    )

                    for consultation in completed_consultations:

                        print(

                            f"{consultation.consultation_id:<15}"
                            f"{consultation.appointment_id:<12}"
                            f"{str(consultation.diagnosis):<30}"

                        )

                    print(

                        "=" * 60

                    )

                    consultation_id = InputHelper.get_input(

                        "\nENTER CONSULTATION ID: "

                    ).strip().upper()

                    bill = (

                        BillingService.search_bill_by_consultation(

                            consultation_id

                        )

                    )

                elif choice == "3":
                    
                    return

                else:

                    print(
                        "INVALID CHOICE"
                    )

                    continue

                if not bill:

                    print(
                        "BILL NOT FOUND"
                    )

                    continue

                print("\n==========================================")
                print("            BILL DETAILS")
                print("==========================================")

                print(
                    "BILL ID :",
                    bill.bill_id
                )

                print(
                    "CONSULTATION ID :",
                    bill.consultation_id
                )

                print(
                    "CONSULTATION FEE :",
                    bill.consultation_fee
                )

                print(
                    "DISCOUNT :",
                    bill.discount_amount
                )

                print(
                    "TAX :",
                    bill.tax_amount
                )

                print(
                    "TOTAL AMOUNT :",
                    bill.total_amount
                )

                print(
                    "BILL DATE :",
                    bill.bill_date
                )

                print(
                    "STATUS :",
                    bill.bill_status
                )

            except OperationCancelled as e:

                print(e)

            except Exception as e:

                print("ERROR:",e)

    @staticmethod
    def display_bills(
        bills,
        title
    ):

        if not bills:

            print(
                f"NO {title.upper()} FOUND"
            )

            return

        print("\n====================================================================================================")
        print(
            f"{title.center(100)}"
        )
        print("====================================================================================================")

        print(

            f"{'BILL ID':<12}"
            f"{'CONSULT ID':<15}"
            f"{'TOTAL':<15}"
            f"{'STATUS':<15}"

        )

        print(

            "=" * 60

        )

        for bill in bills:

            print(

                f"{bill.bill_id:<12}"
                f"{bill.consultation_id:<15}"
                f"{bill.total_amount:<15.2f}"
                f"{bill.bill_status:<15}"

            )

        print(

            "=" * 60

        )

    @staticmethod
    def view_all_bills():

        try:

            bills = (

                BillingService.get_all_bills()

            )

            BillingMenu.display_bills(

                bills,

                "ALL BILLS"

            )

        except Exception as e:

            print(

                "ERROR:",

                e

            )
            
    @staticmethod
    def view_unpaid_bills():

        try:

            bills = (

                BillingService.get_all_bills()

            )

            unpaid_bills = [

                bill

                for bill in bills

                if bill.bill_status
                == "UNPAID"

            ]

            BillingMenu.display_bills(

                unpaid_bills,

                "UNPAID BILLS"

            )

        except Exception as e:

            print(

                "ERROR:",

                e

            )
    
    @staticmethod
    def view_paid_bills():

        try:

            bills = (

                BillingService.get_all_bills()

            )

            paid_bills = [

                bill

                for bill in bills

                if bill.bill_status
                == "PAID"

            ]

            BillingMenu.display_bills(

                paid_bills,

                "PAID BILLS"

            )

        except Exception as e:

            print(

                "ERROR:",

                e

            )
    
    @staticmethod
    def generate_bill():

        try:
            
            print("\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION")
            
            consultations = (

                ConsultationService.get_all_consultations()

            )

            completed_consultations = [

                consultation

                for consultation in consultations

                if consultation.consultation_status
                == "COMPLETED"

            ]

            if not completed_consultations:

                print(

                    "NO COMPLETED CONSULTATIONS FOUND"

                )

                return

            print("\n====================================================================================================")
            print("                                   COMPLETED CONSULTATIONS")
            print("====================================================================================================")

            print(

                f"{'CONSULT ID':<15}"
                f"{'APP ID':<12}"
                f"{'STATUS':<20}"

            )

            print(

                "=" * 50

            )

            for consultation in completed_consultations:

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

            discount_amount = InputHelper.get_float(
                "ENTER DISCOUNT AMOUNT: "
            )

            bill_details = (
                BillingService.calculate_bill(
                    consultation_id,
                    discount_amount
                )
            )

            print(
                "\n============================================================"
            )

            print(
                "                    BILL SUMMARY"
            )

            print(
                "============================================================"
            )

            print(
                f"Consultation ID  : {bill_details['consultation_id']}"
            )

            print(
                f"Appointment ID   : {bill_details['appointment_id']}"
            )

            print(
                f"Patient ID       : {bill_details['patient_id']}"
            )

            print(
                f"Patient Name     : {bill_details['patient_name']}"
            )

            print(
                f"Doctor Name      : {bill_details['doctor_name']}"
            )

            print()

            print(
                f"Consultation Fee : {bill_details['consultation_fee']:.2f}"
            )

            print(
                f"Discount         : {bill_details['discount_amount']:.2f}"
            )

            print(
                f"GST (18%)        : {bill_details['tax_amount']:.2f}"
            )

            print(
                "------------------------------------------------------------"
            )

            print(
                f"Total Amount     : {bill_details['total_amount']:.2f}"
            )

            print(
                "============================================================"
            )

            confirm = InputHelper.get_confirmation()

            if confirm != "Y":

                print()

                print(
                    "BILL GENERATION CANCELLED."
                )

                return

            bill_id = (
                BillingService.generate_bill(
                    consultation_id,
                    discount_amount
                )
            )

            print(
                "\n============================================================"
            )

            print(
                "            BILL GENERATED SUCCESSFULLY"
            )

            print(
                "============================================================"
            )

            print(
                f"Bill ID          : {bill_id}"
            )

            print(
                f"Consultation Fee : {bill_details['consultation_fee']:.2f}"
            )

            print(
                f"Discount         : {bill_details['discount_amount']:.2f}"
            )

            print(
                f"GST (18%)        : {bill_details['tax_amount']:.2f}"
            )

            print(
                f"Total Amount     : {bill_details['total_amount']:.2f}"
            )

            print(
                "============================================================"
            )

        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def process_payment():

        try:
            
            print("\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION")

            bills = (

                BillingService.get_all_bills()

            )

            unpaid_bills = [

                bill

                for bill in bills

                if bill.bill_status
                == "UNPAID"

            ]

            if not unpaid_bills:

                print(

                    "NO UNPAID BILLS FOUND"

                )

                return

            print("\n====================================================================================================")
            print("                                         UNPAID BILLS")
            print("====================================================================================================")
           
            print(

                f"{'BILL ID':<12}"
                f"{'CONSULT ID':<15}"
                f"{'TOTAL':<15}"
                f"{'STATUS':<15}"

            )

            print(

                "=" * 60

            )
            
            for bill in unpaid_bills:

                print(

                    f"{bill.bill_id:<12}"
                    f"{bill.consultation_id:<15}"
                    f"{bill.total_amount:<15.2f}"
                    f"{bill.bill_status:<15}"

                )

            print(

                "=" * 60

            )

            bill_id = InputHelper.get_input(
                "ENTER BILL ID: "
            ).strip().upper()

            bill = (

                BillingService.search_bill_by_id(

                    bill_id

                )

            )

            if not bill:

                print(

                    "BILL NOT FOUND"

                )

                return
            
            if bill.bill_status != "UNPAID":

                print(

                    "ONLY UNPAID BILLS CAN BE PAID"

                )

                return

            print(
                "\n============================================================"
            )

            print(
                "                     BILL DETAILS"
            )

            print(
                "============================================================"
            )

            print(
                "BILL ID           :",
                bill.bill_id
            )

            print(
                "CONSULTATION ID   :",
                bill.consultation_id
            )

            print(
                "CONSULTATION FEE  :",
                f"{bill.consultation_fee:.2f}"
            )

            print(
                "DISCOUNT          :",
                f"{bill.discount_amount:.2f}"
            )

            print(
                "GST (18%)         :",
                f"{bill.tax_amount:.2f}"
            )

            print(
                "TOTAL AMOUNT      :",
                f"{bill.total_amount:.2f}"
            )

            print(
                "STATUS            :",
                bill.bill_status
            )

            print(
                "============================================================"
            )
            
            print(
                "\n=========================================="
            )

            print(
                "            PAYMENT MODE"
            )

            print(
                "=========================================="
            )

            print(
                "1. CASH"
            )

            print(
                "2. UPI"
            )

            print(
                "3. CARD"
            )

            choice = InputHelper.get_input(
                "ENTER CHOICE: "
            )

            if choice == "1":

                payment_mode = "CASH"

            elif choice == "2":

                payment_mode = "UPI"

            elif choice == "3":

                payment_mode = "CARD"

            else:

                print(
                    "INVALID CHOICE"
                )

                return

            transaction_reference = None

            if payment_mode != "CASH":

                transaction_reference = InputHelper.get_input(
                    "ENTER TRANSACTION REFERENCE: "
                )

            print(
                "\n============================================================"
            )

            print(
                "                 CONFIRM PAYMENT"
            )

            print(
                "============================================================"
            )

            print(
                "BILL ID           :",
                bill.bill_id
            )

            print(
                "CONSULTATION ID   :",
                bill.consultation_id
            )

            print(
                "TOTAL AMOUNT      :",
                f"{bill.total_amount:.2f}"
            )

            print(
                "PAYMENT MODE      :",
                payment_mode
            )

            if payment_mode != "CASH":

                print(
                    "REFERENCE NO.     :",
                    transaction_reference
                )

            print(
                "============================================================"
            )

            confirm = InputHelper.get_confirmation()

            if confirm != "Y":

                print()

                print(
                    "PAYMENT CANCELLED."
                )

                return

            payment_id = (
                BillingService.process_payment(
                    bill_id,
                    payment_mode,
                    transaction_reference
                )
            )

            print(
                "\n============================================================"
            )

            print(
                "           PAYMENT PROCESSED SUCCESSFULLY"
            )

            print(
                "============================================================"
            )

            print(
                "PAYMENT ID        :",
                payment_id
            )

            print(
                "BILL ID           :",
                bill.bill_id
            )

            print(
                "CONSULTATION ID   :",
                bill.consultation_id
            )

            print(
                "PAYMENT MODE      :",
                payment_mode
            )

            if payment_mode != "CASH":

                print(
                    "REFERENCE NO.     :",
                    transaction_reference
                )

            print(
                "AMOUNT PAID       :",
                f"{bill.total_amount:.2f}"
            )

            print(
                "PAYMENT STATUS    : SUCCESS"
            )

            print(
                "BILL STATUS       : PAID"
            )

            print(
                "============================================================"
            )

        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def show():

        while True:

            print("\n==========================================")
            print("      BILLING MANAGEMENT")
            print("==========================================")
            print("1. GENERATE BILL")
            print("2. SEARCH BILL")
            print("3. PROCESS PAYMENT")
            print("4. VIEW BILLS")
            print("5. BACK")

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

            except OperationCancelled as e:

                print(e)
                
                break

            if choice == "1":
                BillingMenu.generate_bill()

            elif choice == "2":
                BillingMenu.search_bill()

            elif choice == "3":
                BillingMenu.process_payment()

            elif choice == "4":
                BillingMenu.view_bills()

            elif choice == "5":
                break

            else:
                print("INVALID CHOICE")
                

                
    @staticmethod
    def view_bills():

        while True:

            print(
                "\n=========================================="
            )

            print(
                "              VIEW BILLS"
            )

            print(
                "=========================================="
            )

            print(
                "1. VIEW ALL BILLS"
            )

            print(
                "2. VIEW UNPAID BILLS"
            )

            print(
                "3. VIEW PAID BILLS"
            )
            


            print(
                "4. BACK"
            )

            try:

                choice = InputHelper.get_input(
                    "ENTER CHOICE: "
                )

                if choice == "1":

                    BillingMenu.view_all_bills()

                elif choice == "2":

                    BillingMenu.view_unpaid_bills()

                elif choice == "3":

                    BillingMenu.view_paid_bills()
                    
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

                return