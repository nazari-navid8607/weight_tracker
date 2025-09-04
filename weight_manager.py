import tkinter as tk
import subprocess
import os
import platform

def open_Data_processor():
    subprocess.Popen(["python", "app_data/data_processor.py"])

def open_chart():
    subprocess.Popen(["python", "app_data/chart.py"])

def open_info():
    if platform.system() == "Windows":
        os.startfile("app_data\\info.csv")
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", "app_data/info.csv"])
    else:  # Linux
        subprocess.Popen(["xdg-open", "app_data/info.csv"])



root = tk.Tk()
root.title("Weight Tracker")
root.geometry("400x300")
root.configure(bg="lightblue")
data_processor = tk.Button(root, text="Data Processor", font=("Arial", 26), width=16, command=open_Data_processor, bg="orange")
data_processor.pack(pady=12)
chart = tk.Button(root, text="Open Chart", font=("Arial", 26), width=16, command=open_chart , bg="orange")
chart.pack(pady=12)
info = tk.Button(root, text="Open Info.csv", font=("Arial", 26), width=16, command=open_info  , bg="orange")
info.pack(pady=12)
root.mainloop()