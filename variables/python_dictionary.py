dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name':'john', 'code':6734, 'dept':'sales', 2:4}

print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict[2]
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values