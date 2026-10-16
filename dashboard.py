from tkinter import *
import webbrowser
from report_form import open_report_form
from track_crime import open_track_page
from smart_reporting import open_smart_reporting
from law_mapping import open_law_mapping
from crime_analytics import open_crime_analytics


def open_dashboard(root, user,bg="white"):
    dash = Toplevel(root)
    dash.title("Dashboard")
    dash.state("zoomed")

    header = Frame(dash, bg="#1f4e79", height=60)
    header.pack(fill=X)

    left_frame  = Frame(header,bg="#1f4e79")
    left_frame.pack(side=LEFT,padx=15)

    logo = PhotoImage(file = "C:/Users/upadh/OneDrive/Desktop/python-4th sem/crime reporting and tracking system/crime_logo.png").subsample(20,20)

    logo_label = Label(left_frame,image=logo,bg="#1f4e79")
    logo_label.image = logo
    logo_label.pack(side=LEFT,padx=5)

    Label(left_frame,text="Smart Crime Reporting & Tracking System",bg="#1f4e79", fg="white",font=("Arial", 16, "bold")).pack(side=LEFT)

    def open_news(event):
        webbrowser.open("https://news.google.com/search?q=crime")

    news_label = Label(header,text="Today's Crime News",fg="yellow", bg="#1f4e79",cursor="hand2")
    news_label.pack(side=RIGHT, padx=20)
    news_label.bind("<Button-1>", open_news)
    
    Label(dash,text="Secure Digital Crime Reporting Portal",bg="white",font=("Arial", 22, "bold")).pack(pady=15)
    Label(dash,text="Welcome, " + user,bg="white").pack()

    desc = """This system allows users to report crimes online easily.It helps in maintaining records and tracking complaints.
            The system improve communication between citizens and police.Users can monitor their case status in real-time.
            It ensures transparency and faster processing of complaints.The platform is secure and user-friendly.
            sIt helps authorities analyze crime patterns.
            Overall, it contributes to a safer society."""

    Label(dash,text=desc,bg="white",font=("Arial", 11),justify=CENTER).pack(padx=40, pady=15)

    btn_frame = Frame(dash, bg="white")
    btn_frame.pack(pady=10)

    def open_report():
        open_report_form(dash)

    def open_track():
        open_track_page(dash)

    Button(btn_frame,text="Report Crime",bg="#e74c3c",fg="white",font=("Arial", 11, "bold"),width=15,command=open_report).grid(row=0, column=0, padx=10)
    Button(btn_frame,text="Track Your Case",bg="#3498db",fg="white",font=("Arial", 11, "bold"),width=15,command=open_track).grid(row=0, column=1, padx=10)

    feature_frame = Frame(dash, bg="white")
    feature_frame.pack(pady=40)

    def open_smart_report():
        open_smart_reporting(dash)
    def open_law_mapp():
        open_law_mapping(dash)
    def open_crime_analyt():
        open_crime_analytics(dash)

    img1 = PhotoImage(file="C:/Users/upadh/OneDrive/Desktop/python-4th sem/crime reporting and tracking system/smart_reporting_logo.png").subsample(10,10)
    img2 = PhotoImage(file="C:/Users/upadh/OneDrive/Desktop/python-4th sem/crime reporting and tracking system/crime_lawmapping_logo.png").subsample(10,10)
    img3 = PhotoImage(file="C:/Users/upadh/OneDrive/Desktop/python-4th sem/crime reporting and tracking system/crime_analytics_logo.png").subsample(10,10)

    btn1 = Button(feature_frame, text="Smart Reporting", image=img1,compound=TOP, command=open_smart_report)
    btn1.image = img1
    btn1.grid(row=0, column=0, padx=30)

    btn2 = Button(feature_frame, text="Law Mapping", image=img2, compound=TOP, command=open_law_mapp)
    btn2.image = img2
    btn2.grid(row=0, column=1, padx=30)

    btn3 = Button(feature_frame, text="Crime Analytics", image=img3, compound=TOP,command=open_crime_analyt)
    btn3.image = img3
    btn3.grid(row=0, column=2, padx=30)