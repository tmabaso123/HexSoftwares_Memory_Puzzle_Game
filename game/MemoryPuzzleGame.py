import tkinter as tk
import random
from tkinter import messagebox

# Constants
tile_values = list('AABBCCDDEEFFGGHHIIJJ')  
time_limit = 60  # Time limit in seconds

class MemoryPuzzleGame:
    """
    A class representing the Memory Puzzle Game.

    Attributes:
        root (tk.Tk): The root window for the game.
        buttons (list): A 2D list of button widgets and their corresponding values.
        first_pick (tuple): The first tile selected by the player (row, col).
        second_pick (tuple): The second tile selected by the player (row, col).
        matched_pairs (int): The number of pairs successfully matched.
        time_left (int): The remaining time for the game in seconds.
        timer_label (tk.Label): Label widget to display the timer.
        board_frame (tk.Frame): Frame widget containing the game board.
    """

    def __init__(self, root):
        """
        Initialize the Memory Puzzle Game.

        Args:
            root (tk.Tk): The root window for the game.
        """
        self.root = root
        self.root.title("Memory Puzzle Game")

        # Shuffle the tile values
        random.shuffle(tile_values)

        # Create the board
        self.buttons = []
        self.first_pick = None
        self.second_pick = None
        self.matched_pairs = 0
        self.time_left = time_limit

        self.timer_label = tk.Label(root, text=f"Time left: {self.time_left}s", font=("Arial", 14))
        self.timer_label.pack()

        self.board_frame = tk.Frame(root)
        self.board_frame.pack()

        for i in range(4):
            row = []
            for j in range(3):
                btn = tk.Button(self.board_frame, text="", width=6, height=3, command=lambda r=i, c=j: self.reveal_tile(r, c))
                btn.grid(row=i, column=j)
                row.append((btn, tile_values[i * 3 + j]))
            self.buttons.append(row)

        self.start_timer()

    def start_timer(self):
        """
        Start the countdown timer for the game.

        Decreases the time_left attribute every second and ends the game if time runs out.
        """
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.root.after(1000, self.start_timer)
        else:
            self.end_game("Time's up! You lost.")

    def reveal_tile(self, row, col):
        """
        Reveal the tile at the specified position.

        Parameters:
            row (int): The row index of the tile.
            col (int): The column index of the tile.
        """
        if self.first_pick and self.second_pick:
            return

        button, value = self.buttons[row][col]

        if not button.cget("state") == "normal":
            return

        button.config(text=value, state="disabled")

        if not self.first_pick:
            self.first_pick = (row, col)
        elif not self.second_pick:
            self.second_pick = (row, col)
            self.root.after(500, self.check_match)

    def check_match(self):
        """
        Check if the two selected tiles match.

        Updates the game state based on whether the tiles match or not.
        """
        r1, c1 = self.first_pick
        r2, c2 = self.second_pick
        
        btn1, val1 = self.buttons[r1][c1]
        btn2, val2 = self.buttons[r2][c2]

        if val1 == val2:
            self.matched_pairs += 1
            if self.matched_pairs == len(tile_values) // 2:
                self.end_game("Congratulations! You matched all pairs!")
        else:
            btn1.config(text="", state="normal")
            btn2.config(text="", state="normal")

        self.first_pick = None
        self.second_pick = None

    def end_game(self, message):
        """
        End the game and display a message to the player.

        Parameters:
            message (str): The message to display in the game over dialog.
        """
        messagebox.showinfo("Game Over", message)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryPuzzleGame(root)
    root.mainloop()
