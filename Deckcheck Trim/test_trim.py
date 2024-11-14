import unittest
from unittest.mock import MagicMock
import tkinter as tk
from tkinter import scrolledtext
from trim import update_list

class TestTrimFunction(unittest.TestCase):
    def setUp(self):
        self.window = tk.Tk()
        self.main_text_box = scrolledtext.ScrolledText(self.window)
        self.match_text_box = scrolledtext.ScrolledText(self.window)
        self.output_text_box = scrolledtext.ScrolledText(self.window)
        
        # Mocking the text boxes in the update_list function
        global main_text_box, match_text_box, output_text_box
        main_text_box = self.main_text_box
        match_text_box = self.match_text_box
        output_text_box = self.output_text_box

    def tearDown(self):
        self.window.destroy()

    def test_update_list(self):
        # Setting up the input text
        self.main_text_box.insert(tk.END, "4x Card A (set) [Sideboard]\n2x Card B\n1x Card C (set) [Sideboard]")
        self.match_text_box.insert(tk.END, "Card A: Inferior to other mana rocks in the deck\nCard C: Not needed")
        
        # Running the function to be tested
        trimmed_count = update_list(self.main_text_box, self.match_text_box, self.output_text_box)
        
        # Getting the output text
        output = self.output_text_box.get("1.0", tk.END).strip()
        
        # Expected output
        expected_output = "4x Card A (set) [Trimmed{noDeck}{noPrice}]\n2x Card B\n1x Card C (set) [Trimmed{noDeck}{noPrice}]"
        
        # Asserting the output
        self.assertEqual(output, expected_output)
        
        # Asserting the number of trimmed cards
        self.assertEqual(trimmed_count, 2)

if __name__ == '__main__':
    unittest.main()