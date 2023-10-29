# Creating Classes:

class Employee():
	"""docstring for Employee"""
	# Class variables
	# variables that are shared by all instances
	employeeCount = 0

	# Init Method:
	# Instance Variables 
	# variables unique to each instance of our class
	def __init__(self, name, surname, email, pay):
		# acess instance variable with the instane itself (self.)
		self.name = name
		self.surname = surname
		self.email = email
		self.pay = pay

		# access class variables by calling the class or even the instance{but that will only change it for the instance}
		Employee.employeeCount += 1
		print(Employee.employeeCount)

	# Class Methods
	# functions inside of class
	# always pass self
	def fullName(self):
		return self.name, self.surname



# Instantiating class
# -creating an instance of the class in other words

person1 = Employee("John", 'Jamerson','jj@dailybugel.yahoo', 50000)

# accessing class methods via dot operator
print(person1.fullName())



