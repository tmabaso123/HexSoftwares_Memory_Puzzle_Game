import unittest
from unittest.mock import patch
import tkinter as tk
from tkinter import messagebox
from game.MemoryPuzzleGame import MemoryPuzzleGame

class TestMemoryPuzzleGame(unittest.TestCase):
    """
    Unit tests for the MemoryGame class.
    """

    def setUp(self):
        """
        Set up the test environment by creating a MemoryPuzzleGame instance.
        """
        self.root = tk.Tk()
        self.game = MemoryPuzzleGame(self.root)

    def test_initial_setup(self):
        """
        Test that the game initializes correctly.
        """
        self.assertEqual(len(self.game.buttons), 4)
        self.assertEqual(len(self.game.buttons[0]), 3)
        self.assertEqual(self.game.matched_pairs, 0)
        

    def test_reveal_tile(self):
        """
        Test that revealing a tile works as expected.
        """
        self.game.reveal_tile(0, 0)
        btn, value = self.game.buttons[0][0]
        self.assertEqual(btn.cget("text"), value)
        self.assertEqual(btn.cget("state"), "disabled")

    def test_match_logic(self):
        """
        Simulate a match and test the game's matching logic.
        """
        self.game.first_pick = (0, 0)
        self.game.buttons[0][0][0].config(text=self.game.tile_values[0])
        self.game.second_pick = (0, 1)
        self.game.buttons[0][1][0].config(text=self.game.tile_values[1])

        if self.game.tile_values[0] == self.game.tile_values[1]:
            self.game.check_match()
            self.assertEqual(self.game.matched_pairs, 1)
        else:
            self.game.check_match()
            self.assertEqual(self.game.matched_pairs, 0)

    @patch('tkinter.messagebox.showinfo')  # Mock showinfo method
    def test_end_game(self, mock_showinfo):
        """
        Test the end_game method to ensure it works correctly.
        """
        self.game.end_game("Test Message")
        mock_showinfo.assert_called_with("Game Over", "Test Message")

    def tearDown(self):
        """
        Destroy the test environment.
        """
        self.root.destroy()

if __name__== "__main__":
    unittest.main()

