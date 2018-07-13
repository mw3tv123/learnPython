from Employee import Employee

class Manager(Employee):
	__position = "Manager"
	
	def displayEmployee(self, position):
		print "Name: %10s" % self.name, " | Salary: ", self.salary, " | Position: ", self.position
