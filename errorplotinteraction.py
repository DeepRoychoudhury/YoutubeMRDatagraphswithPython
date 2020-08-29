#!/usr/bin/python
import psycopg2
import matplotlib.pyplot as plt
import numpy as np
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

	cursor.execute("SELECT standarddeviation from stddevmedian where country='IN' AND operationtype='interactive' ")
	stddev5 = cursor.fetchall()
	cursor.execute("SELECT standarddeviation from stddevmedian where country='US' AND operationtype='views'")
	stddev6 = cursor.fetchall()
	cursor.execute("SELECT standarddeviation from stddevmedian where country='CA' AND operationtype='views'")
	stddev7 = cursor.fetchall()
	cursor.execute("SELECT standarddeviation from stddevmedian where country='FR' AND operationtype='views'")
	stddev8 = cursor.fetchall()
	cursor.execute("SELECT standarddeviation from stddevmedian where country='RU' AND operationtype='views'")
	stddev9 = cursor.fetchall()
	standardev1=[stddev5,stddev6,stddev7,stddev8,stddev9]

	cursor.execute("SELECT interactioncount from interactioncount where country='IN' ")
	interact = cursor.fetchall()
	cursor.execute("SELECT interactioncount from interactioncount where country='US' ")
	interact1 = cursor.fetchall()
	cursor.execute("SELECT interactioncount from interactioncount where country='CA' ")
	interact2 = cursor.fetchall()
	cursor.execute("SELECT interactioncount from interactioncount where country='FR' ")
	interact3 = cursor.fetchall()
	cursor.execute("SELECT interactioncount from interactioncount where country='RU' ")
	interact4 = cursor.fetchall()
	viewscount=[]
	viewscount1=[]
	viewscount2=[]
	viewscount3=[]
	viewscount4=[]
	uploads=[]
	uploads1=[]
	uploads2=[]
	uploads3=[]
	uploads4=[]
	for data in interact:
		print (stddev5[0][0])
		if data[0] > stddev5[0][0]:
			viewscount.append(data[0]-stddev5[0][0])
			print(data[0]-stddev5[0][0])
		else:
			viewscount.append(stddev5[0][0]-data[0])
			print(stddev5[0][0]-data[0])
		#       print data
	
	#for data in result1:
	#	categoryid1.append(data[1])
	#	uploads1.append(data[2])
	#	print(data[1], data[2])
	#       print data

	#for data in result2:
	#	categoryid2.append(data[1])
	#	uploads2.append(data[2])
	#	print(data[1], data[2])
	#       print data


	#for data in result3:
	#	categoryid3.append(data[1])
	#	uploads3.append(data[2])
	#	print(data[1], data[2])
	#       print data

	#for data in result4:
	#	categoryid4.append(data[1])
	#	uploads4.append(data[2])
	#	print(data[1], data[2])
	#       print data

	x = np.array([5000000000, 10000000000, 15000000000, 20000000000, 25000000000, 30000000000, 35000000000, 40000000000, 45000000000, 50000000000, 55000000000, 60000000000, 65000000000, 70000000000, 75000000000, 80000000000, 85000000000, 90000000000])
	y = np.power(x, 2) # Effectively y = x**2
	e = np.array(viewscount)

	plt.errorbar(x, y, e, linestyle='None', marker='^', capsize=5)

	plt.show()

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

cursor.close()
con.close()

