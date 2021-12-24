import os
from pydub import AudioSegment

path = "D:\\audios"

for item in os.listdir(path):
    AudioSegment.ffmpeg = "C:\\path_ffmpeg\\ffmpeg.exe"
    a = item.split(".mp3")
    audio = AudioSegment.from_mp3(f"D:\\audios\\{item}")
    audio.export(f"D:\\wav_files\\{a[0]}.wav",format='wav')