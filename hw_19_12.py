import tkinter as tk
from tkinter import ttk, messagebox

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        result = self.num1 + self.num2
        messagebox.showinfo("Result", f"The sum is: {result}")

    def minus(self):
        result = self.num1 - self.num2
        messagebox.showinfo("Result", f"The difference is: {result}")

    def multiply(self):
        result = self.num1 * self.num2
        messagebox.showinfo("Result", f"The product is: {result}")

    def divide(self):
        try:
            result = self.num1 / self.num2
            messagebox.showinfo("Result", f"The quotient is: {result}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero")

def calculate():
    try:
        number1 = int(num1.get())
        number2 = int(num2.get())
        calc = Calculator(number1, number2)
        operation = operation_var.get()
        if operation == "+":
            calc.plus()
        elif operation == "-":
            calc.minus()
        elif operation == "*":
            calc.multiply()
        elif operation == "/":
            calc.divide()
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

main_window = tk.Tk()
main_window.geometry("500x500")
main_window.title("Calculator")

num1 = ttk.Entry()
num2 = ttk.Entry()
operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(main_window)
operation_var.set(operations[0])
operation_menu = ttk.OptionMenu(main_window, operation_var, *operations)
calculate_button = ttk.Button(text="Calculate", command=calculate)

num1.grid(row=0, column=0)
num2.grid(row=1, column=0)
operation_menu.grid(row=0, column=1)
calculate_button.grid(row=1, column=1)

main_window.mainloop()