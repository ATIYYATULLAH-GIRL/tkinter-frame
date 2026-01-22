import tkinter as tk
from tkinter import messagebox
from datetime import date, datetime

def age():
    try:
        day=int(day_entry.get())
        month=int(month_entry.get())
        year=int(year_entry.get())
        date_of_birth=date(year, month, day)
        today=date.today()

        if date_of_birth > today:
            messagebox.showerror("Invalid Date", "Date of birth cannot be in the future.")
            return
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        messagebox.showinfo("Age Result", f"Your current age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date (numeric values only).")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")

tk.Label(root,text="Enter Date of Birth",font=("Arial",14,"bold"),fg="purple").pack(pady=10)

frame=tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame,text="Day:").grid(row=0, column=0, padx=5, pady=5)
day_entry=tk.Entry(frame, width=5)
day_entry.grid(row=0, column=1)

tk.Label(frame,text="Month:").grid(row=1, column=0, padx=5, pady=5)
month_entry=tk.Entry(frame, width=5)
month_entry.grid(row=1, column=1)

tk.Label(frame,text="Year: ").grid(row=2, column=0, padx=5, pady=5)
year_entry=tk.Entry(frame, width=5)
year_entry.grid(row=2, column=1)

tk.Button(root,text="Calculate Age",command=age,bg="pink",fg="white").pack(pady=15)

root.mainloop()