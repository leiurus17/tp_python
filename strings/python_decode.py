from __builtin__ import str
str = "this is string example....wow!!!"

str = str.encode('base64', 'strict')

print str
print str.decode('base64', 'strict')

#There's a mysterious from __builtin__ import str that appeared
#Because I used the variable "str" and it seems that it's a reserved word