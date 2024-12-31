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
