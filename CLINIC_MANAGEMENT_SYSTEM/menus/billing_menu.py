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
    def view_all_bills():

        try:
            

            bills = (
                BillingService.get_all_bills()
            )

            if not bills:

                print(
                    "NO BILLS FOUND"
                )

                return

            print("\n========================================================================================================")
            print("                                           ALL BILLS")
            print("========================================================================================================")

            print(

                f"{'BILL ID':<12}"
                f"{'CONSULT ID':<15}"
                f"{'CONSULT FEE':<15}"
                f"{'DISCOUNT':<12}"
                f"{'TAX':<10}"
                f"{'TOTAL':<12}"
                f"{'STATUS':<15}"

            )

            print(

                "=" * 95

            )

            for bill in bills:

                print(

                    f"{bill.bill_id:<12}"
                    f"{bill.consultation_id:<15}"
                    f"{bill.consultation_fee:<15.2f}"
                    f"{bill.discount_amount:<12.2f}"
                    f"{bill.tax_amount:<10.2f}"
                    f"{bill.total_amount:<12.2f}"
                    f"{bill.bill_status:<15}"

                )

            print(

                "=" * 95

            )

        except Exception as e:
            print("ERROR:", e)
    
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

            tax_amount = InputHelper.get_float(
                "ENTER TAX AMOUNT: "
            )

            bill_id = (
                BillingService.generate_bill(
                    consultation_id,
                    discount_amount,
                    tax_amount
                )
            )

            print("\n==========================================")
            print("BILL GENERATED SUCCESSFULLY")
            print("==========================================")
            print(
                "BILL ID :",
                bill_id
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

            pending_bills = [

                bill

                for bill in bills

                if bill.bill_status
                == "PENDING"

            ]

            if not pending_bills:

                print(

                    "NO PENDING BILLS FOUND"

                )

                return

            print("\n====================================================================================================")
            print("                                         PENDING BILLS")
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

            for bill in pending_bills:

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
            
            payment_mode = InputHelper.get_choice(
                "ENTER PAYMENT MODE (CASH/UPI/CARD): ",
                ["CASH", "UPI", "CARD"]
            )

            transaction_reference = None

            if payment_mode != "CASH":

                transaction_reference = InputHelper.get_input(
                    "ENTER TRANSACTION REFERENCE: "
                )
            confirm = InputHelper.get_confirmation(
                "CONFIRM PAYMENT (Y/N): "
            )

            if confirm == "N":

                print(
                    "PAYMENT CANCELLED"
                )

                return
            payment_id = (
                BillingService.process_payment(
                    bill_id,
                    payment_mode,
                    transaction_reference
                )
            )

            print("\n==========================================")
            print("PAYMENT PROCESSED SUCCESSFULLY")
            print("==========================================")
            print(
                "PAYMENT ID :",
                payment_id
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
            print("4. VIEW ALL BILLS")
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
                BillingMenu.view_all_bills()

            elif choice == "5":
                break

            else:
                print("INVALID CHOICE")