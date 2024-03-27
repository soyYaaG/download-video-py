import requests
import os
from uuid import uuid4

from moviepy.editor import VideoFileClip, AudioFileClip


class DataDownload:
    def __init__(self, url_video: str, video_name: str = None, url_audio: str = None, audio_name: str = None) -> None:
        self.url_video: str = url_video
        self.video_name: str = video_name if video_name else f'{uuid4().hex}.mp4'
        self.url_audio: str = url_audio
        self.audio_name: str = audio_name if audio_name else f'{uuid4().hex}.mp3'


class Download:
    def __init__(self) -> None:
        self.__chunk_size = 256

    
    def __remove(self, filename: str):
        if os.path.exists(filename):
            os.remove(filename)


    def __audio(self, url: str, name: str):
        try:
            response = requests.get(url, stream=True)
            with open(name, 'wb') as f:
                for chunk in response.iter_content(chunk_size=self.__chunk_size):
                    f.write(chunk)
        except ValueError as ex:
            print(f'Error al descargar el audio.\n\rError: {ex}')


    def __video(self, url: str, name: str):
        try:
            response = requests.get(url, stream=True)
            with open(name, 'wb') as f:
                for chunk in response.iter_content(chunk_size=self.__chunk_size):
                    f.write(chunk)
        except ValueError as ex:
            print(f'Error al descargar el video.\n\rError: {ex}')


    def __merge_audio_video(self, data_download: DataDownload, new_name: str):
        video = VideoFileClip(data_download.video_name)
        audio = AudioFileClip(data_download.audio_name)

        final_clip = video.set_audio(audio)
        final_clip.write_videofile(new_name)


    def exec(self, data_download: DataDownload, new_name: str):
        self.__video(data_download.url_video, data_download.video_name)

        if data_download.url_audio:
            self.__audio(data_download.url_audio, data_download.audio_name)
            self.__merge_audio_video(data_download, new_name)
            self.__remove(data_download.audio_name)

        self.__remove(data_download.video_name)