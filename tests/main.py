import unittest

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
        self.assertEqual(self.game.time_left, time_limit)


    def test_reveal_tile(self):
        """
        Test that revealing a tile works as expected.
        """
        self.game.reveal_tile(0, 0)
        btn, value = self.game.buttons[0][0]
        self.assertEqual(btn.cget("text"), value)
        self.assertEqual(btn.cget("state"), "disabled")
