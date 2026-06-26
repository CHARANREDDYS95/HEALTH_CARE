from services.billing_service import BillingService
from utils.input_helper import (InputHelper,OperationCancelled)

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

                    bill = (
                        BillingService.search_bill_by_consultation(
                            InputHelper.get_input(
                                "ENTER CONSULTATION ID: "
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

            print("\n==========================================")
            print("            ALL BILLS")
            print("==========================================")

            for bill in bills:

                print("------------------------------------------")

                print(
                    "BILL ID         :",
                    bill.bill_id
                )

                print(
                    "CONSULTATION ID :",
                    bill.consultation_id
                )

                print(
                    "TOTAL AMOUNT    :",
                    bill.total_amount
                )

                print(
                    "STATUS          :",
                    bill.bill_status
                )

        except Exception as e:
            print("ERROR:", e)
    
    @staticmethod
    def generate_bill():

        try:
            
            print("\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION")
            
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