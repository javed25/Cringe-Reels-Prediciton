from moviepy.editor import *
import os

path = "C:\\Users\\khana_asisvkp\\Documents\\SAMPLES"

for file in os.listdir(path):
    a=file.split(".mp4")

    video = VideoFileClip(f"C:\\Users\\khana_asisvkp\\Documents\\SAMPLES\\{file}")
    audio = video.audio
    audio.write_audiofile(f"D:\\audios\\{a[0]}.mp3")