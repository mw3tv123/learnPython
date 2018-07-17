class Employee:
	'Common base class for all employees'
	empCount = 0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		
	def __del__(self):
		class_name = self.__class__.__name__
		print class_name, "destroyed"
		
	def displayCount(self):
		print "Total Employee %d" % Employee.empCount
		
	def displayEmployee(self):
		print "Name: %10s" % self.name, " | Salary: ", self.salary
		
	def work(self, time):
		
