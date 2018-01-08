
import urllib, urllib2, cookielib,time,json
from dbwrite import todb
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

user ='ubnt'
pswd='1234'
import ssl
pos =1

ssl._create_default_https_context = ssl._create_unverified_context
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r=opener.open('http://192.168.179.100/login.cgi')
login_data=urllib.urlencode({'username':user, 'password':pswd,'action':'login'})
r=opener.open('http://192.168.179.100/login.cgi',login_data)
data=dict()
while(1):
	GPIO.output(17,GPIO.HIGH) #IN2
	GPIO.output(27,GPIO.HIGH) #IN1
	status_page=opener.open('http://192.168.179.100/status.cgi')
	status=status_page.read()
	print (status)
	json_status=json.loads(status)
	signal=json_status['wireless']['signal']
	noise=json_status['wireless']['noisef']
	print str(signal) + 'db'
	print str(noise) + 'db'
	data={'signal_strength':signal,'noise_floor':noise,'ch_master_position':pos}
	signal_pos=signal*-1
	print signal_pos
	if(signal_pos>60): 
		GPIO.output(17,GPIO.LOW) #IN2
		GPIO.output(27,GPIO.HIGH) #IN1
		print "high"
	todb(data)
	time.sleep(5)
