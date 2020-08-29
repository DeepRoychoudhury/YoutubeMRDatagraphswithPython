import psycopg2
import numpy as np
import matplotlib.pyplot as plt
con = None

try:
	con = psycopg2.connect(
		user = "postgres",
		password = "postgres",
		host = "pda.cpwytlyekgvv.us-east-1.rds.amazonaws.com",
		port = "5432",
		database = "YoutubeMR"
	    )
	cursor = con.cursor()
	cursor.execute("SELECT * from viewscount where country='IN' ")
	result = cursor.fetchall()
	cursor.execute("SELECT * from viewscount where country='US' ")
	result1 = cursor.fetchall()
	cursor.execute("SELECT * from viewscount where country='CA' ")
	result2 = cursor.fetchall()
	cursor.execute("SELECT * from viewscount where country='FR' ")
	result3 = cursor.fetchall()
	cursor.execute("SELECT * from viewscount where country='RU' ")
	result4 = cursor.fetchall()

	cursor.execute("SELECT standarddeviation from stddevmedian where country='IN' AND operationtype='views' ")
	stdresult = cursor.fetchall()
	cursor.execute("SELECT standarddeviation from stddevmedian where country='US' AND operationtype='views'")
	stdresult1 = cursor.fetchall()
	cursor.execute("SELECT standarddeviation from stddevmedian where country='CA' AND operationtype='views'")
	stdresult2 = cursor.fetchall()
	cursor.execute("SELECT standarddeviation from stddevmedian where country='FR' AND operationtype='views'")
	stdresult3 = cursor.fetchall()
	cursor.execute("SELECT standarddeviation from stddevmedian where country='RU' AND operationtype='views'")
	stdresult4 = cursor.fetchall()

	categoryid=[]
	categoryid1=[]
	categoryid2=[]
	categoryid3=[]
	categoryid4=[]
	categoryid5=[]
	categoryid6=[]
	categoryid7=[]
	categoryid8=[]
	categoryid9=[]
	uploads=[]
	uploads1=[]
	uploads2=[]
	uploads3=[]
	uploads4=[]
	x=0
	for data in result:
		x=x+1
		if(x<17):
			if data[2] > stdresult[0][0] : 
				categoryid.append(data[2]-stdresult[0][0])
				categoryid1.append(data[2])
				uploads.append(data[1])
				print(data[1], data[2])
			else :
				categoryid.append(stdresult[0][0]-data[2])
				categoryid1.append(data[2])
				uploads.append(data[1])
			#       print data
	

	
	height = categoryid
	bars = uploads
	y_pos = np.arange(len(bars))
	 
	# Create bars
	plt.bar(y_pos, height)
	 
	# Create names on the x-axis
	plt.xticks(y_pos, bars)
	 
	# Show graphic
	plt.show()
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

cursor.close()
con.close()

