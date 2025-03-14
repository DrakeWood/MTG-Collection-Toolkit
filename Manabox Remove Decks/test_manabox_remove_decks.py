import unittest
from unittest.mock import patch, mock_open
import manabox_remove_decks

class TestConvert(unittest.TestCase):

    @patch('manabox_remove_decks.read_csv')
    @patch('manabox_remove_decks.write_csv')
    @patch('builtins.open', new_callable=mock_open)
    def test_main(self, mock_open, mock_write_csv, mock_read_csv):
        mock_read_csv.return_value = [
            ['Binder Name', 'Set code', 'Set name', 'Binder Type'],
            ['Test Deck', 'DECK', 'Test Deck Name', 'deck'],
            ['Italian Legends', 'LEGI', 'Legends Italian', 'list'],
            ['Other Binder', 'SET1', 'Set One', 'binder'],
            ['Another Binder', 'SET2', 'Set Two', 'binder']
        ]

        # Call the main function
        manabox_remove_decks.main('input.csv', 'output.csv')

        # Check if read_csv was called with the correct input file
        mock_read_csv.assert_called_once_with('input.csv')

        # Expected data excludes binder types "deck" and "list"
        expected_modified_data = [
            ['Binder Name', 'Set code', 'Set name', 'Binder Type'],
            ['Other Binder', 'SET1', 'Set One', 'binder'],
            ['Another Binder', 'SET2', 'Set Two', 'binder']
        ]

        # Verify that none of the rows (except header) in output have binder type "deck" or "list"
        for row in expected_modified_data[1:]:
            self.assertNotIn(row[3].lower(), ['deck', 'list'])

        # Check if write_csv was called with the correct output file and modified data
        mock_write_csv.assert_called_once_with('output.csv', expected_modified_data)

if __name__ == "__main__":
    unittest.main()