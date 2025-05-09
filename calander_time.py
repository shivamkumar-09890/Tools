import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

def show_selection():
    selected_date = cal.get_date()
    selected_hour = hour_var.get()
    selected_minute = minute_var.get()
    selected_time = f"{selected_hour}:{selected_minute}"
    result = f"{selected_date} {selected_time}"
    result_label.config(text=f"Selected: {selected_date} {selected_time}")
    print("Selected Date and Time:", result) 

# Main window
root = tk.Tk()
root.title("Select Date and Time")
root.geometry("300x400")

# Calendar widget
cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal.pack(pady=20)

# Time selection
hour_var = tk.StringVar(value="00")
minute_var = tk.StringVar(value="00")

time_frame = ttk.Frame(root)
time_frame.pack(pady=10)

ttk.Label(time_frame, text="Hour:").grid(row=0, column=0)
hour_spin = ttk.Spinbox(time_frame, from_=0, to=23, textvariable=hour_var, width=5, format="%02.0f")
hour_spin.grid(row=0, column=1)

ttk.Label(time_frame, text="Minute:").grid(row=0, column=2)
minute_spin = ttk.Spinbox(time_frame, from_=0, to=59, textvariable=minute_var, width=5, format="%02.0f")
minute_spin.grid(row=0, column=3)

# Button to confirm selection
submit_btn = ttk.Button(root, text="Submit", command=show_selection)
submit_btn.pack(pady=10)

# Label to show result
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
