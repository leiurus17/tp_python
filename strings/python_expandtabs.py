str  = "this is\tstring example." #\t tab

print "Original string:" + str
print "Default expanded tab: " + str.expandtabs() # default is 8. Looks like nothing happens
print "Double expanded tab:" + str.expandtabs(16)
print "Quad expanded tab:" + str.expandtabs(32)