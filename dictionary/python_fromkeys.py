seq  = ('name', 'age', 'sex')
dictz = dict.fromkeys(seq)

print "New Dictionary : %s" % str(dictz)

dictz = dict.fromkeys(seq, 10)

print "New Dictionary : %s" % str(dictz)