import csv
import re
import json

#format ="Symbol","Name","LastSale","MarketCap","IPOyear","Sector","industry","Summary Quote",


count=1
with open('./nasdaq.csv','rb') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
      if re.search('B$',row[3]):
        print '{ "create" : { "_index" : "finance", "_type" : "stock", "_id" : "%s" } }' % count
        print '{ "symbol" : "%s", "name":"%s" , "marketCap":"%s", "ipo":"%s","sector":"%s","industry":"%s" }' % (row[0],row[1],row[3],row[4],row[5],row[6])
	count+=1

with open('./nyse.csv','rb') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
      if re.search('B$',row[3]):
        print '{ "create" : { "_index" : "finance", "_type" : "stock", "_id" : "%s" } }' % count
        print '{ "symbol" : "%s", "name":"%s" , "marketCap":"%s", "ipo":"%s","sector":"%s","industry":"%s" }' % (row[0],row[1],row[3],row[4],row[5],row[6])
	count+=1
