import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

# Display
entry = tk.Entry(window, font=("Arial", 24), justify="right")
entry.pack(fill="both", padx=10, pady=10)

# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

frame = tk.Frame(window)
frame.pack()

for i, button in enumerate(buttons):
    if button == "=":
        command = calculate
    else:
        command = lambda x=button: entry.insert(tk.END, x)

    tk.Button(
        frame,
        text=button,
        font=("Arial", 18),
        width=5,
        height=2,
        command=command
    ).grid(row=i // 4, column=i % 4)

window.mainloop()
