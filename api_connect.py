import json

import googleapiclient.discovery
import googleapiclient.errors
#import YouTube API KEY
with open("credentials.json") as jfile:
    api = json.load(jfile)['API-KEY']
def get_channel_stats(id):

    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api)
    request = youtube.channels().list(
        part='statistics',
     id=id
    )
    resp = request.execute()
    stats = resp['items'][0]['statistics']
    if stats['hiddenSubscriberCount']:
        stats['subscriberCount'] = 0
    return stats

def get_new_channel_info(id): #function for getting info needed to add a new channel to our dataset
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api)
    request = youtube.channels().list(
        part='statistics, snippet',
     id=id
    )
    resp = request.execute()
    stats = resp['items'][0]['statistics']
    snippet = resp['items'][0]['snippet']
    return snippet, stats
def get_video_stats(id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api)
    request = youtube.videos().list(
        part='statistics',
     id=id
    )
    resp = request.execute()
    stats = resp['items'][0]['statistics']
    return stats
def get_new_video_info(id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api)
    request = youtube.videos().list(
        part='statistics, snippet',
     id=id
    )
    resp = request.execute()
    stats = resp['items'][0]['statistics']
    snippet = resp['items'][0]['snippet']
    return snippet, stats
