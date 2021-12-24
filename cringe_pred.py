from tkinter import *
from tkinter import filedialog
import os
from moviepy.editor import *
from pydub import AudioSegment
import librosa
import numpy as np
from keras.models import load_model
from tkinter import messagebox


function = load_model("model.h5")

def cons():
    global temp,temp1
    temp = s.get().split("/")[-1]
    temp1 = temp.split(".mp4")

def v2a():
    video = VideoFileClip(f"C:\\Users\\khana_asisvkp\\Documents\\test\\mp4\\{temp}")
    audio = video.audio
    audio.write_audiofile(f"C:\\Users\\khana_asisvkp\\Documents\\test\\mp3\\{temp1[0]}.mp3")
    for item in os.listdir("C:\\Users\\khana_asisvkp\\Documents\\test\\mp3"):
        if temp1[0] in item:
            a=item.split(".mp3")
            AudioSegment.ffmpeg = "C:\\path_ffmpeg\\ffmpeg.exe"
            audio = AudioSegment.from_mp3(f"C:\\Users\\khana_asisvkp\\Documents\\test\\mp3\\{item}")
            audio.export(f"C:\\Users\\khana_asisvkp\\Documents\\test\\wav\\{a[0]}.wav",format='wav')

def feature(path):
    data , sr = librosa.load(path)
    mfccs = librosa.feature.mfcc(y=data,sr=sr,n_mfcc=40)
    mfccs_features = np.mean(mfccs.T,axis=0)
    return mfccs_features


def get_data():
    global data
    d=[]
    for item in os.listdir(f"C:\\Users\\khana_asisvkp\\Documents\\test\\wav"):
        if temp1[0] in item:
            temp2 = feature(f"C:\\Users\\khana_asisvkp\\Documents\\test\\wav\\{item}")
            d.append(temp2)
            data=np.array(d)


root=Tk()
root.title("Cringe Prediction")
root.geometry("650x400")
root.config(bg="black")
root.resizable(width=False, height=False)

def browse():
    r=filedialog.askopenfile(title="Select Video File",initialdir="C:\\Users\\khana_asisvkp\\Documents\\test\\mp4",
    filetypes=(("video",".mp4"),("images",".jpg"),("all files",".*")))
    s.set(r.name)

def clear():
    s.set("")

def play():
    os.startfile(s.get())

def go():
    global result,per
    cons()
    v2a()
    get_data()
    prediction = function.predict(data)
    if prediction >= 0.5:
        result = "CRINGE"
        per = prediction*100
    else:
        result = "NOT CRINGE"
        per = (1 - prediction)*100

    l1.config(text=f"{result} {int(per)}%")
    messagebox.showinfo("Cringe Prediction Result",f"{result} {int(per)}%")

Label(root,text="VIDEO PATH ",fg="#03fcf8",bg="black",padx=20,font=("arial",26,"bold")).place(x=200,y=50)
l1 = Label(root,text="",fg="white",bg="black",padx=20,font=("arial",29,"bold"))
l1.place(x=155,y=340)
global s
s=StringVar()
text=Entry(root,width=66,font=("",12),bg="white",fg="#161e45",textvariable=s)
text.place(x=25,y=125)

b1=Button(root,text="BROWSE",width=15,font=("",16,"bold"),bg="red",fg="black",command=browse)
b1.place(x=220,y=180)

b2=Button(root,text="G0",width=9,font=("",16,"bold"),bg="#fcba03",fg="black",command=go)
b2.place(x=50,y=250)

b3=Button(root,text="CLEAR",width=9,font=("",16,"bold"),bg="#fcba03",fg="black",command=clear)
b3.place(x=250,y=250)

b4=Button(root,text="PLAY",width=9,font=("",16,"bold"),bg="#fcba03",fg="black",command=play)
b4.place(x=450,y=250)


root.mainloop()