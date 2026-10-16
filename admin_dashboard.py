from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import smtplib


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crime_system"
    )


def send_email(receiver, status):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()

        sender = "upadhyaymedha2008@gmail.com"
        password = "zqvpczsgriyulvgx"

        s.login(sender, password)

        subject = "Crime Case Status Update"
        body = f"Hello,\n\nYour complaint status is updated to: {status}\n\nThank you."

        message = f"Subject: {subject}\n\n{body}"

        s.sendmail(sender, receiver, message)
        s.quit()

        print("Email Sent Successfully")

    except Exception as e:
        print("Email Error:", e)


def open_admin_dashboard(login):
    admin = Toplevel(login)
    admin.title("Admin Dashboard")
    admin.state("zoomed")

    Label(admin, text="Admin Dashboard",font=("Arial", 20, "bold"),bg="#1f4e79", fg="white").pack(fill=X)

    columns = ("track_id", "name", "email", "crime_type", "status")

    crime_table = ttk.Treeview(admin, columns=columns, show="headings")
    crime_table.pack(fill=BOTH, expand=True)

    for col in columns:
        crime_table.heading(col, text=col)
        crime_table.column(col, width=150)

    def load_data():
        con = connect_db()
        cursor = con.cursor()
        cursor.execute("SELECT track_id, name, email, crime_type, status FROM crimes")
        rows = cursor.fetchall()

        for item in crime_table.get_children():
            crime_table.delete(item)

        for record in rows:
            crime_table.insert("", END, values=record)

        con.close()
    load_data()

    status = StringVar()
    status.set("Registered")

    OptionMenu(admin, status,
               "Registered", "In Progress",
               "Under Investigation", "Resolved").pack(pady=10)

    def update_status():
        selected = crime_table.focus()

        if not selected:
            messagebox.showwarning("Error", "Select a record")
            return

        values = crime_table.item(selected, "values")

        track_id = values[0]
        email = values[2]
        new_status = status.get()

        con = connect_db()
        cursor = con.cursor()

        cursor.execute(
            "UPDATE crimes SET status=%s WHERE track_id=%s",
            (new_status, track_id)
        )

        con.commit()
        con.close()

        send_email(email, new_status)
        messagebox.showinfo("Success", "Status Updated and Email Sent")
        load_data()

    Button(admin, text="Update Status",bg="green", fg="white",command=update_status).pack(pady=10)
    Button(admin, text="Refresh",command=load_data).pack(pady=5)