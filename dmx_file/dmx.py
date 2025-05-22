import tkinter as tk
from tkinter import messagebox


def percent_to_dmx(percent_str):
    try:
        if "-" in percent_str:
            start, end = map(float, percent_str.strip('%').split('-'))
            start_dmx = round((start / 100) * 255)
            end_dmx = round((end / 100) * 255)
            return f"DMX Range: {start_dmx} - {end_dmx}"
        else:
            value = float(percent_str.strip('%'))
            dmx = round((value / 100) * 255)
            return f"DMX Value: {dmx}"
    except ValueError:
        return "Invalid input format. Use format like 41% or 2-4%."


def calculate():
    input_str = entry.get().strip()
    result = percent_to_dmx(input_str)
    result_label.config(text=result)


# GUI setup
root = tk.Tk()
root.title("Lightkey DMX Calculator")

tk.Label(root, text="Enter % or Range (e.g., 41% or 2-4%)").pack(pady=10)
entry = tk.Entry(root, width=20)
entry.pack(pady=5)

tk.Button(root, text="Convert", command=calculate).pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
