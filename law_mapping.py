from tkinter import *
from tkinter import messagebox
import webbrowser


def open_law_mapping(root,bg="white"):
    lawmapp = Toplevel(root)
    lawmapp.title("Law Mapping System")
    lawmapp.geometry("700x650")

    Label(lawmapp, text="Smart Law Mapping System",bg="#1e293b", fg="white",font=("Segoe UI", 16, "bold"),pady=10).pack(fill=X)

    crime_law = {
        "Theft": ("IPC 378", "Up to 3 years jail", "Keep valuables safe", "Stealing property"),
        "Fraud": ("IPC 420", "Up to 7 years jail", "Do not share OTP", "Cheating for money"),
        "Assault": ("IPC 351", "Up to 1 year jail", "Stay safe", "Physical attack"),
        "Cyber Crime": ("IT Act 66", "Up to 3 years jail", "Save proof", "Internet crime"),
        "Murder": ("IPC 302", "Life imprisonment", "Serious crime", "Killing a person"),
        "Kidnapping": ("IPC 359", "Up to 7 years jail", "Call police", "Taking person illegally"),
        "Robbery": ("IPC 390", "Up to 10 years jail", "Report immediately", "Forcefully taking property"),
        "Harassment": ("IPC 354A", "Up to 3 years jail", "Report issue", "Unwanted behavior")
    }

    frame = Frame(lawmapp, bg="white")
    frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

    Label(frame, text="Enter Crime:", bg="white",font=("Segoe UI", 12)).grid(row=0, column=0, pady=10)
    
    crime = StringVar()
    crime.set("Theft") 

    crime_entry = OptionMenu(frame, crime, *crime_law.keys())
    crime_entry.grid(row=0, column=1)

    law = Label(frame, text="", bg="white", fg="blue")
    law.grid(row=2, column=1)

    punishment = Label(frame, text="", bg="white", fg="red")
    punishment.grid(row=3, column=1)

    advice = Label(frame, text="", bg="white", fg="green")
    advice.grid(row=4, column=1)

    meaning = Label(frame, text="", bg="white", fg="black")
    meaning.grid(row=5, column=1)

    def show_law():
        selected = crime.get()  

        if selected in crime_law:
            data = crime_law[selected]

            lawtext = data[0]
            punishmenttext = data[1]
            advicetext = data[2]
            meaningtext = data[3]

            law.config(text="Law: " + lawtext)
            punishment.config(text="Punishment: " + punishmenttext)
            advice.config(text="Advice: " + advicetext)
            meaning.config(text="Meaning: " + meaningtext)

        else:
            messagebox.showerror("Error", "Crime not found")

    Button(frame, text="Show Law",bg="#2563eb", fg="white",command=show_law).grid(row=1, column=1, pady=10)

    Label(frame, text="Search IPC:", bg="white").grid(row=6, column=0)
    search = Entry(frame)
    search.grid(row=6, column=1)

    result = Label(frame, text="", bg="white", fg="purple")
    result.grid(row=7, column=1)

    def search_law():
        query = search.get().lower()

        for crime in crime_law:
            law = crime_law[crime][0]

            if query in law.lower():
                result.config(text=crime + " → " + law)
                return

        result.config(text="Not found")

    Button(frame, text="Search",bg="green", fg="white",command=search_law).grid(row=6, column=2)

    Label(frame, text="Top Law Firms in India", 
      bg="white", fg="#1e293b",
      font=("Segoe UI", 11, "bold")).grid(row=8, column=0, columnspan=3, pady=5)

    law_firms_text = """
    1) Cyril Amarchand Mangaldas (CAM)
    - Corporate advisory, M&A, capital markets

    2) Shardul Amarchand Mangaldas & Co
     - Corporate law, dispute resolution, competition law

    3) AZB & Partners
     - M&A, private equity, banking

    4) Khaitan & Co
     - Tax, banking, corporate law

    5) Trilegal
    - Infrastructure, project finance, venture capital
"""

    Label(frame, text=law_firms_text,bg="white", fg="black",justify=LEFT).grid(row=9, column=0, columnspan=3, sticky="w", padx=10)

    def showlawfirms():
        webbrowser.open("https://www.cyrilshroff.com/")

    emergency_btn = Button(frame, text="Visit Law Firms",bg="green", fg="white",command=showlawfirms)
    emergency_btn.grid(row=10, column=1, pady=10)