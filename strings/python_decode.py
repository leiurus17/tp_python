from __builtin__ import str
str = "this is string example....wow!!!"

str = str.encode('base64', 'strict')

print str
print str.decode('base64', 'strict')