from tkinter import *
from tkinter import messagebox,ttk
import mysql.connector
from admin_dashboard import open_admin_dashboard
from dashboard import open_dashboard


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crime_system"
    )


def open_login(root):
    login = Toplevel(root)
    login.title("Login - Crime System")
    login.state("zoomed")
    
    bg_image = PhotoImage(file="C:/Users/upadh/OneDrive/Desktop/python-4th sem/crime reporting and tracking system/crime_bg.png")
    bg_label = Label(login, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = Frame(login, bg="white", bd=5, relief=RIDGE)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    label1 = Label(frame, text="CRIME REPORTING SYSTEM",font=("Arial", 22, "bold"),fg="#b30000",bg="white").grid(row=0, column=0, columnspan=2, pady=20)
    label2 = Label(frame, text="Login Form",font=("Arial", 13), bg="white",fg="gray").grid(row=1, column=0, columnspan=2, pady=5)

    Label(frame, text="Username", bg="white", font=("Arial", 12)).grid(row=2, column=0, pady=10, padx=10)
    txt_user = Entry(frame, font=("Arial", 12), width=20)
    txt_user.grid(row=2, column=1, pady=10)

    Label(frame, text="Password", bg="white", font=("Arial", 12)).grid(row=3, column=0, pady=10)
    txt_pass = Entry(frame, show="*", font=("Arial", 12), width=20)
    txt_pass.grid(row=3, column=1, pady=10)

    def see_password():
        if txt_pass["show"] == "*":
            txt_pass.config(show="")  
        else:
             txt_pass.config(show="*")  
           
    Button(frame, text="Show", command=see_password, bg="lightgray").grid(row=3, column=2, padx=5)

    
    Label(frame, text="Role", bg="white", font=("Arial", 12)).grid(row=4, column=0, pady=10)
    role = ttk.Combobox(frame, values=["Admin", "Citizen"])
    role.grid(row=4, column=1)
    role.set("Select Role")

    def login():
        username = txt_user.get()
        password = txt_pass.get()
        selected_role = role.get()

        if username == "" or password == "" or role == "Select Role":
            messagebox.showwarning("Error", "All fields are required")
            return

        try:
            con = connect_db()
            cursor = con.cursor()

            query = "SELECT username, role FROM login WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                db_role = result[1]
                messagebox.showinfo("Success", "Login Successful")

                if db_role == "Admin":
                    open_admin_dashboard(root)
                else:
                    open_dashboard(root, username)

            else:
                messagebox.showerror("Error", "Invalid Credentials")
                con.close()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def reset():
        txt_user.delete(0, END)
        txt_pass.delete(0, END)
        role.set("Select Role")

    
    Button(frame, text="Login",bg="green", fg="white",width=12,font=("Arial", 11, "bold"),command=login).grid(row=5, column=0, pady=20)
    Button(frame, text="Reset", bg="red", fg="white", width=12, font=("Arial", 11, "bold"),command=reset).grid(row=5, column=1, pady=20)

 