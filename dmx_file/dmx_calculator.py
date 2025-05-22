import tkinter as tk
from tkinter import messagebox

# History list
history = []


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
        return "Invalid input. Use format like 41% or 2-4%."


def calculate(event=None):
    input_str = entry.get().strip()
    result = percent_to_dmx(input_str)
    result_label.config(text=result)
    add_to_history(f"{input_str} → {result}")


def add_to_history(item):
    if len(history) >= 10:
        history.pop(0)
    history.append(item)
    update_history_display()


def update_history_display():
    history_text.config(state=tk.NORMAL)
    history_text.delete(1.0, tk.END)
    for entry in reversed(history):
        history_text.insert(tk.END, entry + "\n")
    history_text.config(state=tk.DISABLED)


def copy_to_clipboard():
    result = result_label.cget("text")
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        messagebox.showinfo("Copied", "Result copied to clipboard!")


def clear_history():
    history.clear()
    update_history_display()


# GUI setup
root = tk.Tk()
root.title("Lightkey DMX Calculator")
root.geometry("600x250")
root.configure(bg="#1e1e1e")

font_main = ("Segoe UI", 12)
font_result = ("Segoe UI", 12, "bold")

# Main input area
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(side=tk.LEFT, padx=20, pady=20)

tk.Label(input_frame, text="Enter % or Range (e.g. 41% or 2-4%)",
         bg="#1e1e1e", fg="#ffffff", font=font_main).pack(pady=(0, 5))

entry = tk.Entry(input_frame, font=font_main, justify="center", width=20)
entry.pack(pady=5)
entry.bind("<Return>", calculate)

tk.Button(input_frame, text="Convert", font=font_main,
          command=calculate).pack(pady=5)
tk.Button(input_frame, text="Copy Result", font=font_main,
          command=copy_to_clipboard).pack(pady=5)

result_label = tk.Label(input_frame, text="",
                        font=font_result, bg="#1e1e1e", fg="#00ff88")
result_label.pack(pady=10)

# History panel
history_frame = tk.Frame(root, bg="#2a2a2a", width=200)
history_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=20)

tk.Label(history_frame, text="History", bg="#2a2a2a",
         fg="#ffffff", font=("Segoe UI", 12, "bold")).pack()

history_text = tk.Text(history_frame, width=30, height=10,
                       state=tk.DISABLED, bg="#333333", fg="#ffffff", font=("Consolas", 10))
history_text.pack(pady=5)

tk.Button(history_frame, text="Clear History", font=(
    "Segoe UI", 10), command=clear_history).pack(pady=(5, 0))

root.mainloop()
