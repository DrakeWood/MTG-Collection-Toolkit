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
    header = data[0]
    binder_type_idx = header.index("Binder Type")
    # Filter out rows where binder type is 'deck' or 'list' (case insensitive)
    filtered_data = [row for row in data if row[binder_type_idx].lower() not in ["deck", "list"]]
    total_rows = len(data)
    removed_rows = total_rows - len(filtered_data)
    
    print(f"Total rows: {total_rows}")
    print(f"Removed deck and list rows: {removed_rows}")
    
    return filtered_data

def process_csv(input_file, output_file='manabox_remove_decks_output.csv'):
    try:
        data = read_csv(input_file)
        modified_data = modify_data(data)
        df = pd.DataFrame(modified_data[1:], columns=modified_data[0])
        
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
        # Set default output file name based on input file name
        base = os.path.splitext(os.path.basename(input_file))[0]
        default_output = f"{base}_output.csv"
        output_entry.delete(0, "end")
        output_entry.insert(0, default_output)

def run_conversion():
    global output_file
    if not input_file:
        messagebox.showerror("Error", "Please select an input file.")
        return
    out_name = output_entry.get().strip()
    if not out_name:
        base = os.path.splitext(os.path.basename(input_file))[0]
        out_name = f"{base}_output.csv"
        output_entry.insert(0, out_name)
    output_file = os.path.join(os.path.dirname(input_file), out_name)
    if process_csv(input_file, output_file):
        messagebox.showinfo("Done", "Conversion completed successfully!")
        os.startfile(os.path.dirname(output_file))

def main(input_file='input.csv', output_file='manabox_remove_decks_output.csv'):
    data = read_csv(input_file)
    modified_data = modify_data(data)
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
    output_entry.insert(0, 'manabox_remove_decks_output.csv')
    output_entry.pack(pady=5)

    convert_button = Button(root, text="Run Conversion", command=run_conversion)
    convert_button.pack(pady=20)

    root.mainloop()