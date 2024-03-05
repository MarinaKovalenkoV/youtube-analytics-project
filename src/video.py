import json
import os
from googleapiclient.discovery import build

api_key: str = os.getenv('YT_API_KEY')


class Video:

    def __init__(self, video_id) -> None:
        self.__video_id = video_id  # id видео
        self.video_response = build('youtube', 'v3', developerKey=api_key).videos().list(
            part='snippet,statistics,contentDetails,topicDetails',
            id=video_id
            ).execute()

    @property
    def _video_id(self):
        return self.__video_id

    @_video_id.setter
    def _video_id(self, id):
        self.__video_id = id
        return self.__video_id

    @property
    def video_title(self):  # название видео
        self._video_title: str = self.video_response['items'][0]['snippet']['title']
        return self._video_title


    def print_info(self):
        print(self.video_response)

    @property
    def video_url(self):  # ссылка на видео
        self.video_url: str = self.video_response['items'][0]['snippet']['title']
        return self.video_url

    @property
    def view_count(self):  # количество просмотров
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
        return self.view_count

    @property
    def like_count(self):  # количество лайков
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        return self.like_count

    def __str__(self):
        return f"{self.video_title}"

class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
