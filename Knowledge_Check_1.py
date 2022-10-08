# Import library for HTTP requests
import requests

# set variable for where data will be requested from

#bored_request = requests.get("https://www.boredapi.com/api/activity")

bored_request = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")

# print the results from the API call in TXT. This is to check that the HTTP call was successfull 
print(bored_request.text)
