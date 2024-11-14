import unittest
import pandas as pd
from io import StringIO
from cardtrader_to_manabox import process_csv

class TestProcessCSV(unittest.TestCase):

    def setUp(self):
        # Sample input CSV data
        self.input_csv = StringIO("""Item Name,Quantity,Set Name,Set Code,Foil/Reverse,Collector Number,Price in USD Cents,Condition,Language,game,set release,signed,first edition,playset
        Card A (Collectors),2,Set A,C234,Foil,001,100,Near Mint,English,Game A,2021-01-01,No,No,No
        Card B,1,Set B,5678,,002,200,Good,Japanese,Game B,2021-02-01,No,No,No
        Card C (Promo),1,Set C,P123,Foil,003,300,Good,English,Game C,2021-03-01,No,No,No
        Card D,1,Set D,S123,,004,400,Good,English,Game D,2021-04-01,No,No,No
        Card E (Prerelease),1,Set C,S123,Foil,003,300,Good,English,Game C,2021-03-01,No,No,No
        """)
        
        # Expected output CSV data
        self.expected_output_csv = """card name,quantity,set code,foil,card number,purchase price,condition,language,purchase currency
Card A,2,234,Foil,001,1.0,Near Mint,English,usd
Card B,1,678,,002,2.0,Good,Japanese,usd
Card C,1,123,Foil,003p,3.0,Good,English,usd
Card D,1,123,,004s,4.0,Good,English,usd
Card E,1,123,Foil,003s,3.0,Good,English,usd
        """

    def test_process_csv(self):
        # Create a temporary output CSV file
        output_csv = StringIO()
        
        # Process the CSV data
        try:
            process_csv(self.input_csv, output_csv)
        except Exception as e:
            self.fail(f"process_csv raised an exception: {e}")
        
        # Move to the beginning of the StringIO object
        output_csv.seek(0)
        
        # Read the processed CSV data
        output_df = pd.read_csv(output_csv)
        
        # Create a DataFrame from the expected output CSV data
        expected_output_df = pd.read_csv(StringIO(self.expected_output_csv))
        
        # Assert that the processed DataFrame matches the expected DataFrame
        pd.testing.assert_frame_equal(output_df, expected_output_df)

if __name__ == '__main__':
    unittest.main()
