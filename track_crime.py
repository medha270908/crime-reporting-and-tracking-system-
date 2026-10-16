from tkinter import *
from tkinter import messagebox
import mysql.connector   

def open_track_page(dash,bg="white"):

    track = Toplevel(dash)
    track.title("Track Case")
    track.state("zoomed")

    header = Frame(track, bg="#1f4e79", height=70)
    header.pack(fill=X)
    Label(header, text="Track a Case",bg="#1f4e79", fg="white",font=("Arial", 20, "bold")).pack(pady=15)

    search_frame = Frame(track, bg="#2d6ca2", height=150)
    search_frame.pack(fill=X)

    Label(search_frame, text="Track Case ID",bg="#2d6ca2", fg="white",font=("Arial", 16, "bold")).pack(pady=10)

    entry_id = Entry(search_frame, font=("Arial", 14), width=30)
    entry_id.pack(pady=10)

    status_frame = Frame(track, bg="white")
    status_frame.pack(pady=40)

    status = []
    steps = ["Registered", "In Progress", "Under Investigation", "Resolved"]

    def show_status(current_status):

        current_index = steps.index(current_status)
        i = 0
        for step in steps:
            if i <= current_index:
                color = "green"
            else:
                color = "gray"

            lbl = Label(status_frame,text=step,bg="white",fg=color,font=("Arial", 11, "bold"))
            lbl.grid(row=0, column=i, padx=30)
            status.append(lbl)
            i += 1
        
    def track_case():
        case_id = entry_id.get()

        if case_id == "":
            messagebox.showwarning("Error", "Enter Case ID")
            return

        try:
            con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="crime_system"
            )

            cursor = con.cursor()
            cursor.execute(
                "SELECT status FROM crimes WHERE track_id=%s",
                (case_id,)
            )
            result = cursor.fetchone()
            if result:
                show_status(result[0])
            else:
                messagebox.showerror("Error", "Invalid Track ID")
            con.close()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    Button(search_frame, text="Track",bg="blue", fg="white",font=("Arial", 11, "bold"),width=12,command=track_case).pack(pady=10)

    def go_back():
        track.destroy()

    Button(track, text="Back",bg="red", fg="white",command=go_back).pack(pady=20)