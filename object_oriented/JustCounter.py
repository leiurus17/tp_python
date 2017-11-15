# Data Hiding

# An object's attributes may or may not be visible outside the class definition.
# You need to name attributes with a double underscore prefix, and those attributes
# then are not be directly visible to outsiders.


class JustCounter:
    __secretCount = 0 # Double underscore, hidden
    
    def count(self):
        self.__secretCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter._JustCounter__secretCount # Can still access the __secretCount

# By accessing instance._className__variable instead of just the double underscore name, you can access the hidden value

print counter.__secretCount

# https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-a-single-and-a-double-underscore-before-an-object-name