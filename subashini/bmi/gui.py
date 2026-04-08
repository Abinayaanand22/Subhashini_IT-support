import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Convert cm to meters if needed
        if height > 3:
            height = height / 100

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter valid positive values!")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db"
        elif bmi < 24.9:
            category = "Normal"
            color = "#2ecc71"
        elif bmi < 29.9:
            category = "Overweight"
            color = "#f39c12"
        else:
            category = "Obese"
            color = "#e74c3c"

        result_label.config(
            text=f"BMI: {round(bmi, 2)}\n{category}",
            fg=color
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only!")

# Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")
root.configure(bg="#eef2f3")

# Title
tk.Label(root, text="BMI Calculator", font=("Helvetica", 18, "bold"), bg="#eef2f3").pack(pady=15)

# Card frame
frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.pack(pady=10)

# Weight
tk.Label(frame, text="Weight (kg)", bg="white").pack()
weight_entry = tk.Entry(frame, font=("Arial", 12))
weight_entry.pack(pady=5)

# Height
tk.Label(frame, text="Height (cm or m)", bg="white").pack()
height_entry = tk.Entry(frame, font=("Arial", 12))
height_entry.pack(pady=5)

# Button
tk.Button(
    frame,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    width=15
).pack(pady=15)

# Result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#eef2f3")
result_label.pack(pady=10)

root.mainloop()
