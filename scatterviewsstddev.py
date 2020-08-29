#!/usr/bin/python
import psycopg2
import numpy
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
	cursor.execute("SELECT standarddeviation from stddevmedian where country='IN' AND operationtype='views' ")
	stddev = cursor.fetchall()
	cursor.execute("SELECT median from stddevmedian where country='US' AND operationtype='views'")
	stddev1 = cursor.fetchall()
	cursor.execute("SELECT median from stddevmedian where country='CA' AND operationtype='views'")
	stddev2 = cursor.fetchall()
	cursor.execute("SELECT median from stddevmedian where country='FR' AND operationtype='views'")
	stddev3 = cursor.fetchall()
	cursor.execute("SELECT median from stddevmedian where country='RU' AND operationtype='views'")
	stddev4 = cursor.fetchall()
	cursor.execute("SELECT * from viewscount where country='IN' ")
	viewsIN = cursor.fetchall()
	cursor.execute("SELECT * from viewscount where country='US' ")
	viewsUS = cursor.fetchall()
	cursor.execute("SELECT * from viewscount where country='CA' ")
	viewsCA = cursor.fetchall()
	cursor.execute("SELECT * from viewscount where country='FR' ")
	viewsFR = cursor.fetchall()
	cursor.execute("SELECT * from viewscount where country='RU' ")
	viewsRU = cursor.fetchall()

	categoryid4=[]
	categoryid5=[]
	categoryid6=[]
	categoryid7=[]
	categoryid8=[]
	for data in viewsIN:
		categoryid4.append(data[2])
		#uploads4.append(data[2])
	#       print data

	for data in viewsUS:
		categoryid5.append(data[2])
		#uploads4.append(data[2])
	#       print data

	for data in viewsCA:
		categoryid6.append(data[2])
		#uploads4.append(data[2])
	#       print data

	for data in viewsFR:
		categoryid7.append(data[2])
		#uploads4.append(data[2])
	#       print data

	for data in viewsRU:
		categoryid8.append(data[2])
		#uploads4.append(data[2])
	#       print data

	print(categoryid5)
	#goal_types = ['IN','US','CA','FR','RU'] 
	#goals = [stddev[0][0],stddev1[0][0],stddev2[0][0],stddev3[0][0],stddev4[0][0]] 
	#colors = ['y','r','b','m','g'] 
	#plt.pie(goals, labels = goal_types, colors=colors ,shadow = True, explode = (0.05, 0.05, 0.05, 0.05, 0.05),autopct = '%1.1f%%') 
	#plt.axis('equal') 
	#plt.show()

	#fig = plt.figure()
	#ax = fig.add_axes([0,0,1,1])
	#langs = ['IN','US','CA','FR','RU'] 
	#students = [23,17,35,29,12]
	#ax.bar(langs,students)
	#plt.show()

	#print (categoryid4[0][0])
	medianIN = numpy.random.normal(categoryid4)
	medianCA = numpy.random.normal(categoryid6)
	medianFR = numpy.random.normal(categoryid7)
	medianRU = numpy.random.normal(categoryid8)
	grades_range = numpy.random.normal([10000000000, 15000000000, 20000000000, 25000000000, 30000000000, 35000000000, 40000000000, 45000000000, 50000000000, 55000000000, 60000000000, 65000000000, 70000000000, 75000000000, 80000000000, 85000000000, 90000000000,95000000000])
	grades_rangeUS = numpy.random.normal([10000000000, 15000000000, 20000000000, 25000000000, 30000000000, 35000000000, 40000000000, 45000000000, 50000000000, 55000000000, 60000000000, 65000000000, 70000000000, 75000000000, 80000000000, 85000000000, 90000000000])
	#fig=plt.figure()
	#ax=fig.add_axes([0,0,1,1])
	#ax.scatter(grades_range, girls_grades, color='r')
	#ax.scatter(grades_range, boys_grades, color='b')
	#ax.set_xlabel('Grades Range')
	#ax.set_ylabel('Grades Scored')
	#ax.set_title('scatter plot')
	plt.scatter(medianIN,grades_range)	
	plt.show()
	
	medianUS = numpy.random.normal(categoryid5)
	plt.scatter(medianUS,grades_range)	
	plt.show()
	plt.scatter(medianCA,grades_rangeUS)	
	plt.show()
	plt.scatter(medianFR,grades_range)	
	plt.show()
	plt.scatter(medianRU,grades_range)	
	plt.show()

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

cursor.close()
con.close()
