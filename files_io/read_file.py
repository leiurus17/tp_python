# Open a file
fo  = open("foo.txt", "r+")
str = fo.read(10)
print "Read string is: ", str
fo.seek(0, 0) # Reset position
str2 = fo.read()
print "Read string is: ", str2
# Close opened file
fo.close()