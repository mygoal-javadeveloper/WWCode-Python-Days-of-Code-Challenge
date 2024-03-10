# Create a class representing a simple bank account with deposit and withdraw methods

class Banking:
    def __init__(self, customer_id, required_bal = 10000):
        self.customer_id = customer_id
        self.required_bal = required_bal
        self.customer_data = self.customer_details()

    def customer_details(self):
        bankcustomer = {1001: {'name': 'XYZ', 'age': 21, 'total_balance': 10000},
                        1002: {'name': 'ABC', 'age': 33, 'total_balance': 20000}}
        return bankcustomer

    def deposit_amt(self, deposit_amt):
        self.customer_data[self.customer_id]['total_balance'] = self.customer_data[self.customer_id]['total_balance'] + deposit_amt
        print(f"Account balance updated successfully by adding the deposited amount Rs {deposit_amt}.")

    def withdraw_amt(self, withdraw_amt):
        if self.customer_data[self.customer_id]['total_balance'] < withdraw_amt or self.customer_data[self.customer_id]['total_balance'] - withdraw_amt < self.required_bal:
            print(f"Account balance not sufficient for the required withdrawal amount Rs {withdraw_amt} to be carried out.")
        else:
            self.customer_data[self.customer_id]['total_balance'] = self.customer_data[self.customer_id]['total_balance'] - withdraw_amt
            print(f"Account Balance updated Successfully by subtracting the withdrawal amount Rs {withdraw_amt}.")

    def print_accountdetails(self):
        print(f"Customer ID: {self.customer_id} \nCustomer name: {self.customer_data[self.customer_id]['name']} \nCustomer age: {self.customer_data[self.customer_id]['age']} \nTotal balance amount: Rs {self.customer_data[self.customer_id]['total_balance']}")



if __name__ == "__main__":
    # customer details only
    bank_obj1 = Banking(1001)
    print('The details of customer:')
    bank_obj1.print_accountdetails()
    print()

    # customer wants to deposit amount in his bank account.
    bank_obj1.deposit_amt(8000)
    bank_obj1.print_accountdetails()
    print()

    # customer wants to withdraw amount from his bank account.
    bank_obj1.withdraw_amt(800)
    bank_obj1.print_accountdetails()
    print()

    # customer wants to withdraw amount from his bank account.
    bank_obj1.withdraw_amt(8000)
    bank_obj1.print_accountdetails()
    print()

    # customer details only
    bank_obj2 = Banking(1002)
    print('The details of customer:')
    bank_obj2.print_accountdetails()
    print()




