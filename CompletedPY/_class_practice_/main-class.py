from Employee import Employee
from Manager import Manager

if __name__=="__main__":
	emp1 = Employee("Manny", 3000)
	emp1.displayEmployee()
	emp2 = Employee("Cage", 2500)
	emp2.displayEmployee()
	mng1 = Manager("Lord", 5000)
	mng1.displayEmployee()
