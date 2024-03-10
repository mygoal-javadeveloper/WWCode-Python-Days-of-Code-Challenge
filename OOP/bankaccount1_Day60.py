# Create a class representing a simple bank account with deposit and withdraw methods

class Banking:
    def __init__(self, customer_id, account_bal, required_bal = 10000):
        self.customer_id = customer_id
        self.account_bal = account_bal
        self.required_bal = required_bal

    def deposit_amt(self, deposit_amt):
        self.account_bal = self.account_bal + deposit_amt
        print(f"Account balance updated successfully by adding the deposited amount Rs {deposit_amt}.")

    def withdraw_amt(self, withdraw_amt):
        if self.account_bal < withdraw_amt or self.account_bal - withdraw_amt < self.required_bal:
            print(f"Account balance not sufficient for the required withdrawal amount Rs {withdraw_amt} to be carried out.")
        else:
            self.account_bal = self.account_bal - withdraw_amt
            print(f"Account Balance updated Successfully by subtracting the withdrawal amount Rs {withdraw_amt}.")

    def print_accountdetails(self):
        print(f"Customer ID: {self.customer_id} \nTotal balance amount: Rs {self.account_bal}")



if __name__ == "__main__":
    # customer wants to deposit amount in his bank account.
    bank_obj1 = Banking(1001, 10000)
    bank_obj1.print_accountdetails()
    bank_obj1.deposit_amt(8000)
    bank_obj1.print_accountdetails()
    print()
    # customer wants to withdraw amount from his bank account.
    bank_obj2 = Banking(1001, 18000)
    bank_obj2.print_accountdetails()
    bank_obj2.withdraw_amt(800)
    bank_obj2.print_accountdetails()
    print()
    # customer wants to withdraw amount from his bank account.
    bank_obj3 = Banking(1001, 17200)
    bank_obj3.print_accountdetails()
    bank_obj3.withdraw_amt(8000)
    bank_obj3.print_accountdetails()