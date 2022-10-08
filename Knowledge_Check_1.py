#Import library for HTTP requests
import numpy as np
import requests as req
#Import pandas to structure 
import pandas as pd

#set variable for where data will be requested from

usa_request = req.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")

#Convert to JSON to make easier to read into dataframe? 
x =usa_request.json()

# Create structure data using pandas that makes data more readable 
df = pd.DataFrame(x["data"])

#Getting headers in a list
headers= list(df)

#Count columns and rows
count_cols = len(df.axes[1])
count_rows = len(df.axes[0])

#Max value of pop column 
max_pop = df["Population"].max()
av_pop = df["Population"].mean()

#Query in pandas 
#Q = df.query(df(["Population"]>322903031) & (df(["Year"] < 2019)))---Why didn't this work? Cast as a int but still was read as int. 
Q = df.query('Population ==' +str( max_pop))

inx = df.iloc[:,[2,3]]


#Print stuff
print( "Data USA Table\n")
print(df)
print("\n")

print("Headers in Data USA Table" + str(headers))
print("Number of columns in table: " + str(count_cols))
print("Number of rows in table: " + str(count_rows))
print("The max pop was: " + str(max_pop))
print ("The average pop was: " + str(av_pop))
print("\n")
print("Result of Query:\n" + str(Q))

print("\n")
print("Printing the 2nd & 3rd columns of the table \n" + str(inx))




