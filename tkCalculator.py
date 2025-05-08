import tkinter as tk
from tkinter import messagebox

# Function to update expression
def press(symbol):
    current = input_var.get()
    input_var.set(current + str(symbol))

# Function to clear input
def clear():
    input_var.set("")
    result_var.set("")

# Function to evaluate the expression
def calculate():
    try:
        expression = input_var.get().replace('×', '*').replace('÷', '/')
        result = eval(expression)
        result_var.set(f"= {result}")
    except ZeroDivisionError:
        result_var.set("Error: ÷0")
    except Exception:
        result_var.set("Invalid Expression")

# Initialize main window
root = tk.Tk()
root.title("Mobile Calculator")
root.geometry("320x450")
root.resizable(False, False)
root.configure(bg="#222831")

input_var = tk.StringVar()
result_var = tk.StringVar()

# Display area
display_frame = tk.Frame(root, height=100, bg="#222831")
display_frame.pack(expand=True, fill="both")

input_display = tk.Label(display_frame, textvariable=input_var, anchor="e",
                         bg="#222831", fg="white", font=("Helvetica", 24))
input_display.pack(expand=True, fill="both", padx=10)

result_display = tk.Label(display_frame, textvariable=result_var, anchor="e",
                          bg="#222831", fg="#00ffcc", font=("Helvetica", 18))
result_display.pack(expand=True, fill="both", padx=10)

# Button layout
buttons = [
    ['C', '%', '÷', '×'],
    ['7', '8', '9', '-'],
    ['4', '5', '6', '+'],
    ['1', '2', '3', '='],
    ['0', '.', '', '']
]

# Button frame
btn_frame = tk.Frame(root, bg="#393e46")
btn_frame.pack(expand=True, fill="both")

# Create buttons
for row_index, row in enumerate(buttons):
    for col_index, symbol in enumerate(row):
        if symbol == '':
            continue
        btn = tk.Button(btn_frame, text=symbol, font=("Helvetica", 18, "bold"),
                        bg="#00adb5" if symbol not in ('C', '=', '+', '-', '×', '÷') else
                        ("#ff5722" if symbol == 'C' else "#00796b" if symbol == '=' else "#30475e"),
                        fg="white", borderwidth=0,
                        command=(clear if symbol == 'C' else
                                 calculate if symbol == '=' else
                                 lambda s=symbol: press(s)))
        btn.grid(row=row_index, column=col_index, sticky="nsew", padx=1, pady=1)

# Make grid cells expand equally
for i in range(5):
    btn_frame.rowconfigure(i, weight=1)
for i in range(4):
    btn_frame.columnconfigure(i, weight=1)

# Run the application
root.mainloop()
