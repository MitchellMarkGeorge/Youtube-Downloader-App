import pytube
from pytube import exceptions
import tkinter
from tkinter import messagebox
import os


height = 140
width = 300



def youtube_video():

    # Setting up variables
    link = youtube_entry.get()
    yt = None
    # Checking invalid URL entry
    try:
        yt = pytube.YouTube(link, False)
    except:
        messagebox.showerror('Error', 'URL is invalid')

    # Selelcts the best quality of the required video
    stream = yt.streams.first()

    # Sets path_entry to users home directory + what every sub directory they type in

    save_path = os.path.expanduser('~/') + path_entry.get()

    if not os.path.exists(save_path):
        # Creates a new directory in users home directory if the current path provided dosent exist
        os.makedirs(save_path)

    #     If program hangs for a bit, it is creating a new directory (look in home directory to find it)


    # Downloads actual video and displays message
    try:
        print('Trying to download ', str(yt.title))
        stream.download(save_path)
        on_complete()
    #
    except FileNotFoundError:
        messagebox.showerror('Error', 'Invalid Path Given')

    # Error handling - if not bale to download video
    except exceptions.PytubeError:
        messagebox.showerror('Error', 'Not able to download video')



# Messgae box if video is downloaded sucessfully
def on_complete():
    messagebox.showinfo('Complete', 'Video download complete')


# GUI for App
root = tkinter.Tk()

root.title('Youtube Downloader')

canvas = tkinter.Canvas(root, height=height, width=width)
canvas.pack()

frame = tkinter.Frame(root)
frame.place(relwidth=1, relheight=1)

youtube_label = tkinter.Label(frame, text='Youtube Link:')
youtube_label.place(relx=0.1, rely=0.1)

youtube_entry = tkinter.Entry(frame)
youtube_entry.place(relx=0.5, rely=0.1)


path_label = tkinter.Label(frame, text='Path Link:')
path_label.place(relx=0.1, rely=0.4)

path_entry = tkinter.Entry(frame)
path_entry.place(relx=0.5, rely=0.4)

download_button = tkinter.Button(frame, text='Download', command=youtube_video)
download_button.place(relx=0.4, rely=0.7)

root.resizable(False, False)
root.mainloop()