import tkinter as tk
from datetime import datetime
now = datetime.now()
date = now.strftime(r"%m/%d/%Y")

variable_names = ["Weight", "Calories", "Cardio", "PushUps"]
variable_values = []
current_index = 0

def on_enter(event=None):
    global current_index
    value = entry.get()
    variable_values.append(value)
    entry.delete(0, tk.END)
    current_index += 1
    if current_index < len(variable_names):
        label.config(text=f"Enter {variable_names[current_index]}:")
    else:
        root.geometry("330x360")
        global Weight, Calories, Cardio, PushUps
        Weight, Calories, Cardio, PushUps = variable_values
        label.config(text=f"Information collected\n\nWeight: {Weight} kg\nCalories: {Calories} Cal\nCardio: {Cardio} mins\nPushUps: {PushUps}\n\nPress Enter to exit")
        entry.pack_forget()
        def quit(event=None):
            root.destroy()
        entry.bind('<Return>', quit)

            
        
        with open("app_data/info.csv", "a") as file:
            file.write(f"\n{date},{Weight},{Calories},{Cardio},{PushUps}")

root = tk.Tk()
root.title("Health Manager")
root.geometry("330x200")
root.configure(bg="lightblue")
label = tk.Label(root, text=f"Enter {variable_names[current_index]}:", font=("Arial", 22), bg="lightblue")
label.pack(pady=30)

entry = tk.Entry(root, width=16, font=("Arial", 20))
entry.pack(pady=10)
entry.focus_set()
entry.bind('<Return>', on_enter)

root.mainloop()