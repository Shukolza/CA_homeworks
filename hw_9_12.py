import random
import tkinter as tk
from tkinter import ttk

numbers = list(range(1, 16))  # More efficient way to create the number list
latest_number = 0

main_window = tk.Tk()
main_window.title("MADE BY SHUKOLZA")
main_window.geometry("600x600")


def reverse_game():
    reversed_game = True
    for button in buttons:
        if button["bg"] == "green":
            button.config(bg="white", state="normal")
        elif button["bg"] == "white":
            button.config(bg="green", state="disabled")


def button_click(but):
    global latest_number
    try:
        button_value = int(but["text"])
        if button_value - latest_number == 1:
            but.config(bg="green", state="disabled")
            latest_number = button_value
        else:
            but.config(bg="red", state="disabled")
            main_window.after(
                1000, lambda: but.config(bg="white", state="normal")
            )  # Use after for delay
    except Exception as e:
        print(f"An error occurred: {e}")


def r_button_click(but):
    global latest_number
    try:
        button_value = int(but["text"])
        if button_value - latest_number == 1:
            but.config(bg="green", state="disabled")
            latest_number = button_value
        else:
            but.config(bg="red", state="disabled")
            main_window.after(
                1000, lambda: but.config(bg="white", state="normal")
            )  # Use after for delay
    except Exception as e:
        print(f"An error occurred: {e}")


que_choose = ttk.Checkbutton(text="Развернуть игру", command=reverse_game)

que_choose.pack()

random.shuffle(numbers)  # Shuffle the numbers BEFORE creating buttons

buttons = []
for number in numbers:
    button = tk.Button(main_window, text=number)
    button["command"] = lambda b=button: button_click(b)
    button.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    buttons.append(button)

main_window.mainloop()
