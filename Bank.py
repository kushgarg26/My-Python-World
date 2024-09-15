class Bank:
    print("Running")
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        print("In menu")  # Debugging line
        user_input = input("""Hello, would you like to proceed?
        Enter 1 to create_pin 
        Enter 2 to deposit
        Enter 3 to withdraw
        Enter 4 to check_balance
        Enter 5 to exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Exiting...")
        else:
            print("Invalid syntax")
            self.menu()  # Restart the menu if input is invalid

    def create_pin(self):
        self.pin = input("Enter the pin: ")
        print("Pin set successfully")
        self.menu()

    def deposit(self):
        temp = input("Enter the pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid pin")
        self.menu()

    def withdraw(self):
        temp = input("Enter the pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful")
            else:
                print("Operation failed: Insufficient balance")
        else:
            print("Invalid pin")
        self.menu()

    def check_balance(self):
        temp = input("Enter the pin: ")
        if temp == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Invalid pin")
        self.menu()

bank = Bank()
