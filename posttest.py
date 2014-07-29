import urllib2, urllib

token = "1432579593.1d71bb6.e407d5ce5f4b4cc68ad3852efc9717df"
params = urllib.urlencode({ "token" : token})
print params
dir="https://www.instagram.com/oauth/revoke_access?%s" %(params)


request = urllib2.Request(dir)
print request.get_full_url()
response = urllib2.urlopen(request).read()

print response