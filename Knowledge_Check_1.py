#Import library for HTTP requests
from posixpath import split
import requests as req
#Import pandas to structure 
import pandas as pd

import math

#set variable for where data will be requested from

usa_request = req.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")

#Convert to JSON to make easier to read into dataframe? 
x =usa_request.json()

# Create structure data using pandas that makes data more readable 
df = pd.DataFrame(x["data"])

#Count columns and rows

count_cols = len(df.axes[1])
count_rows = len(df.axes[0])

headers= list(df)


#Print stuff

print( "Data USA Table\n")
print(df)
print("\n")

print("Headers in Data USA Table" + headers)
print("Number of columns in table: " +count_cols)
print("Number of rows in table: " + count_rows)





