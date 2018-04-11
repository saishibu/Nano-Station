import urllib, urllib2, cookielib,time,json 
from dbwrite import todb 
import time 
import RPi.GPIO as GPIO
import serial,pynmea2
port = serial.Serial("/dev/ttyUSB0", baudrate=9600)

user ='ubnt' 
pswd='1234' 
import ssl 
pos=1 
mode="Sarveshwari_april6" 

dir="" 
lat=""
lon=""
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(17,GPIO.OUT) 
GPIO.setup(27,GPIO.OUT)

f=open('pos','r')
pos=f.read()
f.close
print "last Ch_M position retreived"
pos  = int(str(pos))
print pos

ssl._create_default_https_context = ssl._create_unverified_context
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
r=opener.open('https://192.168.179.116/login.cgi')
login_data=urllib.urlencode({'username':user, 'password':pswd,'action':'login'})
r=opener.open('https://192.168.179.116/login.cgi',login_data)
data=dict()

print "login success"
while(1):
	a=1
	while a:
	        rcv = port.readline()
#	        print rcv[0:6]
	        if rcv[0:6] == '$GPGGA':
	                msg=pynmea2.parse(rcv)
	                lat=msg.lat
	                print lat
	                lon=msg.lon
	                print lon
			a=0
	GPIO.output(17,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	print "next set"
	status_page=opener.open('https://192.168.179.116/status.cgi')
	status=status_page.read()
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
	f=open('pos','w')
	if(signalinv==0):
		pos=pos+1
		GPIO.output(27,GPIO.HIGH)
		print "no signal"
		dir="no conn"

	if (signalinv>65):
		pos=pos+1
		f.write(str(pos))
		f.close
		if(pos<36):
			GPIO.output(27,GPIO.HIGH)
			print "Auto mode-FWD"
			dir="fwd"
		if(pos>36):
			GPIO.output(27,GPIO.LOW)
			GPIO.output(17,GPIO.HIGH)
			print "Auto mode-REV"
			dir="rev"
		if(pos>72):
			pos=0
			GPIO.output(27,GPIO.LOW)
			GPIO.output(17,GPIO.LOW)

	print pos
	data={'lat':lat,'lon':lon,'dir':dir,'mode':mode,'ss':signal,'nf':noise,'pos':pos,'ccq':ccq,'d':distance}
	todb(data)

	time.sleep(2)
	GPIO.output(27,GPIO.LOW)
	GPIO.output(17,GPIO.LOW)	
	time.sleep(3)
	print "Data Stored"
	

