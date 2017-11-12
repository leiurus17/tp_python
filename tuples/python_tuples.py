tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d", "e"
tup4 = (50,)

print tup1
print tup2
print tup3
print tup4

print tup1[0]
print tup2[1:5]

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# You cannot update tuples
# tup1[0] = 100

# So let's create a new tuple as follows

tup3 = tup1 + tup2
print tup3
del tup3
#print tup3

print len(tup1)
print (1, 2, 3) + (4, 5, 6)
print ('Hi!',) * 4
print 3 in (1, 2, 3)
print 4 in (1, 2, 3)

for x in (1, 2, 3) : print x