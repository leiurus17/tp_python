#Function definition is here
def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print "Output is: "
    print arg1
    for var in vartuple:
        print var + 1
    return

# Now you can call printinfo function
first = 10
print first
printinfo(first)

second = (10, 20, 30, 40, 50)
print second
printinfo(second)

# Now direct to the function
printinfo(10, 20, 30, 40, 50)