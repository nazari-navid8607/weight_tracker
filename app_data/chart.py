import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Load and prepare your data
df = pd.read_csv("app_data/info.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y", errors="coerce")
df.dropna(subset=["Date"], inplace=True)
df.set_index("Date", inplace=True)

metrics = ["Weight", "Calories", "Cardio", "PushUps"]
current_index = 0

# Create main window
root = tk.Tk()
root.title("📊 Health Chart Viewer")
root.geometry("900x600")

# Frame for chart
chart_frame = tk.Frame(root)
chart_frame.pack(expand=True, fill=tk.BOTH)

# Function to draw chart
def draw_chart(index):
    metric = metrics[index]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(df.index, df[metric], marker='o', label=metric)
    ax.set_title(f"{metric} Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel(metric)
    ax.grid(True)
    ax.legend()

    # Clear previous chart
    for widget in chart_frame.winfo_children():
        widget.destroy()

    # Embed chart in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)

# Navigation functions
def next_chart():
    global current_index
    current_index = (current_index + 1) % len(metrics)
    draw_chart(current_index)

def prev_chart():
    global current_index
    current_index = (current_index - 1) % len(metrics)
    draw_chart(current_index)

# Frame for buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="⬅ Back", command=prev_chart, width=10).pack(side=tk.LEFT, padx=20)
tk.Button(btn_frame, text="Next ➡", command=next_chart, width=10).pack(side=tk.RIGHT, padx=20)

# Initial chart
draw_chart(current_index)

# Run the app
root.protocol("WM_DELETE_WINDOW", root.quit)
root.mainloop()