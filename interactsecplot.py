#!/usr/bin/python
import psycopg2
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
	cursor.execute("SELECT * from interactioncount where country='IN' ")
	result = cursor.fetchall()
	cursor.execute("SELECT * from interactioncount where country='US' ")
	result1 = cursor.fetchall()
	cursor.execute("SELECT * from interactioncount where country='CA' ")
	result2 = cursor.fetchall()
	cursor.execute("SELECT * from interactioncount where country='FR' ")
	result3 = cursor.fetchall()
	cursor.execute("SELECT * from interactioncount where country='RU' ")
	result4 = cursor.fetchall()
	categoryid=[]
	categoryid1=[]
	categoryid2=[]
	categoryid3=[]
	categoryid4=[]
	uploads=[]
	uploads1=[]
	uploads2=[]
	uploads3=[]
	uploads4=[]
	x=0
	for data in result:
		x=x+1
		if(x<17):
			categoryid.append(data[1])
			uploads.append(data[2])
			print(data[1], data[2])
		#       print data
	
	for data in result1:				
		categoryid1.append(data[1])
		uploads1.append(data[2])
		print(data[1], data[2])
	#       print data

	for data in result2:
		categoryid2.append(data[1])
		uploads2.append(data[2])
		print(data[1], data[2])
	#       print data


	for data in result3:
		categoryid3.append(data[1])
		uploads3.append(data[2])
		print(data[1], data[2])
	#       print data
	x=0
	for data in result4:
		x=x+1
		if(x<17):
			categoryid4.append(data[1])
			uploads4.append(data[2])
			print(data[1], data[2])
		#       print data


	print (categoryid)
	print(uploads)
	print (categoryid1)
	print(uploads1)
	print (categoryid2)
	print(uploads2)
	print (categoryid3)
	print(uploads3)
	print (categoryid4)
	print(uploads4)
	#population_age = categoryid
	#bins = uploads
	#population_age1 = categoryid1
	#bins1 = uploads1
	#plt.hist(population_age, bins, histtype='bar')
	#plt.hist(population_age1, bins1, histtype='bar')
	#plt.xlabel('Top 10 Categories')
	#plt.ylabel('Category Id')
	#plt.plot(range(10))
	#plt.xlim(0,10000)
	#plt.ylim(0,30)
	#plt.title('Histogram')
	#plt.show()
	category = categoryid 
	uploads = uploads
	plt.plot([],[], color='b', label = 'IN uploads')
	plt.plot([],[], color='r', label = 'US uploads')
	plt.plot([],[], color='m', label = 'CA uploads')
	plt.plot([],[], color='g', label = 'FR uploads')
	plt.plot([],[], color='c', label = 'RU uploads')
	plt.stackplot(category, uploads,uploads1,uploads2,uploads3,uploads4, colors = ['b','r','m','g','c'])
	plt.legend()
	plt.title('interaction')
	plt.xlabel('category')
	plt.ylabel('interaction count')
	plt.show()
	#goal_types = categoryid 
	#goals = uploads 
	#colors = ['y','r','b','c','m','g','k','b','m','r'] 
	#plt.pie(goals, labels = goal_types, colors=colors ,shadow = True, explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05), 		#autopct = '%1.1f%%') 
	#plt.axis('equal') 
	#plt.show()
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

cursor.close()
con.close()

