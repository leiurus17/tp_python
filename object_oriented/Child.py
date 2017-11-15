from Parent import Parent

class Child(Parent): # Define child class
    
    def __init__(self):
        print "Calling child constructor"
        
    def childMethod(self):
        print "Calling child method"
        
    def awesomeMethod(self): #Overriding method
        print "This is awesome method from child class."