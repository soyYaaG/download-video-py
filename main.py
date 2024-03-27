from moviepy.editor import *

from download import DataDownload, Download


def run():
    download = Download()

    video1 = DataDownload(
        url_video='',
        url_audio=''
    )

    download.exec(video1, 'clase1.mp4')


if __name__ == '__main__':
    run()