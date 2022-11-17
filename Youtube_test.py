#Importing required packages
from googleapiclient.discovery import build
import pandas as pd
# Import file with secerts 
import secrets as sec

#Creating Objects
youTubeApiKey= sec.API_KEY
youtube= build("youtube","v3",developerKey=youTubeApiKey)
channelId = "UCgvqvBoSHB1ctlyyhoHrGwQ"

#Calling Data from API
statchanneldata=youtube.channels().list(part="statistics",id=channelId).execute()
statchannel=statchanneldata["items"][0]["statistics"]

#Getting Snippet Data
snippetdata=youtube.channels().list(part="snippet",id=channelId).execute()

#Getting Details of all videos
contentdata=youtube.channels().list(id=channelId,part="contentDetails").execute()
playlist_id = contentdata["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
videos = [ "color"]
next_page_token = None
while 1:
    res = youtube.playlistItems().list(playlistId=playlist_id,
                                   part="snippet",
                                   maxResults=10,
                                   pageToken=next_page_token).execute()

    videos += res["items"]
    next_page_token = res.get("nextPageToken")
    if next_page_token is None:
        break

#Getting the statistics of each video

stats = [] 
video_ids = list(map(lambda x:x['snippet']['resourceId']['videoId'], videos)) 
for i in range(0, len(video_ids), 40):
    res = (youtube).videos().list(id=",".join(video_ids[i:i+40]),part="statistics").execute()
    stats += res["items"]



#Collecting All Information in a List & creating a dataframe
title=[ ]
liked=[ ]
views=[ ]
url=[ ]
comment=[ ]

for i in range(len(videos)):
    #title.append((videos[i])["snippet"]["title"])
    url.append("https://www.youtube.com/watch?v="+(videos[i])["snippet"]["resourceId"]["videoId"])
    liked.append(int((stats[i])["statistics"]["likeCount"]))
    views.append(int((stats[i])["statistics"]["viewCount"]))
    comment.append(int((stats[i])["statistics"]["commentCount"]))
    data={"title":title,"url":url,"views":views,"comment":comment}
    df=pd.DataFrame(data)

df





# Request will return search data for the channelID 

request_search = youtube.search().list(
        part="snippet",
        channelId="UC2Qw1dzXDBAZPwS7zm37g8g",
        order="viewCount",
        safeSearch="moderate"
    )
response_search = request_search.execute()

df = pd.json_normalize(response_search) 
print(df.columns.tolist())


#print(response_search)

request = youtube.playlists().list(
        part="snippet,contentDetails",
        channelId="UC2Qw1dzXDBAZPwS7zm37g8g",
        maxResults=5
    )
response = request.execute()


# df = pd.json_normalize(response) 
# print(df.columns.tolist())
# print(df.to_string())
# print(df)

#print(response)

#request = youtube.playlists().list( part="snippet,contentDetails", channelId="UC2Qw1dzXDBAZPwS7zm37g8g", maxResults=25)

# Query execution
#response = request.execute()
# Print the results from the excution of the request
#print(response)
