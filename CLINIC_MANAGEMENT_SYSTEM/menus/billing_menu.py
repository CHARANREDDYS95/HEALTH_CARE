from services.billing_service import BillingService
from utils.input_helper import (InputHelper,OperationCancelled)

class BillingMenu:
          
    @staticmethod
    def search_bill():

        try:
            print(
                "\nTYPE 'CANCEL' AT ANY TIME TO STOP THE OPERATION"
            )

            bill_id = InputHelper.get_input(
                "ENTER BILL ID: "
            ).strip().upper()

            bill = (
                BillingService.search_bill(
                    bill_id
                )
            )

            if not bill:

                print(
                    "BILL NOT FOUND"
                )

                return

            print(
                "\n===== BILL DETAILS ====="
            )

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

            return
        except Exception as e:
            print("ERROR:", e)
            
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

            print(
                "\n===== ALL BILLS ====="
            )

            for bill in bills:

                print(
                    bill.bill_id,
                    "|",
                    bill.consultation_id,
                    "|",
                    bill.total_amount,
                    "|",
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

            discount_amount = float(
                InputHelper.get_input(
                    "ENTER DISCOUNT AMOUNT: "
                )
            )

            tax_amount = float(
                InputHelper.get_input(
                    "ENTER TAX AMOUNT: "
                )
            )

            bill_id = (
                BillingService.generate_bill(
                    consultation_id,
                    discount_amount,
                    tax_amount
                )
            )

            print(
                f"BILL GENERATED SUCCESSFULLY. ID: {bill_id}"
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

            BillingService.process_payment(
                bill_id
            )

            print(
                "PAYMENT PROCESSED SUCCESSFULLY"
            )
        except OperationCancelled as e:

            print(e)

            return
        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def show():

        while True:

            print(
                "\n===== BILLING & PAYMENT MANAGEMENT ====="
            )
            print("1. GENERATE BILL")
            print("2. SEARCH BILL")
            print("3. PROCESS PAYMENT")
            print("4. VIEW ALL BILLS")
            print("5. BACK")

            choice = input("ENTER CHOICE: ")

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