from yt_dlp import YoutubeDL
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# git clean -fx john-vegas/assets/
# git clean -fx ../john-vegas/assets/
# uv run download-vegas.py

# from converter import Converter
# https://pypi.org/project/moviepy/

import os

URLS = [
    "https://www.youtube.com/watch?v=clnrrJOmfPk"
        ]


_dir = os.path.dirname(__file__)

print(_dir)

_assets_dir = os.path.abspath(os.path.join(_dir, '../john-vegas/assets'))
os.chdir(_assets_dir)

_john_vegas_mp4 = os.path.abspath(os.path.join(_assets_dir, "Cool Protagonist for Your Video Game (Free to Use Audio) [clnrrJOmfPk].mp4")) 


if not os.path.isfile(_john_vegas_mp4):
    downloaded = []
    with YoutubeDL() as ydl:
        downloaded = ydl.download(URLS)


original_video = VideoFileClip(_john_vegas_mp4)

# TODO load in a csv with the start and endpoints for the lines being spoken.
# https://stackoverflow.com/questions/68399696/moviepy-extracting-audio-from-a-video-and-using-it-in-another-video
# video = VideoFileClip(_john_vegas_mp4).subclipped(10, 20)
video = original_video.subclipped(0, 5)
video.audio.write_audiofile("audio.mp3")
video.audio.write_audiofile("audio.wav")

print(video)
# print("move to assets", type(downloaded), downloaded)

john_vegas_png = os.path.abspath(os.path.join(_assets_dir, "john_vegas.png")) 
john_vegas_trans_png = os.path.abspath(os.path.join(_assets_dir, "john_vegas_trans.png")) 
video.save_frame(john_vegas_png)

import pyvips 


image = pyvips.Image.new_from_file(john_vegas_png, access='sequential')
# Color to make transparent
col = [255,255,255]

# Tolerance ... ie., how close to target before we become solid
tol = 25

# for each pixel, pythagorean distance from target colour
d = sum(((image - col) ** 2).bandsplit()) ** 0.5

# scale d so that distances > tol become 255
alpha = 255 * d / tol

# https://pypi.org/project/pyvips/
# attach the alpha and save

# OSError: cannot load library 'libvips-42.dll': error 0x7e.  Additionally, ctypes.util.find_library() did not manage to locate a library called 'libvips-42.dll'
image.bandjoin(alpha).write_to_file(john_vegas_trans_png)




#https://stackoverflow.com/questions/55582117/efficiently-converting-color-to-transparency-in-python