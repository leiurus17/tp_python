list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = ["a", "b", "c", "d"]

print list1
print list2
print list3

print "list[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

print list1
list1[2] = 2001
print "list1[2] = 2001"
print list1

print list1
del list1[2]
print "del list1[2]"
print list1

print len([1,2,3])
print [1,2,3] + [4,5,6]
print ["Hi!"] * 5
print 3 in [1, 2, 3]
print 4 in [1, 2, 3]

for x in [1, 2, 3]: print x

L = ['spam', 'Spam', 'SPAM']

print L[2]
print L[-2]
print L[1:]