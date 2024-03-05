# import tkinter as tk
# from tkinter import messagebox

# def calculate_bmi():
#     try:
#         weight = float(weight_entry.get())
#         height = float(height_entry.get())
        
#         if weight <= 0 or height <= 0:
#             raise ValueError
        
#         bmi = weight / ((height / 100) ** 2)
#         result_label.config(text=f"BMI: {bmi:.2f}")
#     except ValueError:
#         messagebox.showerror("Error", "Please enter valid weight and height")

# # Create main window
# root = tk.Tk()
# root.title("BMI Calculator")

# # Create labels
# tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
# tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
# result_label = tk.Label(root, text="")
# result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# # Create entry fields
# weight_entry = tk.Entry(root)
# weight_entry.grid(row=0, column=1, padx=5, pady=5)
# height_entry = tk.Entry(root)
# height_entry.grid(row=1, column=1, padx=5, pady=5)

# # Create calculate button
# calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
# calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# # Run the main event loop
# root.mainloop()


import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        
        bmi = weight / (height ** 2)
        
        if bmi < 18:
            category = "Underweight"
        elif bmi >= 18 and bmi < 25:
            category = "Normal"
        else:
            category = "Overweight"
        
        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry('200x200')#fixed size
root.resizable(0,0)#fixed variance
root.configure(background='black')

# Create input fields
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=5, pady=5)

# Create button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Display the result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
