#!/usr/bin/env python3

import csv
from datetime import datetime

# 1. load input.csv into a variable called `polls`
with open('input.csv') as f:
	reader = csv.DictReader(f)
	rows =list(reader)
	polls = [dict(row) for row in rows]
   
# 2. write a new file called output.csv and write a row with two headers: "date" and "approve"
with open('output.csv', "w") as f:
	writer = csv.writer(f)
	writer.writerow(['date', 'approval'])


#	3. Loop through each row of `polls` 
	for p in polls:
		raw_date = p["enddate"]
		approve= p['approve']

# 4. and within that loop... convert the format of `enddate` from "1/22/2017" to "22-Jan-17"
		date_format = "%m/%d/%Y"
		parsed_date = datetime.strptime(raw_date, date_format)
		date_str = parsed_date.strftime("%d-%b-%y")

# 5. write a new row of data with the transformed date and value for "approve" 
		writer.writerow([date_str, approve])


	
#By Rees Sweeney-Taylor, Alina Cough, Adam Staveski