import pandas as pd
import re
import sys

def process_csv(input_file, output_file='cardtrader_to_manabox_output.csv'):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Rename columns
    df.rename(columns={
        'Item Name': 'card name',
        'Quantity': 'quantity',
        'Set Code': 'set code',
        'Foil/Reverse': 'foil',
        'Collector Number': 'card number',
        'Price in USD Cents': 'purchase price',
        'Condition': 'condition',
        'Language': 'language'
    }, inplace=True)
    
    # Remove unwanted columns if they exist
    columns_to_drop = ['game', 'set name', 'set released at', 'set release', 'signed', 'first edition', 'playset', 'altered']
    columns_to_drop = [col.lower() for col in columns_to_drop]
    df.columns = [col.lower() for col in df.columns]
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)
    
    # Add 'purchase currency' column with 'usd' as value for all rows
    df['purchase currency'] = 'usd'
    
    # Clean up 'card name' column
    df['card name'] = df['card name'].apply(lambda x: re.sub(r'\s*\(.*?\)\s*', '', x).strip())
    
    # Convert 'purchase price' from cents to dollars and cents
    df['purchase price'] = df['purchase price'].apply(lambda x: x / 100)
    
    # Format 'card number' column values as strings with leading zeros
    df['card number'] = df['card number'].apply(lambda x: str(x).zfill(3))
    
    # Fix promos. Append 'p' to 'card number' if 'set code' has 4 letters and starts with 'P'
    df['card number'] = df.apply(lambda row: str(row['card number']) + 'p' if len(str(row['set code'])) == 4 and str(row['set code']).startswith('P') else row['card number'], axis=1)
    
    # Fix prereleases. Append 's' to 'card number' if 'set code' has 4 letters and starts with 'S'
    df['card number'] = df.apply(lambda row: str(row['card number']) + 's' if len(str(row['set code'])) == 4 and str(row['set code']).startswith('S') else row['card number'], axis=1)
    
    # Modify 'set code' column, remove first character if there are 4
    df['set code'] = df['set code'].apply(lambda x: str(x)[1:] if len(str(x)) == 4 else str(x))
    
    # Miscellaneous set code corrections
    # Replace 'IDF' with 'DBL' for Innistrad: Double Feature
    df['set code'] = df['set code'].replace({'IDF': 'DBL'})

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python cardtrader_to_manabox.py <input_file> [<output_file>]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) == 3 else 'cardtrader_to_manabox_output.csv'
    
    process_csv(input_file, output_file)
