def functionName(level):
    if level < 1:
        raise "Invalid level!", level
        # The code below to this would not be executed
        # If we raise the exception
        print level
    print "Hello! %d" % level

functionName(2)
functionName(0)