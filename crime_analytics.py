from tkinter import *
import matplotlib.pyplot as plt
import mysql.connector


def get_data(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crime_system"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

def open_crime_analytics(root):
    analy = Toplevel(root)
    analy.title("Crime Analytics Dashboard")
    analy.geometry("700x550")
    analy.configure(bg="#eef2f7")

    Label(analy, text="Crime Analytics Dashboard",bg="#0f172a", fg="white",font=("Arial", 18, "bold"),height=2).pack(fill=X)

    def bar_chart():
        data = get_data("SELECT area, COUNT(*) FROM reports GROUP BY area")

        areas = []
        counts = []

        for area in data:
            areas.append(area[0])
            counts.append(area[1])
        
        plt.figure(figsize=(10,5))
        plt.bar(areas, counts)
        plt.xticks(rotation=45)
        plt.title("Crime by Area")
        plt.tight_layout()
        plt.xlabel("Area")
        plt.ylabel("Number of Crimes")
        plt.show()

    def pie_chart():
        data = get_data("SELECT issue, COUNT(*) FROM reports GROUP BY issue")

        labels = []
        values = []

        for area_list in data:
            labels.append(area_list[0])
            values.append(area_list[1])

        plt.pie(values, labels=labels, autopct="%1.1f%%")
        plt.title("Crime Types")
        plt.show()

    def top_area():
        data = get_data("SELECT area, COUNT(*) FROM reports GROUP BY area")

        max_area = ""
        max_count = 0

        for area_list in data:
            if area_list[1] > max_count:
                max_count = area_list[1]
                max_area = area_list[0]

        outputlabel.config(text="Top Area: " + max_area)

    frame = Frame(analy, bg="white")
    frame.pack(pady=20)

    Button(frame, text="Bar Graph", width=20, command=bar_chart).grid(row=0, column=0, padx=10, pady=10)
    Button(frame, text="Pie Chart", width=20, command=pie_chart).grid(row=0, column=1, padx=10, pady=10)
    Button(frame, text="Top Area", width=20, command=top_area).grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    
    outputlabel = Label(analy,text="Click buttons to see result",font=("Arial", 12),bg="white")
    outputlabel.pack(pady=20)