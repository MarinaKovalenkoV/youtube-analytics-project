import json
import os
from googleapiclient.discovery import build

# создание апи ключа
api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id  # id каннала
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
