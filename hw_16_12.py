import tkinter as tk
from tkinter import messagebox
import random

# Constants
COLORS = ["red", "blue", "green", "yellow", "orange", "purple"]
BOARD_SIZE = 10

# Global variables
board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
player_color = None
computer_color = None


def initialize_board():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            board[i][j] = random.choice(COLORS)


def flood_fill(x, y, target_color, replacement_color):
    if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
        return
    if board[x][y] != target_color:
        return
    board[x][y] = replacement_color
    flood_fill(x + 1, y, target_color, replacement_color)
    flood_fill(x - 1, y, target_color, replacement_color)
    flood_fill(x, y + 1, target_color, replacement_color)
    flood_fill(x, y - 1, target_color, replacement_color)


def computer_turn():
    global computer_color
    valid_colors = [
        color for color in COLORS if color != player_color and color != computer_color
    ]
    if not valid_colors:
        return
    max_fill = 0
    best_color = None
    for color in valid_colors:
        temp_board = [row[:] for row in board]
        flood_fill(BOARD_SIZE - 1, BOARD_SIZE - 1, computer_color, color)
        fill = sum(row.count(color) for row in temp_board)
        if fill > max_fill:
            max_fill = fill
            best_color = color
    flood_fill(BOARD_SIZE - 1, BOARD_SIZE - 1, computer_color, best_color)
    computer_color = best_color
    update_board()
    check_game_over()


def player_turn(color):
    global player_color
    if color != player_color and color != computer_color:
        flood_fill(0, 0, player_color, color)
        player_color = color
        update_board()
        check_game_over()
        computer_turn()


def update_board():
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            buttons[i][j].config(bg=board[i][j])


def check_game_over():
    if all(color == player_color for row in board for color in row) or all(
        color == computer_color for row in board for color in row
    ):
        end_game()
    elif all(color != player_color for row in board for color in row) or all(
        color != computer_color for row in board for color in row
    ):
        end_game()


def end_game():
    player_score = sum(row.count(player_color) for row in board)
    computer_score = sum(row.count(computer_color) for row in board)
    result = "You win!" if player_score > computer_score else "Computer wins!"
    messagebox.showinfo("Game Over", result)
    root.quit()


# Initialize Tkinter window and buttons
root = tk.Tk()
buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        buttons[i][j] = tk.Button(
            root, width=2, command=lambda i=i, j=j: player_turn(board[i][j])
        )
        buttons[i][j].grid(row=i, column=j)

# Initialize game
initialize_board()
player_color = board[0][0]
computer_color = board[BOARD_SIZE - 1][BOARD_SIZE - 1]
update_board()

# Start game
root.mainloop()
