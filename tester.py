import random
import time
import socket
import datetime
import re

a = [0,1]
print a[0]
print len(a)

for x in range(0, 5):
    print "We're on time %d" % (x)
print random.randint(1.5*60,5*60)

print socket.gethostbyname(socket.gethostname())
print socket.gethostbyname(socket.getfqdn())

print datetime.datetime.now().time()

print 'testing.sss'.strip('.')
print re.split(r'\.', str(datetime.datetime.now().time()))[0]

start_time = time.time()
time.sleep(0)
end_time = time.time()
print 'Elapsed time %s seconds' % (round(end_time-start_time))
print str(datetime.timedelta(seconds=round(end_time-start_time)))

mediaid = '121'
mediausername = 'petronella'

fo = open("foo.txt", "ab+")

fo.write('%s, %s' % (mediaid, mediausername))

fo.write('testing2\n')

fo.close()

# import httplib, urllib
# params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
# conn = httplib.HTTPConnection("musi-cal.mojam.com:80")
# conn.request("POST", "/cgi-bin/query", params, headers)
# response = conn.getresponse()
# print response.status, response.reason
# data = response.read()
# conn.close()