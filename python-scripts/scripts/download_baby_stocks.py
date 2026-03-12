from scripts.download_youtube_asset import download_youtube_asset
from scripts.save_mp3_from_timing_array import save_mp3_from_timing_array


# create mp4 + mp3
original_video = download_youtube_asset("https://www.youtube.com/watch?v=lkJkPhuTCco", 'short_baby')


save_mp3_from_timing_array(original_video,timing_array)
