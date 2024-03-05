import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            raise ValueError
        
        bmi = weight / ((height / 100) ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid weight and height")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")

# Create labels
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create entry fields
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
