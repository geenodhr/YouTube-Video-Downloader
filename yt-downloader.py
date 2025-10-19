import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests
from PIL import Image, ImageTk
import yt_dlp
import threading
# import time
# import subprocess
# from pathlib import Path

class VideoDownloaderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("YouTube Video Downloader")
        # self.master.geometry("400x400")
        self.master.minsize(width=400, height=400)

        self.video_url = tk.StringVar()
        self.selected_resolution = tk.StringVar()
        self.download_directory = ""

        # Video URL input
        ttk.Label(master, text="Video URL:").pack(pady=5)
        self.url_entry = ttk.Entry(master, textvariable=self.video_url, width=50)
        self.url_entry.pack(pady=5)

        # Load button
        self.load_button = ttk.Button(master, text="Load Video", command=self.load_video)
        self.load_button.pack(pady=5)

        # Thumbnail and title display
        self.thumbnail_label = ttk.Label(master)
        self.thumbnail_label.pack(pady=5)
        self.title_label = ttk.Label(master, text="", font=("Calibri", 12))
        self.title_label.pack(pady=5)

        # Resolution dropdown
        self.resolution_label = ttk.Label(master, text="Select Resolution:")
        self.resolution_label.pack(pady=5)
        self.resolution_dropdown = ttk.Combobox(master, textvariable=self.selected_resolution)
        self.resolution_dropdown.pack(pady=5)

        # Destination button
        self.dest_button = ttk.Button(master, text="Select Destination", command=self.select_destination)
        self.dest_button.pack(pady=5)
        self.dest_label = tk.Label(self.master, text="No directory selected.")
        self.dest_label.pack(pady=10)

        # Download button
        self.download_button = ttk.Button(master, text="Download Video", command=self.download_video)
        self.download_button.pack(pady=5)

        # Progress bar
        style = ttk.Style()
        style.configure("grey.Horizontal.TProgressbar", background="grey")
        style.configure("green.Horizontal.TProgressbar", background="green")
        style.configure("blue.Horizontal.TProgressbar", background="blue")
        style.configure("red.Horizontal.TProgressbar", background="red")

        # Set the initial style of the progress bar
        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode="determinate", style="grey.Horizontal.TProgressbar")
        self.progress_bar.pack(pady=10)
        self.status_label = tk.Label(self.master, text="")
        self.status_label.pack(pady=10)

    def load_video(self):
      url = self.video_url.get()
      if url:
          ydl_opts = {
              'format': 'best',
              'noplaylist': True
          }

          # Fetch video information
          with yt_dlp.YoutubeDL(ydl_opts) as ydl:
              try:
                  info_dict = ydl.extract_info(url, download=False)
                  title = info_dict.get('title', None)
                  thumbnail = info_dict.get('thumbnail', None)
                  formats = info_dict.get('formats', [])

                  self.title_label.config(text=title)

                  if thumbnail:
                      response = requests.get(thumbnail)
                      img_data = Image.open(requests.get(thumbnail, stream=True).raw)
                      img = img_data.resize((200, 150), Image.LANCZOS)
                      img = ImageTk.PhotoImage(img)
                      self.thumbnail_label.config(image=img)
                      self.thumbnail_label.image = img

                  resolutions = sorted(set(f['height'] for f in formats if f.get('height') is not None))
                  self.resolution_dropdown['values'] = resolutions
                  if resolutions:
                      self.resolution_dropdown.current(0)

              except Exception as e:
                  messagebox.showerror("Error", f"Failed to load video: {str(e)}")

    def select_destination(self):
        self.download_directory = filedialog.askdirectory()
        if self.download_directory:
            self.dest_label.config(text="Directory set to " + self.download_directory)

    def download_video(self):
        if not self.video_url.get() or not self.download_directory:
            messagebox.showerror("Error", "Please enter a video URL and select a download destination.")
            return

        url = self.video_url.get()
        resolution = self.selected_resolution.get()
        # output_path = os.path.join(self.download_directory, "%(title)s.%(ext)s")
        output_path = os.path.join(self.download_directory, "%(title)s.mp4")
        threading.Thread(target=self.download_thread, args=(url, resolution, output_path)).start()

    def download_thread(self, url, resolution, output_path):
        self.status_label.config(text="Loading...")
        self.progress_bar.config(style="grey.Horizontal.TProgressbar")

        ydl_opts = {
            # 'format': f"bestvideo[height<={resolution}]+bestaudio/best",
            'format': f"bestvideo[ext=mp4][height<={resolution}]+bestaudio[ext=m4a]/best[ext=mp4]",
            'outtmpl': output_path,
            'progress_hooks': [self.progress_hook],
            # 'postprocessors': [{
            #     'key': 'FFmpegVideoConvertor',
            #     'preferedformat': 'mp4'  
            # }],
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
            except Exception as e:
                self.status_label.config(text="Error during download")
                self.progress_bar.config(style="red.Horizontal.TProgressbar")
                self.progress_bar['value'] = 100

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            if d.get('total_bytes') and d.get('downloaded_bytes'):
                percent = int(d['downloaded_bytes'] / d['total_bytes'] * 100)
                self.progress_bar['value'] = percent
                self.status_label.config(text="Downloading...")
                self.progress_bar.config(style="green.Horizontal.TProgressbar")  
                self.master.update_idletasks()

        elif d['status'] == 'finished':
            self.status_label.config(text="Download Complete!")
            self.progress_bar.config(style="blue.Horizontal.TProgressbar")  
            self.progress_bar['value'] = 100
                
if __name__ == "__main__":
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()