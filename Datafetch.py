
import urllib, urllib2, cookielib,time,json


user ='ubnt'
pswd='amma'

cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r=opener.open('http://192.168.1.20/login.cgi')
login_data=urllib.urlencode({'username':user, 'password':pswd,'action':'login'})
r=opener.open('http://192.168.1.20/login.cgi',login_data)

while(1):
	status_page=opener.open('http://192.168.1.20/status.cgi')
	status=status_page.read()
	print (status)
	json_status=json.loads(status)
	signal=json_status['wireless']['signal']
	print str(signal) + 'db'
	time.sleep(1)
	

