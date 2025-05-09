# 📅 Interview Slot Picker (Tkinter GUI)

This is a Python-based GUI application built using **Tkinter** and **tkcalendar**, designed for scheduling interview call slots. The app allows users to select multiple time slots when they are available, with various restrictions to ensure valid scheduling.

---

## 🖥️ Features

- ✅ Calendar widget to select a **date**.
- ✅ Only **weekdays (Monday–Friday)** can be selected — weekends are disabled.
- ✅ Time selection using spinboxes with **15-minute intervals**.
- ✅ Only **office hours (09:00 to 17:00)** are allowed.
- ✅ No past date or time can be selected.
- ✅ Users can select **multiple time slots** for interview availability.
- ✅ Already added slots are shown in a list and printed to the console.
- ✅ Duplicate slots are prevented.

---

## 🚀 Requirements

- Python 3.x
- `tkcalendar` library

Install the required package:

```bash
pip install -r requirements.txt
