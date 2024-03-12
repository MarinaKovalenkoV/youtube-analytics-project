import os
import datetime

import isodate
from googleapiclient.discovery import build
from pprint import pprint

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class PlayList:
    def __init__(self, playlist_id) -> None:
        self.playlist_id = playlist_id
        self.playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                            part='contentDetails',
                                                            maxResults=50,
                                                            ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = youtube.videos().list(part='snippet,contentDetails,statistics',
                                                    id=','.join(video_ids)
                                                    ).execute()

        self.title = self.video_response['items'][0]['snippet']['localized']['title'][0:24]
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'



    @property
    def total_duration(self) -> datetime.timedelta:
        sum_duration = datetime.timedelta(0,0)
        for video in self.video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            sum_duration += duration
        return sum_duration

    def show_best_video(self):
        videos = []
        for video in self.video_response['items']:
            vid_views = video['statistics']['viewCount']

            vid_id = video['id']
            yt_link = f'https://youtu.be/{vid_id}'

            videos.append(
                {
                    'views': int(vid_views),
                    'url': yt_link
                }
            )
            videos.sort(key=lambda vid: vid['views'], reverse=True)
        return f'{videos[0]['url']}'
