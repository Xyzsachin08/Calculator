import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

# Entry box to show input/output
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to update text in entry
def press(key):
    entry.insert(tk.END, key)

# Function to evaluate expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Add buttons to window
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(window, text=text, padx=20, pady=20, font=("Arial", 14), command=calculate)
    elif text == 'C':
        btn = tk.Button(window, text=text, padx=88, pady=20, font=("Arial", 14), command=clear)
        btn.grid(row=row, column=col, columnspan=4)
        continue
    else:
        btn = tk.Button(window, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

# Run the window
window.mainloop()
