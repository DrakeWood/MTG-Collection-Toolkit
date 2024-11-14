import csv
import pandas as pd
import re
import sys
from tkinter import Tk, filedialog, Button, Label, Entry, messagebox
import os

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def write_csv(file_path, data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def modify_data(data):
    # Find the indices of the relevant columns
    header = data[0]
    binder_name_idx = header.index("Binder Name")
    set_code_idx = header.index("Set code")
    set_name_idx = header.index("Set name")
    binder_type_idx = header.index("Binder Type")

    # Filter the data based on the new criteria
    filtered_data = [row for row in data if row[binder_name_idx] != "Italian Legends" and row[set_code_idx] != "LEGI" and row[set_name_idx] != "Legends Italian" and row[binder_type_idx] != "list"]
    # Collect some stats
    total_rows = len(data)
    removed_rows = total_rows - len(filtered_data)
    
    italian_legends_count1 = 0
    italian_legends_count2 = 0
    italian_legends_count3 = 0

    for row in data:
        if row[binder_name_idx] == "Italian Legends":
            italian_legends_count1 += 1
        elif "LEGI" in row[set_code_idx]:
            italian_legends_count2 += 1
        elif "Legends Italian" in row[set_name_idx]:
            italian_legends_count3 += 1
    combined_count = italian_legends_count1 + italian_legends_count2 + italian_legends_count3
    list_count = sum(1 for row in data if row[1] == "list")
    
    print(f"Total rows: {total_rows}")
    print(f"Removed rows: {removed_rows}")
    print(f"'Italian Legends': {combined_count}")
    print(f"'list': {list_count}")
    
    modified_data = filtered_data
    return modified_data

def process_csv(input_file, output_file='manabox_to_archidekt_output.csv'):
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Rename columns
        df.rename(columns={
            'Binder Name': 'binder_name',
            'Binder Type': 'binder_type',
            'Name': 'name',
            'Set code': 'set_code',
            'Set name': 'set_name',
            'Collector number': 'collector_number',
            'Foil': 'foil',
            'Rarity': 'rarity',
            'Quantity': 'quantity',
            'ManaBox ID': 'manabox_id',
            'Scryfall ID': 'scryfall_id',
            'Purchase price': 'purchase_price',
            'Misprint': 'misprint',
            'Altered': 'altered',
            'Condition': 'condition',
            'Language': 'language',
            'Purchase price currency': 'purchase_price_currency'
        }, inplace=True)
        
        # Save the updated DataFrame to a new CSV file
        df.to_csv(output_file, index=False)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during conversion: {e}")
        return False

def select_input_file():
    global input_file
    input_file = filedialog.askopenfilename(title="Select input CSV file", filetypes=[("CSV files", "*.csv")])
    if input_file:
        input_label.config(text=f"Input File: {input_file}")

def run_conversion():
    global output_file
    if not input_file:
        messagebox.showerror("Error", "Please select an input file.")
        return
    output_file = os.path.join(os.path.dirname(__file__), output_entry.get())
    if not output_file:
        messagebox.showerror("Error", "Please specify an output file.")
        return
    if process_csv(input_file, output_file):
        messagebox.showinfo("Done", "Conversion completed successfully!")
        os.startfile(os.path.dirname(output_file))

def main(input_file='input.csv', output_file='manabox_to_archidekt_output.csv'):
    # Read the CSV file
    data = read_csv(input_file)
    
    # Modify the data
    modified_data = modify_data(data)
    
    # Write the modified data to a new CSV file
    write_csv(output_file, modified_data)

if __name__ == "__main__":
    input_file = None

    root = Tk()
    root.title("Manabox to Archidekt Converter")

    input_button = Button(root, text="Select Input File", command=select_input_file)
    input_button.pack(pady=10)

    input_label = Label(root, text="Input File: None")
    input_label.pack(pady=5)

    output_label = Label(root, text="Output File:")
    output_label.pack(pady=5)

    output_entry = Entry(root, width=50)
    output_entry.insert(0, 'manabox_to_archidekt_output.csv')
    output_entry.pack(pady=5)

    convert_button = Button(root, text="Run Conversion", command=run_conversion)
    convert_button.pack(pady=20)

    root.mainloop()