import tkinter as tk
from tkinter import messagebox
import re

# Common SQL injection patterns
sql_patterns = [
    r"(?i)(\bOR\b|\bAND\b)\s+\d+=\d+",  # e.g., OR 1=1
    r"(?i)(\bUNION\b\s+\bSELECT\b)",    # UNION SELECT
    r"(?i)(--|#)",                      # SQL comment
    r"(?i)(\bDROP\b|\bDELETE\b|\bINSERT\b|\bUPDATE\b)",  # DDL/DML keywords
    r"'|\""                             # quotes
]

def detect_sql_injection(input_text):
    for pattern in sql_patterns:
        if re.search(pattern, input_text):
            return True
    return False

def on_submit():
    user_input = entry.get()
    if detect_sql_injection(user_input):
        messagebox.showwarning("Warning", "⚠️ Potential SQL Injection Detected!")
    else:
        messagebox.showinfo("Safe", "✅ Input looks clean.")

# GUI setup
root = tk.Tk()
root.title("SQL Injection Detector")
root.geometry("400x200")

label = tk.Label(root, text="Enter input:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

submit_btn = tk.Button(root, text="Check", command=on_submit)
submit_btn.pack(pady=10)

root.mainloop()
