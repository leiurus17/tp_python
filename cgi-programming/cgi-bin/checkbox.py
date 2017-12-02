# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('math'):
    math_flag = "ON"
else:
    math_flag = "OFF"
    
if form.getvalue('physics'):
    physics_flag = "ON"
else:
    physics_flag = "OFF"
    
if form.getvalue('chemistry'):
    chemistry_flag = "ON"
else:
    chemistry_flag = "OFF"
    
if form.getvalue('biology'):
    biology_flag = "ON"
else:
    biology_flag = "OFF"
    
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Checkbox - Third CGI Program</title>"
print "</head>"
print "<body>"
print "<h2> Checkbox Math is : %s</h2>"      %math_flag
print "<h2> Checkbox Physics is : %s</h2>"   %physics_flag
print "<h2> Checkbox Chemistry is : %s</h2>" %chemistry_flag
print "<h2> Checkbox Biology is : %s</h2>"   %biology_flag
print "</body>"
print "</html>"