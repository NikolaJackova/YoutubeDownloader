import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox
from enum import Enum
from downloader import YoutubeDownloader

def create_widgets():
    tk.Label(root, text="Link: ", font="Arial 14").grid(row=0)
    linkEntry = tk.Entry(root, width=40, textvariable=video_link)
    linkEntry.grid(row=0, column=1, columnspan=2, pady=10, padx=10)

    tk.Label(root, text="Destination: ", font="Arial 14").grid(row=1)
    destinationEntry = tk.Entry(root, width=40, textvariable=download_path)
    destinationEntry.grid(row=1, column=1, columnspan=2)

    Combobox(root, textvariable=combobox_var, values=list(format_enum.__members__), state="readonly").grid(row=2, columnspan=2)

    tk.Button(root, text="Browse", command=browse).grid(row=1, column=3, padx=10, pady=10)
    tk.Button(root, text="Download", command= lambda: downloader.download(video_link.get(), download_path.get(), combobox_var.get()), width=20).grid(columnspan=4, padx=10, pady=10)

def browse():
    download_directory = filedialog.askdirectory(title="Save file", initialdir="C:")
    download_path.set(download_directory)

format_enum = Enum(value="FormatEnum", names="MP3 MP4")
downloader = YoutubeDownloader()

root = tk.Tk()
root.title("Youtube Downloader")
root.geometry("500x250")
root.resizable(False, False)

combobox_var = tk.StringVar(value=format_enum.MP3.name)
video_link = tk.StringVar()
playlist_list = tk.StringVar()
download_path = tk.StringVar()

create_widgets()
tk.mainloop() 