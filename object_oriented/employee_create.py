from Employee import Employee

emp1 = Employee("Ava", 2000)

emp2 = Employee("Emma", 3000)

print Employee.empCount
print emp1.name
print emp2.name
print emp1.displayEmployee()
print emp2.displayEmployee()

emp1.age = 8
print emp1.age
emp1.age = 7
emp2.age = 9
print emp1.age
print emp2.age

del emp1.age
del emp2.age