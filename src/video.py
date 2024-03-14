import json
import os
from pprint import pprint

from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Video:

    def __init__(self, video_id) -> None:
        self.__video_id = video_id  # id видео
        try:
            self.video_response = youtube.videos().list(part='snippet,statistics', id=video_id).execute()
            self.count = self.video_response['items'][0]['statistics']
            self.title = self.video_response['items'][0]['snippet']['title']
            self.url = f'https://www.youtube.com/watch?v={self.__video_id}'
            self.view_count = int(self.count['viewCount'])
            self.like_count = int(self.count['likeCount'])
        except IndexError:
            self.video_response = None
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None


    @property
    def _video_id(self):
        return self.__video_id

    @_video_id.setter
    def _video_id(self, id):
        self.__video_id = id
        return self.__video_id

    def print_info(self):
        print(self.video_response)

    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
