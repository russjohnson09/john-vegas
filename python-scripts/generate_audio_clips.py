

from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import pandas as pd
import pathlib

import os
_dir = os.path.dirname(__file__)

_assets_dir = os.path.abspath(os.path.join(_dir, '../john-vegas/assets'))
# os.chdir(_assets_dir)
_john_vegas_mp4 = os.path.abspath(os.path.join(_assets_dir, "Cool Protagonist for Your Video Game (Free to Use Audio) [clnrrJOmfPk].mp4")) 

def _get_timing(file_path):
    df = pd.read_csv(file_path, keep_default_na=False)

    dict_output = df.to_dict(orient="index")

    print(dict_output)
    # tests\test_font.py {0: {'start': 1000, 'text': 'PRESS'}, 1: {'start': 2000, 'text': ''}, 2: {'start': 3000, 'text': 'ZIP'}}
    
    result = []
    for key in list(dict_output.keys()):
        row = dict_output[key]
        result.append(row)

    print(result)
    return result


def _make_path_directory(filepath):
    dir_path = os.path.dirname(filepath)
    print(f'make directory if not exists {dir_path}')
    pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True) 


def _get_mp3_filename(text: str):

    filename = text

    filename = f'{filename}.mp3'
    
    
    return os.path.abspath(os.path.join(_assets_dir, './john_vegas_audio', filename)) 


def _save_mp3_from_timing_array(video: VideoFileClip, timing_array):


    count = 0
    for timing in timing_array:
        count += 1
        print(timing)

        filepath = _get_mp3_filename(f'{count}. {timing.get('text')}')

        clipped_video = video.subclipped(timing.get('start'), timing.get('end'))

        _make_path_directory(filepath)
        clipped_video.audio.write_audiofile(filepath)

def main():

    print(_get_mp3_filename("The name's john vegas"))


    timing_array = _get_timing(os.path.dirname(__file__) + '/john_vegas.csv')

    # df = pd.read_csv(, keep_default_na=False)
    # dict_output = df.to_dict(orient="index")
    print(timing_array)

    original_video = VideoFileClip(_john_vegas_mp4)
    # # TODO load in a csv with the start and endpoints for the lines being spoken.
    # # https://stackoverflow.com/questions/68399696/moviepy-extracting-audio-from-a-video-and-using-it-in-another-video
    video = VideoFileClip(_john_vegas_mp4).subclipped(10, 20)
    
    
    # video = original_video.subclipped(0, 5)


    # original_video.audio.write_audiofile("audio.mp3")
    # original_video.audio.write_audiofile("audio.wav")

    print(video)


    _save_mp3_from_timing_array(original_video,timing_array)

    pass


main()





#https://stackoverflow.com/questions/55582117/efficiently-converting-color-to-transparency-in-python