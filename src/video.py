import json
import os
from pprint import pprint

from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

class Video:

    def __init__(self, video_id) -> None:
        self.__video_id = video_id  # id видео
        self.video_response = youtube.videos().list(part='snippet,statistics', id=video_id).execute()
        self.item = self.video_response['items'][0]['snippet']
        self.count = self.video_response['items'][0]['statistics']

    @property
    def _video_id(self):
        return self.__video_id

    @_video_id.setter
    def _video_id(self, id):
        self.__video_id = id
        return self.__video_id

    @property
    def video_title(self):  # название видео
        return self.item['title']


    def print_info(self):
        print(self.video_response)

    @property
    def video_url(self):  # ссылка на видео
        return self.item['thumbnails']['default']['url']

    @property
    def view_count(self):  # количество просмотров
        return int(self.count['viewCount'])

    @property
    def like_count(self):  # количество лайков
        return int(self.count['likeCount'])

    def __str__(self):
        return f"{self.video_title}"

class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
