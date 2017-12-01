import re

line = "Cats are smarter than dogs"

# Matching
matchObj = re.match(r'dogs', line, re.M|re.I)
if matchObj:
    print "match ---> matchObj.group(): ", matchObj.group()
else:
    print "No match!"
    
# Searching
searchObj = re.search(r'dogs', line, re.M|re.I)
if searchObj:
    print "search ---> searchObj.group(): ", searchObj.group()
else:
    print "Nothing found!!!"