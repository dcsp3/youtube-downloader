import os

from tkinter import messagebox
from pytube import YouTube as yt, Playlist


class Youtube:
    def __init__(self, link: str) -> None:
        self.link = link
        self.path = os.getcwd().replace('\\bin', '\\Downloads')
        try:
            self.obj = yt(link)
        except:
            pass

    def get_info(self):
        try:
            messagebox.showinfo('Info', f'Title: {self.obj.title} \n Channel: {self.obj.author} \n Views: {self.obj.views}')
        except:
            messagebox.showerror('Error', 'Please enter a valid url!')

    def download_vid(self):
        try:
            vid = self.obj.streams.get_highest_resolution()
            vid.download(self.path)
            messagebox.showinfo('Success', 'Your file was downloaded succesfully!')
        except:
            messagebox.showerror('Error', 'Please enter a valid url!')

    def download_pl(self):
        try:
            pl = Playlist(self.link)
            for vid in pl.videos:
                vid.streams.get_highest_resolution().download(self.path + f'/{pl.title}')
            messagebox.showinfo('Success', 'Your file was downloaded succesfully!')
        except:
            messagebox.showerror('Error', 'Please enter a valid url!')

    def download_aud(self):
        try:
            vid = self.obj.streams.get_highest_resolution()
            vid.download(self.path)
            title, title_rename = self.path+'/'+vid.title+'.mp4', self.path+'/'+vid.title.replace(' ', '')+'.mp4'
            os.rename(title, title_rename)
            title_rename_f = title_rename.replace('.mp4', '.mp3')
            os.system(f'ffmpeg -i {title_rename} {title_rename_f}')
            os.remove(title_rename)
            messagebox.showinfo('Success', 'Your file was downloaded succesfully!')
        except:
            messagebox.showerror('Error', 'Please enter a valid url!')

    @staticmethod
    def execute(val, obj):
        if val == 1:
            obj.get_info()

        elif val == 2:
            obj.download_aud()

        elif val == 3:
            obj.download_vid()

        elif val == 4:
            obj.download_pl()

        else:
            messagebox.showerror('Error', 'Please select a valid command!')
