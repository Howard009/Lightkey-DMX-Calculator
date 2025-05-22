# Lightkey-DMX-Calculator
A simple, clean desktop tool built with Python and Tkinter to convert percentage values (0–100%) to DMX channel values (0–255), specifically useful for controlling lighting software like **Lightkey**.

## ✨ Features

- ✅ Enter a percentage (e.g. `41%`) or range (`2–4%`)
- ✅ Converts instantly to the corresponding DMX value or range
- ✅ Stylish dark mode UI
- ✅ Copy result to clipboard with one click
- ✅ Keeps a **history of the last 10 results**
- ✅ Option to clear history

---

## 📸 Screenshot

![Screenshot](screenshot.png) <!-- Optional: Add a screenshot to your repo -->

---

## ⚙️ How It Works

Lightkey often uses percentage values, but DMX hardware expects values between 0 and 255.

This tool converts:
- `41% → 104`
- `2–4% → 5–10`

**Formula used**:
```python
DMX = round((percent / 100) * 255)
