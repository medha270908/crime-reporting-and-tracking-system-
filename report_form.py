from tkinter import *
from tkinter import messagebox,ttk
from tkcalendar import Calendar
import mysql.connector
import random

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crime_system"
    )

def open_report_form(dash):

    reportform = Toplevel(dash)
    reportform.title("Crime Reporting Form")
    reportform.state("zoomed")
    reportform.configure(bg="white")

    Label(reportform, text="Crime Reporting Form",font=("Arial", 20, "bold"),bg="white").pack(pady=20)

    form = Frame(reportform, bg="white", bd=1, relief=SOLID)
    form.pack(pady=10, padx=20)

    gender = StringVar()
    agree_var = IntVar()
    track_id = "CR" + str(random.randint(1000, 9999))

    Label(form, text="Name", bg="white").grid(row=0, column=0, padx=10, pady=10)
    name = Entry(form)
    name.grid(row=0, column=1)

    Label(form, text="Gender", bg="white").grid(row=1, column=0)
    g_frame = Frame(form, bg="white")
    g_frame.grid(row=1, column=1)

    Radiobutton(g_frame, text="Male", variable=gender, value="Male", bg="white").pack(side=LEFT)
    Radiobutton(g_frame, text="Female", variable=gender, value="Female", bg="white").pack(side=LEFT)
    Radiobutton(g_frame, text="Other", variable=gender, value="Other", bg="white").pack(side=LEFT)

    Label(form, text="Email", bg="white").grid(row=2, column=0)
    email = Entry(form)
    email.grid(row=2, column=1)

    Label(form, text="Phone", bg="white").grid(row=3, column=0)
    phone = Entry(form)
    phone.grid(row=3, column=1)

    Label(form, text="Date", bg="white").grid(row=4, column=0)
    cal = Calendar(form, selectmode='day')
    cal.grid(row=4, column=1)

    Label(form, text="Crime Type", bg="white").grid(row=5, column=0)

    crimes = ["Theft", "Robbery", "Assault", "Cyber Crime",
              "Fraud", "Inchoate Crimes", "Organized Crime",
              "Financial Crimes", "Other"]
    crime_type = ttk.Combobox(form,values=crimes,state="readonly")
    crime_type.grid(row=5,column=1)

    Label(form, text="Description", bg="white").grid(row=6, column=0)
    desc = Text(form, width=30, height=4)
    desc.grid(row=6, column=1)

    Label(form, text="Location", bg="white").grid(row=7, column=0)
    location = Entry(form)
    location.grid(row=7, column=1)

    Checkbutton(form,text="I confirm the information is correct",variable=agree_var,bg="white").grid(row=9, columnspan=2)

    def submit_crime():

        if name.get() == "" or phone.get() == "":
            messagebox.showwarning("Error", "Fill required fields")
            return

        if agree_var.get() == 0:
            messagebox.showwarning("Error", "Please confirm details")
            return

        selected_date = cal.get_date()

        try:
            con = connect_db()
            cursor = con.cursor()

            query = """INSERT INTO crimes(track_id, name, gender, email, phone,crime_type, description, date, location)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            values = (
                track_id,name.get(),gender.get(),email.get(),phone.get(),crime_type.get(),desc.get("1.0", END),selected_date,location.get()
            )

            cursor.execute(query, values)
            con.commit()
            con.close()

            messagebox.showinfo("Success",f"Crime Reported!\nTrack ID: {track_id}",parent=reportform)
            reportform.destroy()

        except Exception as e:
            messagebox.showerror("DB Error", str(e))

    def reset_form():
        name.delete(0, END)
        email.delete(0, END)
        phone.delete(0, END)
        location.delete(0, END)
        desc.delete("1.0", END)
        gender.set("")
        crime_type.set("Select")
        agree_var.set(0)

    Button(form, text="Submit",bg="green", fg="white", width=12,command=submit_crime).grid(row=10, column=0, padx=20, pady=20)
    Button(form, text="Reset",bg="red", fg="white", width=12,command=reset_form).grid(row=10, column=1, padx=20, pady=20)