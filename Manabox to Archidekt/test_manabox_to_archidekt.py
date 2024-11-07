import unittest
from unittest.mock import patch, mock_open
import manabox_to_archidekt

class TestConvert(unittest.TestCase):

    @patch('manabox_to_archidekt.read_csv')
    @patch('manabox_to_archidekt.write_csv')
    @patch('builtins.open', new_callable=mock_open)
    def test_main(self, mock_open, mock_write_csv, mock_read_csv):
        # Mock the data returned by read_csv
        mock_read_csv.return_value = [
            ['Binder Name', 'Set code', 'Set name', 'Binder Type'],
            ['Italian Legends', 'LEGI', 'Legends Italian', 'list'],
            ['Other Binder', 'SET1', 'Set One', 'normal'],
            ['Another Binder', 'SET2', 'Set Two', 'normal']
        ]

        # Call the main function
        manabox_to_archidekt.main('input.csv', 'output.csv')

        # Check if read_csv was called with the correct input file
        mock_read_csv.assert_called_once_with('input.csv')

        # Check if write_csv was called with the correct output file and modified data
        expected_modified_data = [
            ['Binder Name', 'Set code', 'Set name', 'Binder Type'],
            ['Other Binder', 'SET1', 'Set One', 'normal'],
            ['Another Binder', 'SET2', 'Set Two', 'normal']
        ]
        mock_write_csv.assert_called_once_with('output.csv', expected_modified_data)

if __name__ == "__main__":
    unittest.main()