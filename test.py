import urllib, urllib2, cookielib,time,json
from dbwrite import todb
data=dict()
signal=-45
noise =90
pos=90
while(1):
	data={'signal_strength':signal,'noise_floor':noise,'ch_master_position':pos}
	todb(data)
	time.sleep(5)
	

