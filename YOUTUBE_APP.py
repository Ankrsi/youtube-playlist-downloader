import tkinter
import pytube
import os
import threading

d=["YOUTUBE_DOWNLOAD"]
list=os.listdir("C:")
if(d[0] not in list):
    os.mkdir("C:/YOUTUBE_DOWNLOAD")

def tube():
    try:
        Text = text.get()
        vl=pytube.Playlist(Text)
        for i in vl:
            v=pytube.YouTube(i)
            d=v.streams.get_highest_resolution()
            mes="downloading"
            lab.config(text=mes)
            txt.config(state=tkinter.NORMAL)
            d.download("C:/YOUTUBE_DOWNLOAD")
            txt.insert(tkinter.END,i+"\n")
            txt.config(state=tkinter.DISABLED)
        mess="downloaded"
        lab.config(text=mess)
    except Exception:
        mesg=("not downloaded")
        lab.config(text=mesg)
try:
    window=tkinter.Tk()
    window.config(bg='blue')
    window.title("YOUTUBE DOWNLODER")
    window.geometry("700x700")
    text=tkinter.Entry(window,width=80)
    text.place(x=60,y=25,height=30)
    button=tkinter.Button(window, width=11, text="click here", command=tube)
    button.place(x=250,y=70)
    lab=tkinter.Label(window,text="Wellcome",bg='red',width=20)
    lab.place(x=70,y=650)
    txt=tkinter.Text(window)
    txt.place(x=8,y=100)
    txt.pack(fill=tkinter.X,expand=1)
    txt.config(state=tkinter.DISABLED)
    window.mainloop()
except Exception:
    print("app not run"+str(Exception))

t=threading.Thread(target=tube())
t.start()
t1=threading.Thread(target=tube())
t1.start()