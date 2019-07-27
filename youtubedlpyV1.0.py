################################################################################
#Youtube Downloader
#Version : v1.0
#Using : youtube-dl | tkinter
#built on 27/07/2019
#Author : Auto5k
################################################################################

import youtube_dl
import tkinter as tk
from tkinter import filedialog

rootframecolor = '#FFFFFF'
path = '' #Default Path, downloads where program is executed
url = ''

def directory(): #Promp for selecting download target
    global path
    path = filedialog.askdirectory()
    path_entry_text.set(path)

def clear_entry(event):
    url_entry.delete(0, tk.END)

def music_dl(): #Function for downloading
    url = url_entry.get()
    print(url)
    ydl = youtube_dl.YoutubeDL()
    info_dict = ydl.extract_info(url, download=False)
    title = info_dict.get('title') + '.mp3'

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': path + '/' + title
        }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    info_dict = ydl.extract_info(url, download=True)

#root Tkinter windows
gui = tk.Tk()
gui.resizable(0, 0)
gui.title("Youtube MP3 Downloader")
rootframe = tk.Frame(bg=rootframecolor)
rootframe.pack()
###Frame 1 for Label############################################################
frame1 = tk.Frame(master=rootframe, bd=0, bg=rootframecolor)
frame1.pack()
label1 = tk.Label(master=frame1,
text="Youtube MP3 Downloader",
font=("Arial", 18),
bg=rootframecolor
)
label1.pack(pady=(20, 10))
###frame2 for Entry#############################################################
frame2 = tk.Frame(master=rootframe, bd=10, bg=rootframecolor)
frame2.pack()
url_entry = tk.Entry(frame2, justify="center", width=50, bd=1, relief="solid")
url_entry.insert(0, 'Enter URL here')
url_entry.bind("<Button-1>", clear_entry)
url_entry.pack()
###frame3 for path selection and download button################################
frame3 = tk.Frame(master=rootframe, bd=10, bg=rootframecolor, width=50)
frame3.pack(fill='both', expand=1)
path_entry_text = tk.StringVar()

path_display = tk.Entry(frame3, textvariable=path_entry_text, bd=1, relief="solid", bg=rootframecolor)
path_display.configure(state='readonly')
button0 = tk.Button(frame3, command=directory, text='PATH', bd=1, relief="solid", bg=rootframecolor)
button1 = tk.Button(frame3, command=music_dl, text='Download', bd=1, relief="solid", bg=rootframecolor)

path_display.pack(side='left', pady=(0, 15), fill='both', expand=1)
button0.pack(side='left', pady=(0,15), padx=(0,10))
button1.pack(side='right', pady=(0, 15))

gui.mainloop()
