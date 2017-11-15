from Parent import Parent

class Child(Parent): # Define child class
    
    def __init__(self):
        print "Calling child constructor"
        
    def childMethod(self):
        print "Calling child method"