dictionary = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dictionary['Name']: ", dictionary['Name']
print "dictionary['Age']: ", dictionary['Age']
print "dictionary['Class']: ", dictionary['Class']
#print "dictionary['Sagala']: ", dictionary['Sagala']

#Update a dictionary
dictionary['Age']   = 12
dictionary['Class'] = 'Hogwarts'

print "dictionary['Name']: ", dictionary['Name']
print "dictionary['Age']: ", dictionary['Age']
print "dictionary['Class']: ", dictionary['Class']

student = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print student
del student['Name']
print student
student.clear()
print student
#del student
#print student