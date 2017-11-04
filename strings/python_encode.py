string_variable = "This is a string sample. Wow!!!"

print string_variable.encode('base64', 'strict')
string_variable = string_variable.encode('base64', 'strict')
print string_variable.decode('base64', 'strict')

#No from __builtin__ import str happened