#!/usr/bin/python
import psycopg2
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
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
	cursor.execute("SELECT * from top10categories where country='IN' order by uploads")
	result = cursor.fetchall()
	cursor.execute("SELECT * from top10categories where country='US' order by uploads")
	result1 = cursor.fetchall()
	cursor.execute("SELECT * from top10categories where country='CA' order by uploads")
	result2 = cursor.fetchall()
	cursor.execute("SELECT * from top10categories where country='FR' order by uploads")
	result3 = cursor.fetchall()
	cursor.execute("SELECT * from top10categories where country='RU' order by uploads")
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
	for data in result:
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

	for data in result4:
		categoryid4.append(data[1])
		uploads4.append(data[2])
		print(data[1], data[2])
	#       print data

	print (categoryid)
	print(uploads)
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
	
	goal_types = categoryid 
	goals = uploads 
	colors = ['y','r','b','m','k','w','g','r','b','y'] 
	plt.pie(goals, labels = goal_types, colors=colors ,shadow = True, explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05), 		autopct = '%1.1f%%') 
	plt.axis('equal') 
	plt.show()

	goal_types = categoryid1 
	goals = uploads1 
	colors = ['y','r','b','m','k','w','g','r','b','y'] 
	plt1.pie(goals, labels = goal_types, colors=colors ,shadow = True, explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05), 		autopct = '%1.1f%%') 
	plt1.axis('equal') 
	plt1.show()

	goal_types = categoryid2 
	goals = uploads2 
	colors = ['y','r','b','m','k','w','g','r','b','y'] 
	plt.pie(goals, labels = goal_types, colors=colors ,shadow = True, explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05), 		autopct = '%1.1f%%') 
	plt.axis('equal') 
	plt.show()

	goal_types = categoryid3 
	goals = uploads3 
	colors = ['y','r','b','m','k','w','g','r','b','y'] 
	plt1.pie(goals, labels = goal_types, colors=colors ,shadow = True, explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05), 		autopct = '%1.1f%%') 
	plt1.axis('equal') 
	plt1.show()

	goal_types = categoryid4 
	goals = uploads4 
	colors = ['y','r','b','m','k','w','g','r','b','y'] 
	plt1.pie(goals, labels = goal_types, colors=colors ,shadow = True, explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05), 		autopct = '%1.1f%%') 
	plt1.axis('equal') 
	plt1.show()

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

cursor.close()
con.close()

