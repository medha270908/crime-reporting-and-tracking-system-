from tkinter import *

def open_track_page():
    win = Toplevel()
    win.title("Track Crime")
    win.geometry("500x400")

    Label(win, text="Track Crime Page",
          font=("Arial", 18)).pack(pady=50)