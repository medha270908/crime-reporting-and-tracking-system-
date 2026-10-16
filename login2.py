from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
import mysql.connector
import random
from datetime import datetime
from tkcalendar import DateEntry

# -------- DATABASE CONNECTION --------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crime_system"
    )

# -------- REPORT CRIME WINDOW --------
def open_report_form():
    root = Tk()
    form = Toplevel(root)
    form.title("Report Crime")
    form.state("zoomed")
    form.configure(bg="#eef2f7")

    Label(form, text="Crime Reporting Form",
          font=("Arial",20,"bold"),
          bg="#eef2f7").pack(pady=20)

    frame = Frame(form, bg="white", bd=1, relief=SOLID)
    frame.pack(pady=10, padx=20)

    # -------- VARIABLES --------
    name = StringVar()
    gender = StringVar()
    email = StringVar()
    phone = StringVar()
    crime_type = StringVar()
    photo_path = StringVar()

    # -------- FORM --------
    Label(frame, text="Name", bg="white").grid(row=0, column=0, padx=10, pady=10)
    Entry(frame, textvariable=name).grid(row=0, column=1)

    # -------- GENDER RADIO --------
    Label(frame, text="Gender", bg="white").grid(row=1, column=0)

    g_frame = Frame(frame, bg="white")
    g_frame.grid(row=1, column=1)

    Radiobutton(g_frame, text="Male", variable=gender, value="Male", bg="white").pack(side=LEFT)
    Radiobutton(g_frame, text="Female", variable=gender, value="Female", bg="white").pack(side=LEFT)
    Radiobutton(g_frame, text="Other", variable=gender, value="Other", bg="white").pack(side=LEFT)

    # -------- EMAIL --------
    Label(frame, text="Email", bg="white").grid(row=2, column=0)
    Entry(frame, textvariable=email).grid(row=2, column=1)

    # -------- PHONE --------
    Label(frame, text="Phone", bg="white").grid(row=3, column=0)
    Entry(frame, textvariable=phone).grid(row=3, column=1)

    # -------- DATE PICKER --------
    Label(frame, text="Date", bg="white").grid(row=4, column=0)
    date_entry = DateEntry(frame, width=20)
    date_entry.grid(row=4, column=1)

    # -------- TIME PICKER --------
    Label(frame, text="Time", bg="white").grid(row=5, column=0)

    time_frame = Frame(frame, bg="white")
    time_frame.grid(row=5, column=1)

    hour = ttk.Combobox(time_frame,
                        values=[str(i).zfill(2) for i in range(24)],
                        width=5, state="readonly")
    hour.set("HH")
    hour.pack(side=LEFT)

    Label(time_frame, text=":", bg="white").pack(side=LEFT)

    minute = ttk.Combobox(time_frame,
                          values=[str(i).zfill(2) for i in range(60)],
                          width=5, state="readonly")
    minute.set("MM")
    minute.pack(side=LEFT)

    # -------- CRIME TYPE --------
    Label(frame, text="Crime Type", bg="white").grid(row=6, column=0)
    ttk.Combobox(frame, textvariable=crime_type,
                 values=["Theft","Cyber Crime","Fraud","Assault","Other"],
                 state="readonly").grid(row=6, column=1)

    # -------- DESCRIPTION --------
    Label(frame, text="Description", bg="white").grid(row=7, column=0)
    desc = Text(frame, width=30, height=4)
    desc.grid(row=7, column=1)

    # -------- PHOTO --------
    def upload_photo():
        file = filedialog.askopenfilename(parent=form)
        if file:
            photo_path.set(file)

    Label(frame, text="Photo", bg="white").grid(row=8, column=0)
    Button(frame, text="Upload Photo", command=upload_photo).grid(row=8, column=1)

    # -------- SUBMIT --------
    def submit_crime():

        if name.get()=="" or phone.get()=="":
            messagebox.showwarning("Error","Fill required fields")
            return

        if hour.get()=="HH" or minute.get()=="MM":
            messagebox.showwarning("Error","Select valid time")
            return

        track_id = "CR" + str(random.randint(1000,9999))

        selected_date = date_entry.get()
        selected_time = f"{hour.get()}:{minute.get()}"

        try:
            con = connect_db()
            cursor = con.cursor()

            query = """INSERT INTO crimes
                       (track_id, name, gender, email, phone, crime_type, description, date, time, photo)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            values = (
                track_id,
                name.get(),
                gender.get(),
                email.get(),
                phone.get(),
                crime_type.get(),
                desc.get("1.0", END),
                selected_date,
                selected_time,
                photo_path.get()
            )

            cursor.execute(query, values)
            con.commit()
            con.close()

            messagebox.showinfo("Success", f"Crime Reported!\nTrack ID: {track_id}")

        except Exception as e:
            messagebox.showerror("DB Error", str(e))

    Button(frame, text="Submit",
           bg="#4CAF50",
           fg="white",
           command=submit_crime).grid(row=9, column=0, columnspan=2, pady=20)

# -------- DASHBOARD --------
def open_dashboard(user):

    dash = Toplevel()
    dash.title("Dashboard")
    dash.state("zoomed")
    dash.configure(bg="#eef2f7")

    Label(dash, text="Digital Crime Reporting Portal",
          font=("Arial",22,"bold"),
          bg="#eef2f7").pack(pady=20)

    Label(dash, text=f"Welcome, {user}",
          bg="#eef2f7").pack()

    btn_frame = Frame(dash, bg="#eef2f7")
    btn_frame.pack(pady=30)

    Button(btn_frame, text="Report Crime",
           bg="#4CAF50", fg="white",
           width=18, height=2,
           command=open_report_form).grid(row=0, column=0, padx=20)

    Button(btn_frame, text="Track Case",
           bg="#2196F3", fg="white",
           width=18, height=2).grid(row=0, column=1, padx=20)

# -------- LOGIN FUNCTION --------
def login():
    username = txt_user.get()
    password = txt_pass.get()
    role = role_box.get()

    if username == "" or password == "":
        messagebox.showwarning("Error", "All fields are required")
        return

    try:
        con = connect_db()
        cursor = con.cursor()

        query = "SELECT * FROM login WHERE username=%s AND password=%s AND role=%s"
        cursor.execute(query, (username, password, role))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", "Login Successful")
            open_dashboard(username)
        else:
            messagebox.showerror("Error", "Invalid Credentials")

        con.close()

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# -------- RESET --------
def reset():
    txt_user.delete(0, END)
    txt_pass.delete(0, END)
    role_box.set("Select Role")

# -------- MAIN WINDOW --------
window = Tk()
window.title("Crime Reporting System")
window.state("zoomed")
window.configure(bg="#eef2f7")

frame = Frame(window, bg="white", bd=1, relief=SOLID)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(frame, text="Crime Reporting & Tracking System",
      font=("Arial",20,"bold"),
      bg="white").grid(row=0, column=0, columnspan=2, pady=10)

Label(frame, text="Login Form",
      font=("Arial",12),
      bg="white",
      fg="gray").grid(row=1, column=0, columnspan=2)

Label(frame, text="Username", bg="white").grid(row=2, column=0, pady=10)
txt_user = Entry(frame)
txt_user.grid(row=2, column=1)

Label(frame, text="Password", bg="white").grid(row=3, column=0, pady=10)
txt_pass = Entry(frame, show="*")
txt_pass.grid(row=3, column=1)

Label(frame, text="Role", bg="white").grid(row=4, column=0, pady=10)
role_box = ttk.Combobox(frame, values=["Admin","Customer"], state="readonly")
role_box.set("Select Role")
role_box.grid(row=4, column=1)

Button(frame, text="Login",
       bg="#4CAF50", fg="white",
       command=login).grid(row=5, column=0, pady=20)

Button(frame, text="Reset",
       bg="#f44336", fg="white",
       command=reset).grid(row=5, column=1, pady=20)

window.mainloop()