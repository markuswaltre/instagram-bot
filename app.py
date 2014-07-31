##
## my new app for generating followers - yay
##

from instagram.client import InstagramAPI
#import socket
import time
import random
import datetime
import re

output = open('log.txt', 'ab+')

#ip_address = socket.gethostbyname(socket.gethostname())
#ip_address = socket.gethostbyname(socket.getfqdn())
ip_address = '80.203.71.193' # the above one doesn't return the correct ip

tag_name = 'follow4follow'

class Access:
	def __init__(self, token, secret, id):
		self.token = token
		self.secret = secret
		self.id = id

a = [ 
		Access(	#pythonplayarea
				"1432579593.1d71bb6.92708473c417460a93184f3bac9adea1",
			 	"c02f82afd80e4a12bb5b68b6c97775a6",
			 	 "1d71bb656bb4442ba099230aae9a5d2a"
			 ),		
		# Access(	#fashionlover, dammit this one is connect to wrong account
		# 		"184193267.36cd1d4.870d75a0f032438dbb9d57ef591c4941",
		# 	 	"47f27bb3759a4885af2113c1a5d475d2",
		# 	 	"36cd1d42cbeb4854ab63e56ad8236294"
		# 	 ),
		Access(	#fashionismypassion
				"1432579593.2a43e88.d3aa26c20bc64ccfb396ea5447862a18",
			 	"8e182224c5ff4ff3ac5b7c8659b047c3",
			 	"2a43e88c2e574c42bcfe77aa26bd2ee5"
			 )
	]

count = 0
tok_count = 0
start_time = time.time()

print ''
print 'Script starting'
print 'at time: %s' % (re.split(r'\.', str(datetime.datetime.now().time()))[0])
print ''

def initAPI(c):
	return InstagramAPI(access_token=a[c].token, client_ips=ip_address, client_secret=a[c].secret, client_id=a[c].id)

api = initAPI(0)
for x in range(0, 5):
	recent_media, next = api.tag_recent_media(count=10, tag_name=tag_name)
	# recent media by tag
	for media in recent_media:
		try:
			api.follow_user(user_id=media.user.id)
			api.like_media(media_id=media.id)
		except Exception, e:
			print e

			if '429' in str(e):
				tok_count+=1
				if(tok_count == len(a)):
					tok_count = 0

				print '429 found, switching token to number %s' % (tok_count)
				#api = initAPI(tok_count)
				# s = random.randint(25*60, 60*60) # 25:60 min sleep
				# print 'Sleeping for %s min' % (s/60)
				# time.sleep(s)
		else:
			output.write('%s, %s \n' % (media.user.id, media.user.username))
			print 'Followed %s' % (media.user.username)
			time.sleep(random.randint(0,4)) # random 0:9 sek
			print 'Liked media id %s' % (media.user.id)
			count+=1
			time.sleep(random.randint(30,90)) # 1:5 min ~ 3min - 1/3 velocity

end_time = time.time()
output.close()

print ''
print 'Script done'
print 'Followed and liked %s times' % (count)
print 'Elapsed time is %s seconds' % (round(end_time-start_time))
print '%s in (hh:mm:ss)' % (str(datetime.timedelta(seconds=round(end_time-start_time))))
print ''

