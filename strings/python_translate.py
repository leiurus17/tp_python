from string import maketrans

intab = "aeiou"
outtab = "09876"

transtab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print str.translate(transtab)