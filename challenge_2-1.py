#create a class name called BankAccount
class BankAccount:
#create a function called __init__ which include account information
	def __init__(self, account_number, account_holder_name,initial_balance=0.0):
		self.__account_number = account_number
		self.__account_holder_name = account_holder_name
		self.__account_balance = initial_balance
#create a deposit function 
	def deposit(self, amount):
#check the amount is greater than 0
		if amount > 0:
			self.__account_balance += amount
			print("Deposited ₹{}. New balance: ₹{}".format(amount, self.__account_balance))
#if condition is fail than executed else 
		else:
			print("Invalid deposit amount. Please deposit a positive amount.")
#create a function called withdraw
	def withdraw(self, amount):
#check if the amount greater then 0 and check withdraw amount is in the account
		if amount > 0 and amount <= self.__account_balance:
			self.__account_balance -=amount
			print("Withdraw ₹{}. New balance: ₹{}".format(amount,self.__account_balance))
#if condition is fail than executed the else condition
		else:
			print("invalid withdraw amount or insufficient balance.")
#create a function called display_balance and display account information
	def display_balance(self):
		print("Account balance for {} (Account #{}): ₹{}". format(self.__account_holder_name, self.__account_number ,self.__account_balance))
account = BankAccount(account_number='123456789',account_holder_name="keyan", initial_balance=5000.0)
account.display_balance()
account.deposit(500.0)
account.withdraw(200000.0)
account.display_balance()
