from googleapiclient.discovery import build

api_key = 'AIzaSyDyvYZq6ucVpRno2YBH89Tz7FYjAIbGY3s'


def video_comments(video_id):
    # empty list for storing reply
    #replies = []

    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=api_key)

    # retrieve youtube video results
    video_response = youtube.commentThreads().list(
        part='id,snippet,replies',
        videoId=video_id
    ).execute()




    # iterate video response
    ids = []
    comments = []
    while video_response:

        # extracting required info
        # from each result object
        count = 0
        for item in video_response['items']:
            count = count + 1

            id = item['id']
            ids.append(id)
            #print(id)
            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
            #print(count)
            if count > 20:
                break

            # counting number of reply of comment
            #replycount = item['snippet']['totalReplyCount']

            # if reply is there
            '''if replycount > 0:

                # iterate through all reply
                for reply in item['replies']['comments']:
                    # Extract reply
                    reply = reply['snippet']['textDisplay']'''
        #print(comments)
        break

                    # Store reply is list
                    #replies.append(reply)

            # print comment with list of reply
            #print(comment, end='\n\n')
            #rows = [id, comment]
            #csvwriter.writerows(rows)
            # empty reply list
            #replies = []
    import pandas as pd
    import numpy as np
    a = np.array(ids)
    b = np.array(comments)

    df = pd.DataFrame({"id": a, "comment": b})
    df.to_csv("comments.csv", index=False)

    import pandas as panda
    datasetToPredict = panda.read_csv("comments.csv")
    x = datasetToPredict.head(2)
    print(x)
    # Again repeat
    '''if 'nextPageToken' in video_response:
               video_response = youtube.commentThreads().list(
                   part='snippet,replies',
                   videoId=video_id
               ).execute()
           else:
               break'''


# Enter video id
from urllib.parse import urlparse
url_data = urlparse("https://www.youtube.com/watch?v=RG9TMn1FJzc")
print(url_data.query[2::])

#video = query["v"][0]
video_id = url_data.query[2::]

# Call function
video_comments(video_id)