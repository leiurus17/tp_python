list1, list2 = [123, 'xyz'], [456, 'abc']

print cmp(list1, list2)
print cmp(list2, list1)

list3 = list2 + [786]

print cmp(list2, list3)

list1, list2 = [123, 'xyz'], [123, 'xyz']

print cmp(list1, list2)
print cmp(list2, list1)