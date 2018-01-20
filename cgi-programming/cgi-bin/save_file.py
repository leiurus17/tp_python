import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from filename to avoid
    # directory traversal attacks
    
    # Linux / Unix
    # fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
    
    # Windows
    fn = os.path.basename(fileitem.filename)
    
    # File will be uploaded to the /tmp folder E.g. C:/tmp
    open('/tmp/' + fn, 'wb').write(fileitem.file.read())
    
    message = 'The file "' + fn + '" was uploaded successfully'
    
else:
    message = 'No file was uploaded'
    
print """\
Content-Type: text/html\n
<html>
    <body>
        <p>%s</p>
    </body>
</html>
""" % (message, )