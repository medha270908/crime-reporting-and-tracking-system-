from tkinter import *
from tkinter import messagebox,ttk
import mysql.connector
import webbrowser


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crime_system"
    )


def open_smart_reporting(root):

    smartrep = Toplevel(root)
    smartrep.title("Smart Crime reporting system")
    smartrep.geometry("800x600")
    smartrep.configure(bg="white")

    Label(smartrep,text="SMART CRIME REPORTING SYSTEM",font=("Arial", 16, "bold"),bg="#1f4e79",fg="white").pack(fill=X)

    main = Frame(smartrep, bg="white")
    main.pack(fill=BOTH, expand=True, padx=20, pady=10)

    left = Frame(main, bg="white")
    left.grid(row=0, column=0, sticky="n")

    right = Frame(main, bg="white")
    right.grid(row=0, column=1, sticky="n", padx=40)

    severity = StringVar(value="Low")

    result = Label(left, text="", fg="blue", bg="white", font=("Arial", 11, "bold"))
    result.grid(row=3, column=0, columnspan=3, pady=5)

    tips = Label(left, text="", bg="white", fg="green")
    tips.grid(row=4, column=0, columnspan=3,pady=2)

    station = Label(left, text="", fg="green", bg="white")
    station.grid(row=5, column=0, columnspan=3, pady=2)

    summary_label = Label(left, text="", bg="white", justify=LEFT)
    summary_label.grid(row=6, column=0, columnspan=3, pady=2)

    def detect_crime():
        text = desc_entry.get().lower()

        if "theft" in text or "steal" in text or "missing" in text:
            crime = "Theft"
            tip_text = "Keep valuables safe"
        elif "fraud" in text or "fake calling" in text or "scam calling" in text or "cheating" in text:
            crime = "Cyber Crime"
            tip_text = "Do not share OTP"
        elif "attack" in text or "fight" in text or "assault" in text:
            crime = "Assault"
            tip_text = "Go to safe place"
        elif "kill" in text or "murder" in text:
            crime = "Murder"
            tip_text = "Call emergency services"
        elif "kidnap" in text or "abduct" in text:
            crime = "Kidnapping"
            tip_text = "Call emergency services"
        elif "robbery" in text or "hold up" in text:
            crime = "Robbery"
            tip_text = "Report immediately"
        elif "harass" in text or "eve-teasing" in text:
            crime = "Harassment"
            tip_text = "Report issue"
        else:
            crime = "General"
            tip_text = "Stay alert"

        result.config(text="Detected Crime: " + crime)
        tips.config(text="Tips: " + tip_text)

    def find_station():
        if area.get() == "Colaba":
            station_text = "Colaba Police Station"
        elif area.get() == "Dadar":
            station_text = "Shivaji Park Police Station"
        elif area.get() == "Goregaon":
            station_text = "Goregaon West Police Station"
        elif area.get() == "Jogeshwari":
            station_text = "Amboli Police Station"
        elif area.get() == "Juhu":
            station_text = "Juhu Police Station"
        elif area.get() == "Kalyan":
            station_text = "Mahatma Phule Police Station"
        elif area.get() == "Kurla":
            station_text = "Kurla Police Station"
        elif area.get() == "Malad":
            station_text = "Malad Police Station"
        elif area.get() == "Marine Lines":
            station_text = "Marine Lines Police Station"
        elif area.get() == "Powai":
            station_text = "Powai Police Station"
        elif area.get() == "Santacruz":
            station_text = "Santacruz Police Station"
        elif area.get() == "Andheri":
            station_text = "MIDC Police Station"
        elif area.get() == "Bandra":
            station_text = "Bandra Police Station"
        else:
            station_text = "Search in map"

        station.config(text="Nearest: " + station_text)

    def open_map():
        place = place_entry.get()
        if place == "":
            place = area.get()

        link= "https://www.google.com/maps/search/" + place + "+police station"
        webbrowser.open(link)

    def call_police(event):
        messagebox.showinfo("Calling", "Calling 100...")

    def call_fire(event):
        messagebox.showinfo("Calling", "Calling 101...")

    def call_ambulance(event):
        messagebox.showinfo("Calling", "Calling 102...")

    def call_tourist(event):
        messagebox.showinfo("Calling", "Calling 1363...")

    def call_road(event):
        messagebox.showinfo("Calling", "Calling 1073...")

    def call_disaster(event):
        messagebox.showinfo("Calling", "Calling 108...")

    def call_women(event):
        messagebox.showinfo("Calling", "Calling 1091...")

    def save_report():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reports (issue, area, severity) VALUES (%s,%s,%s)",
            (desc_entry.get(), area.get(), severity.get()))
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Report Saved")

    def show_summary():
        summary = f"""
CASE SUMMARY
----------------
Issue: {desc_entry.get()}
Area: {area.get()}
Severity: {severity.get()}
"""
        summary_label.config(text=summary)
    
    def emergency():
        messagebox.showwarning("Emergency", "Call Police: 100")

    Label(left, text="Describe Issue:", bg="white").grid(row=0, column=0)
    desc_entry = Entry(left, width=25)
    desc_entry.grid(row=0, column=1)

    Button(left, text="Detect Crime", command=detect_crime, width=15).grid(row=0, column=2, padx=10)

    Label(left, text="Select Area:", bg="white").grid(row=1, column=0, pady=10)
    areas = ["Colaba", "Dadar", "Goregaon", "Jogeshwari", "Juhu","Kalyan", "Kurla", "Malad", "Marine Lines", "Powai", "Santacruz",
               "Andheri", "Bandra"]
    area = ttk.Combobox(left,values=areas,state="readonly")
    area.grid(row=1,column=1)
    area.set("Select Area")

    Button(left, text="Find Station", command=find_station, width=15).grid(row=1, column=2, padx=10)

    Label(left, text="Severity:", bg="white").grid(row=2, column=0, pady=10)
    severity = ttk.Combobox(left,values=["Low", "Medium", "High"],state="readonly",width=15)
    severity.grid(row=2, column=1)
    severity.set("Select severity")

    Label(right, text="Search Place:", bg="white").grid(row=0, column=0)

    place_entry = Entry(right, width=25)
    place_entry.grid(row=1, column=0)

    Button(right, text="Open Map", command=open_map,bg="#2563eb", fg="white").grid(row=1, column=1, padx=10)

    Label(right, text="Emergency Numbers",bg="white", fg="#1f4e79",font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2, pady=10)

    police = Label(right, text="Police: 100", fg="blue", bg="white", cursor="hand2")
    police.grid(row=3, column=0, columnspan=2, sticky="w")
    police.bind("<Button-1>", call_police)

    fire = Label(right, text="Fire: 101", fg="blue", bg="white", cursor="hand2")
    fire.grid(row=4, column=0, columnspan=2, sticky="w")
    fire.bind("<Button-1>", call_fire)

    ambulance = Label(right, text="Ambulance: 102", fg="blue", bg="white", cursor="hand2")
    ambulance.grid(row=5, column=0, columnspan=2, sticky="w")
    ambulance.bind("<Button-1>", call_ambulance)

    tourist = Label(right, text="Tourist Helpline: 1363", fg="blue", bg="white", cursor="hand2")
    tourist.grid(row=6, column=0, columnspan=2, sticky="w")
    tourist.bind("<Button-1>", call_tourist)

    road = Label(right, text="Road Accident: 1073", fg="blue", bg="white", cursor="hand2")
    road.grid(row=7, column=0, columnspan=2, sticky="w")
    road.bind("<Button-1>", call_road)

    disaster = Label(right, text="Disaster Management: 108", fg="blue", bg="white", cursor="hand2")
    disaster.grid(row=8, column=0, columnspan=2, sticky="w")
    disaster.bind("<Button-1>", call_disaster)

    women = Label(right, text="Women in Distress: 1091", fg="blue", bg="white", cursor="hand2")
    women.grid(row=9, column=0, columnspan=2, sticky="w")
    women.bind("<Button-1>", call_women)

    Button(left, text="Save Report", bg="green", fg="white",command=save_report, width=18).grid(row=7, column=1, padx=10)
    Button(left, text="Show Summary",command=show_summary, width=18).grid(row=7, column=2, padx=10)
    Button(smartrep,text="EMERGENCY",bg="red",fg="white",font=("Arial", 12, "bold"),width=30,command=emergency).pack(side=BOTTOM, pady=20)