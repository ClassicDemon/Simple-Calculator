import tkinter as tk

def add():
    x = float(num1.get())
    y = float(num2.get())
    result = x + y
    label_result.config(text=f"Result: {result}")

def subtract():
    x = float(num1.get())
    y = float(num2.get())
    result = x - y
    label_result.config(text=f"Result: {result}")

def multiply():
    x = float(num1.get())
    y = float(num2.get())
    result = x * y
    label_result.config(text=f"Result: {result}")

def divide():
    x = float(num1.get())
    y = float(num2.get())
    result = x / y
    label_result.config(text=f"Result: {result}")

#UI
window = tk.Tk()
window.title("Simple Calculator")

frame = tk.Frame(master=window, bg="black", padx=10)
frame.pack()

num1 = tk.Entry(master=frame, relief=tk.SUNKEN, borderwidth=3, width=30)
num1.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)

num2 = tk.Entry(master=frame, relief=tk.SUNKEN, borderwidth=3, width=30)
num2.grid(row=1, column=0, columnspan=4, ipady=2, pady=2)

button_add = tk.Button(master=frame, text="+", relief=tk.RAISED, borderwidth=3, width=5, command=add)
button_add.grid(row=0, column=4, rowspan=2, padx=2, pady=2)

button_subtract = tk.Button(master=frame, text="-", relief=tk.RAISED, borderwidth=3, width=5, command=subtract)
button_subtract.grid(row=0, column=5, rowspan=2, padx=2, pady=2)

button_multiply = tk.Button(master=frame, text="* ", relief=tk.RAISED, borderwidth=3, width=5, command=multiply)
button_multiply.grid(row=0, column=6, rowspan=2, padx=2, pady=2)

button_divide = tk.Button(master=frame, text="/", relief=tk.RAISED, borderwidth=3, width=5, command=divide)
button_divide.grid(row=0, column=7, rowspan=2, padx=2, pady=2)

label_result = tk.Label(master=frame, text="Result:")
label_result.grid(row=2, column=0, columnspan=8, pady=10)

window.mainloop()

