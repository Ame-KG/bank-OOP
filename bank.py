# we will have users and a bank class

# Parent Class: Users
# Store basic info
# method to show user details

# Child Class: Bank
# stores details about the acount 
# methods for deposit, withdrawal, view_balance

class User():

	def __init__(self, firstName, lastName, age, gender):
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.gender = gender

	def showUserDetails(self):
		details = {
		'First Name': self.firstName,
		'Last Name': self.lastName,
		'Age': self.age,
		'Gender': self.gender,
					}
		print('Personal Details...')
		return details

user1 = User('Ame', 'Kgomo', 20, 'M')


# print(user1.showUserDetails())

# accessing the key and the value through  a for loop
# for i, x in user1.showUserDetails().items():
# 	print(f' {i}: {x}')


class Bank(User):

	# inherited initialiser method
	def __init__(self, firstName, lastName, age, gender, balance = 0,):
		super().__init__(firstName, lastName, age, gender)
		self.balance = balance

	def showBalance(self):
		details = {
		'First Name': self.firstName,
		'Last Name': self.lastName,
		'Balance': self.balance}
		return details

	def deposit(self, amount):
		self.balance += amount
		print('Deposit Successful')

	def withdraw(self, amount):
		self.balance -= amount
		print('Withdrawal Succsesful')




jack = Bank('Jack', 'Wisowski', 33, 'M')

jack.deposit(10000)
print(jack.showBalance())

jack.withdraw(2000)
print(jack.showBalance())