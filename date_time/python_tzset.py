import time
import os

os.environ['TZ'] = 'EST+05EDT,M4.10,M10.5.0'
#time.tzset()
print time.strftime('%X %x %Z')
