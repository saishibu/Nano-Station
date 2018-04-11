
import urllib, urllib2, cookielib,time,json 
from dbwrite import todb
import time
import RPi.GPIO as GPIO
user ='ubnt'
pswd='1234'
import ssl
pos=1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

ssl._create_default_https_context = ssl._create_unverified_context
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r=opener.open('https://192.168.179.107/login.cgi')
login_data=urllib.urlencode({'username':user, 'password':pswd,'action':'login'})
r=opener.open('https://192.168.179.107/login.cgi',login_data)
data=dict()
print "login success"
while(1):
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	print "next set"
	status_page=opener.open('https://192.168.179.107/status.cgi')
	status=status_page.read()
#	print (status)
	json_status=json.loads(status)
	signal=json_status['wireless']['signal']
	noise=json_status['wireless']['noisef']
	ccq=json_status['wireless']['ccq']
	distance=json_status['wireless']['distance']
	print str(signal) + 'db'
	print str(noise) + 'db';
	print str(ccq) 
	print str(distance) + 'm'
	signalinv=signal*-1
	if (signalinv>65):
		GPIO.output(17,GPIO.HIGH)
		pos =pos+1
		print "Auto mode"
	data={'signalstrength':signal,'noisefloor':noise,'pos':pos,'ccq':ccq,'distance':distance}
	todb(data)
	time.sleep(5)
	print "Data Stored"
	

