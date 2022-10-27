from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
import csv

try:
    api_key = open('api_key.txt', 'r').read()
except FileNotFoundError:
    print('api_key.txt not found')

class api:

    def get_channel_id(url):

        youtube = build('youtube', 'v3', developerKey=api_key)

        request = youtube.search().list(
            part='id',
            type='channel',
            q=url

        ).execute()

        items = request['items']

        channel_id = items[0]['id']['channelId']

        return channel_id

    def get_videos_id(channel_id):

        youtube = build('youtube', 'v3', developerKey=api_key)

        request = youtube.search().list(
            part='id',
            channelId=channel_id,
            maxResults=50,
            order='date'
        ).execute()

        items = request['items']

        video_ids = []

        for item in items:
            if "videoId" in item['id']:
                video_ids.append(item['id']['videoId'])
        
        return video_ids

    def get_category(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        category = soup.find('meta', {'itemprop':"genre"})['content']
        return category

    def transcript(url):
        df = []
        for id in api.get_videos_id(api.get_channel_id(url)):
            try:
                srt = YouTubeTranscriptApi.get_transcript(id, languages=[languages])
                fala = []
                for i in srt:
                    fala.append(i['text'])
                fala = ' '.join(fala)
                cat = api.get_category('https://www.youtube.com/watch?v='+id)
                lista = [id, fala, cat]
                df.append(lista)
            except:
                pass
        return df

languages = input('Enter the language: ')

url = input('Enter the channel url: ')

list = api.transcript(url)

fields = ['video_id', 'transcript', 'category']

with open('list', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(list)