from tkinter import *
from login import open_login


def show_splash(root):

    root.state("zoomed")
    root.configure(bg="black")

    frame = Frame(root, bg="black")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    logo = PhotoImage(file="C:/Users/upadh/OneDrive/Desktop/python-4th sem/crime reporting and tracking system/crime_logo.png")
    logo = logo.subsample(2, 2)

    logo_label = Label(frame, image=logo)
    logo_label.pack(pady=20)
    frame.logo = logo   

    title = Label(frame,text="CRIME SE SURAKSHA",font=("Arial", 36, "bold"),fg="red",bg="black")
    title.pack(pady=10)

    Label(frame,text="Crime Reporting and Tracking System",font=("Arial", 18),fg="white",bg="black").pack()

    def flash():
        current = title.cget("fg")
        title.config(fg="white" if current == "red" else "red")
        root.after(500, flash)

    flash()

    def go_to_login():
        root.withdraw()   
        open_login(root)  
    root.after(3000, go_to_login)

root = Tk()
show_splash(root)
root.mainloop()