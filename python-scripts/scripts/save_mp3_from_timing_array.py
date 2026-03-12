
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import pandas as pd
import pathlib

import os
_dir = os.path.dirname(__file__)

_assets_dir = os.path.abspath(os.path.join(_dir, '../../john-vegas/assets'))

def _get_timing(file_path):
    df = pd.read_csv(file_path, keep_default_na=False)

    dict_output = df.to_dict(orient="index")

    print(dict_output)
    
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




def save_mp3_from_timing_array(video: VideoFileClip, timing_file, directory):

    def _get_mp3_filename(text: str):

        filename = text

        filename = f'{filename}.mp3'
        
        
        return os.path.abspath(os.path.join(_assets_dir, directory, filename)) 


    timing_array = _get_timing(timing_file)

    count = 0
    for timing in timing_array:
        count += 1
        print(timing)

        filepath = _get_mp3_filename(f'{count}. {timing.get('text')}')

        clipped_video = video.subclipped(timing.get('start'), timing.get('end'))

        _make_path_directory(filepath)
        clipped_video.audio.write_audiofile(filepath)