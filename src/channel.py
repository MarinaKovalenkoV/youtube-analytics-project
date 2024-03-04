import json
import os
from googleapiclient.discovery import build
from pprint import pprint

# создание апи ключа
api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id  # id каннала
        self.channel = build('youtube', 'v3', developerKey=api_key).channels().list(id=self.channel_id, part='snippet,statistics').execute()

    @property
    def channel_id(self):
        return self._channel_id

    @property
    def title(self):
        self._title: str = self.channel['items'][0]['snippet']['title']
        return self._title # название канала

    @property
    def description(self):
        self._description: str = self.channel['items'][0]['snippet']['description']
        return self._description # описание канала

    @property
    def url(self):
        self._url = self.channel['items'][0]['snippet']['thumbnails']["default"]['url']
        return self._url  # ссылка на канал

    @property
    def subscriber_сount(self):
        self._subscriber_сount: int = self.channel['items'][0]['statistics']['subscriberCount']
        return self._subscriber_сount  # кол-во подписчиков

    @property
    def video_count(self):
        self._video_count: int = self.channel['items'][0]['statistics']['videoCount']
        return self._video_count # кол-во видео

    @property
    def view_сount(self):
        self._view_сount: int = self.channel['items'][0]['statistics']['viewCount']
        return self._view_сount  # общее число просмотров


    def print_info(self):
        """Выводит в консоль информацию о канале."""
        pprint(self.channel)

    @classmethod
    def get_service(cls):
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


    def to_json(self, name):
        """Создает файл с данными по каналу в json-подобном формате"""
        i = self.channel
        with open(name, 'w') as f:
            return json.dump(i, f)
