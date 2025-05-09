import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import datetime, date, time as dt_time

selected_slots = []

def is_weekend(selected):
    dt_obj = datetime.strptime(selected, "%Y-%m-%d")
    return dt_obj.weekday() >= 5  # 5 = Saturday, 6 = Sunday

def validate_and_add_slot():
    selected_date = cal.get_date()
    
    if is_weekend(selected_date):
        messagebox.showerror("Invalid Date", "Weekends are not allowed.")
        return
    
    selected_hour = int(hour_var.get())
    selected_minute = int(minute_var.get())
    
    selected_dt = datetime.strptime(selected_date, "%Y-%m-%d").replace(
        hour=selected_hour, minute=selected_minute)

    now = datetime.now()
    
    if selected_hour < 9 or selected_hour > 17:
        messagebox.showerror("Invalid Time", "Select a time between 09:00 and 17:00.")
        return
    elif selected_dt < now:
        messagebox.showerror("Past Time", "Cannot select a past time slot.")
        return

    slot = f"{selected_date} {selected_hour:02d}:{selected_minute:02d}"
    if slot in selected_slots:
        messagebox.showinfo("Duplicate", "This time slot is already added.")
    else:
        selected_slots.append(slot)
        slot_listbox.insert(tk.END, slot)
        print("Selected Slot:", slot)

# GUI setup
root = tk.Tk()
root.title("Interview Slot Selection")
root.geometry("400x500")

# Calendar
cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd', mindate=date.today())
cal.pack(pady=10)

# Time selection
hour_var = tk.StringVar(value="09")
minute_var = tk.StringVar(value="00")

time_frame = ttk.Frame(root)
time_frame.pack(pady=10)

ttk.Label(time_frame, text="Hour (09–17):").grid(row=0, column=0)
hour_spin = ttk.Spinbox(time_frame, from_=9, to=17, textvariable=hour_var, width=5, format="%02.0f")
hour_spin.grid(row=0, column=1)

ttk.Label(time_frame, text="Minute:").grid(row=0, column=2)
minute_spin = ttk.Spinbox(time_frame, from_=0, to=59, increment=15, textvariable=minute_var, width=5, format="%02.0f")
minute_spin.grid(row=0, column=3)

# Add slot button
submit_btn = ttk.Button(root, text="Add Slot", command=validate_and_add_slot)
submit_btn.pack(pady=10)

# Slot listbox
ttk.Label(root, text="Selected Interview Slots:").pack()
slot_listbox = tk.Listbox(root, width=40, height=10)
slot_listbox.pack(pady=10)

root.mainloop()
