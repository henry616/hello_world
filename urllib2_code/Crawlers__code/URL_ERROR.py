import urllib2

req = urllib2.Request('http://bbs.csdn.net/callmewhy')

print"lal"

try: urllib2.urlopen(req)

except urllib2.URLError, e:
    #print e.reason
    print e.read()
