import json
import os
from googleapiclient.discovery import build

# создание апи ключа
api_key: str = os.getenv('YT_API_KEY')

# создаем переменную для получения данных с ютуб
youtube = build('youtube', 'v3', developerKey=api_key)

url = 'https://developers.google.com/youtube/v3/docs/channels/list'
channel_id = 'UCDBOWnTdpOOD-hoTcBGTkmQ'
ch_request = youtube.channels().list(id=channel_id, part='snippet,statistics')
ch_response = ch_request.execute()


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


print(ch_response)

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics')
        return printj(channel)



