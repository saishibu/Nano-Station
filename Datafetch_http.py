
import urllib, urllib2, cookielib,time,json


user ='ubnt'
pswd='1234'
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r=opener.open('https://192.168.179.100/login.cgi')
login_data=urllib.urlencode({'username':user, 'password':pswd,'action':'login'})
r=opener.open('https://192.168.179.100/login.cgi',login_data)

while(1):
	status_page=opener.open('https://192.168.179.100/status.cgi')
	status=status_page.read()
	print (status)
	json_status=json.loads(status)
	signal=json_status['wireless']['signal']
	print str(signal) + 'db'
	time.sleep(5)
	

