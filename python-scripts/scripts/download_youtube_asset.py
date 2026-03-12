
from yt_dlp import YoutubeDL
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# git clean -fx john-vegas/assets/
# git clean -fx ../john-vegas/assets/
# uv run download-vegas.py

# from converter import Converter
# https://pypi.org/project/moviepy/

import os

_dir = os.path.dirname(__file__)
_assets_dir = os.path.abspath(os.path.join(_dir, '../../john-vegas/assets'))



def _mp4_to_mp3(mp4_filename, mp3_filename):
    mp4_video = VideoFileClip(mp4_filename)

    mp4_video.audio.write_audiofile(mp3_filename)


def _download_mp4(url, name):
    mp4_filename = os.path.abspath(os.path.join(_assets_dir,f'{name}.mp4'))

    if os.path.isfile(mp4_filename):
        return mp4_filename
    

    # def yt_dlp_monitor(self, d):
    #     final_filename  = d.get('info_dict').get('_filename')
    #     print('yt_dlp_monitor',final_filename)
        # You could also just assign `d` here to access it and see all the data or even `print(d)` as it updates frequently

    # https://stackoverflow.com/questions/74157935/getting-the-file-name-of-downloaded-video-using-yt-dlp
    ydl_opts = {
        "outtmpl": f'{_assets_dir}/{name}.%(ext)s'
        # "outtmpl": '/whatever/directory/%(uploader)s_%(title)s.%(ext)s',  # this is where you can edit how you'd like the filenames to be formatted
        # "progress_hooks": [yt_dlp_monitor]  # here's the function we just defined
        }

    with YoutubeDL(ydl_opts) as ydl:
        # downloaded = ydl.download(url)
        # info = ydl.extract_info(url)
        # print(info)
        # print(ydl.get(''))
        # print(ydl.post_extract)
        info_dict = ydl.extract_info(url, download=True)
        output_filename = ydl.prepare_filename(info_dict)
        print(f"downloaded {output_filename}")

    return mp4_filename


# PYTHONPATH=. uv run scripts/download_baby_stocks.py 
def download_youtube_asset(url, name):
    mp4_filename = _download_mp4(url, name)
    mp3_filename = os.path.abspath(os.path.join(_assets_dir,f'{name}.mp3'))

    mp4_video = VideoFileClip(mp4_filename)

    _mp4_to_mp3(mp4_filename, mp3_filename)

    return mp4_video

