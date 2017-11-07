from string import maketrans # Required to call maketrans function.

intab  = "aeiou"
outtab = "12345"

transtab = maketrans(intab, outtab)

str = "this is string example. wow!!!"
print str.translate(transtab)