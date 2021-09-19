import os

from tkinter import messagebox
from pytube import YouTube as yt, Playlist


class Youtube:
    """
    A class to perform YouTube functions.
    """
    def __init__(self, link: str) -> None:
        """
        :param link: link of the url
        """
        self.link = link
        self.path = os.getcwd().replace('\\bin', '\\Downloads')
        try:
            self.obj = yt(link)
        except:
            pass

    def get_info(self) -> None:
        """
        Gets information about the requested url.
        """
        try:
            messagebox.showinfo('Info', f'Title: {self.obj.title} \n Channel: {self.obj.author} \n Views: {self.obj.views}')
        except:
            messagebox.showerror('Error', 'Please enter a valid url!')

    def download_vid(self) -> None:
        """
        Downloads the video from the requested url.
        """
        try:
            vid = self.obj.streams.get_highest_resolution()
            vid.download(self.path)
            messagebox.showinfo('Success', 'Your file was downloaded succesfully!')
        except:
            messagebox.showerror('Error', 'Please enter a valid url!')

    def download_pl(self):
        """
        Downloads the playlist from the requested url.
        """
        try:
            pl = Playlist(self.link)
            for vid in pl.videos:
                vid.streams.get_highest_resolution().download(self.path + f'/{pl.title}')
            messagebox.showinfo('Success', 'Your file was downloaded succesfully!')
        except:
            messagebox.showerror('Error', 'Please enter a valid url!')

    def download_aud(self) -> None:
        """
        Downloads the audio from the requested url.
        """
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
    def execute(val: int, obj) -> None:
        """
        Executes the functions based on values
        :param val: Value of the function
        :param obj: Youtube class object
        """
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
