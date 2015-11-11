import csv
import re
import json

with open('./trades/synth-0000','rb') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='\t')
    for row in csv_reader:
      if row[2]=='1':
        print "%s	%s	%s" % (row[0],row[1],row[3])
      elif row[2]=='2':
        print "%s	%d	%s" % (row[0],int(row[1])+10000,row[3])
      elif row[2]=='3':
        print "%s	%d	%s" % (row[0],int(row[1])+100000,row[3])

