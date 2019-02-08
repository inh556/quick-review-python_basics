import time
print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y%m%d'))
 
import datetime

print(datetime.datetime.now()) # current time
newtime = datetime.timedelta(minutes=10)
print(newtime + datetime.datetime.now()) # ten minutes later

one_day = datetime.datetime(2008, 5, 1) #someday 
newtime = datetime.timedelta(days=10)
print(newtime + one_day) # ten days later