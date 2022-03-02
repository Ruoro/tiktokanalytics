# import TikTokApi sdk
from TikTokApi import TikTokApi 
# the json is for the export of data 
# import json

api = TikTokApi()

for video in api.trending.videos():
    print(video.author.username)