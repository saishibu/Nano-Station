import pymysql

def todb (data):

	conn =pymysql.connect(database="oceannet",user="oceannet",password="1234",host="localhost")
	cur=conn.cursor()
	cur.execute("INSERT INTO status(signal_strength,noise_floor,ch_master_position) VALUES(%(signal_strength)s,%(noise_floor)s,%(ch_master_position)s);",data)
	conn.commit()
	conn.close()
