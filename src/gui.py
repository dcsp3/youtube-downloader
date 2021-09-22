import tkinter as tk

from youtube import Youtube


root = tk.Tk()
root.resizable(False, False)
root.title('Youtube Downloader')
root.iconbitmap('icon.ico')

canvas = tk.Canvas(root, height=400, width=800, bg='black')
canvas.pack()

# Main Window
main_frame = tk.Frame(root, bg='#FF7276')
main_frame.place(relx=.5, rely=.025, relwidth=.98, relheight=.95, anchor='n')

# URL Frame
url_frame = tk.Frame(root)
url_frame.place(relx=.5, rely=.1, relwidth=.7, relheight=.7, anchor='n')

url_label = tk.Label(url_frame, text='URL', fg='black')
url_label.config(font=("Times New Roman", 15))
url_label.place(relx=.05, rely=.05, relwidth=.1, relheight=.1, anchor='n', height=1, width=1)

# URL Entry
url_entry = tk.Entry(url_frame, bd=5)
url_entry.place(relx=.55, rely=.03, relwidth=.9, relheight=.13, anchor='n')

r = tk.IntVar()

# Radio button 2
option1 = tk.Radiobutton(url_frame, text='Get Info', variable=r, value=1, indicatoron=20)
option1.config(font=('', 25))
option1.place(relx=.403, rely=.25, relwidth=.9, relheight=.13, anchor='n')

# Radio button 2 
option2 = tk.Radiobutton(url_frame, text='Download Audio', variable=r, value=2, indicatoron=1)
option2.config(font=('', 25))
option2.place(relx=.505, rely=.4, relwidth=.9, relheight=.13, anchor='n')

# Radio button 3
option3 = tk.Radiobutton(url_frame, text='Download Video', variable=r, value=3, indicatoron=1)
option3.config(font=('', 25))
option3.place(relx=.505, rely=.55, relwidth=.9, relheight=.13, anchor='n')

# Radio button 4
option4 = tk.Radiobutton(url_frame, text='Download Playlist', variable=r, value=4, indicatoron=1)
option4.config(font=('', 25))
option4.place(relx=.521, rely=.7, relwidth=.9, relheight=.13, anchor='n')


def out() -> None:
    """
    Outputs command to be executed.
    """
    yt = Youtube(url_entry.get())
    Youtube.execute(r.get(), yt)

# Download Button
dl_button = tk.Button(main_frame, text='GO', font=40, bg='black', fg='white', command=lambda: out())
dl_button.place(relx=.5, rely=.85, relwidth=.2, relheight=.1, anchor='n')

root.mainloop()
