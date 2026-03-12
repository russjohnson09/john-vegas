
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


# PYTHONPATH=. uv run scripts/download_baby_stocks.py 
def download_youtube_asset(url):


    # print(_dir)

    # os.chdir(_assets_dir)

    # _john_vegas_mp4 = os.path.abspath(os.path.join(_assets_dir, "Cool Protagonist for Your Video Game (Free to Use Audio) [clnrrJOmfPk].mp4")) 

    final_filename = None

    # def yt_dlp_monitor(self, d):
    #     final_filename  = d.get('info_dict').get('_filename')
    #     print('yt_dlp_monitor',final_filename)
        # You could also just assign `d` here to access it and see all the data or even `print(d)` as it updates frequently

    # https://stackoverflow.com/questions/74157935/getting-the-file-name-of-downloaded-video-using-yt-dlp
    ydl_opts = {
        "outtmpl": f'{_assets_dir}/%(uploader)s_%(title)s.%(ext)s'
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

    # print(final_filename)

    pass