import csv
import os
import logging
from tkinter import Tk, filedialog, Button, Label, Entry, messagebox

# Constants
APP_TITLE = "Manabox Value Balancer"
DEFAULT_OUTPUT_FILE = 'manabox_balanced_values.csv'

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CSVProcessor:
    def __init__(self, input_file: str, output_file: str, total_purchase_price: float):
        self.input_file = input_file
        self.output_file = output_file
        self.total_purchase_price = total_purchase_price

    def read_csv(self) -> list:
        logging.info(f"Reading CSV file: {self.input_file}")
        with open(self.input_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data

    def write_csv(self, data: list):
        logging.info(f"Writing modified data to CSV file: {self.output_file}")
        with open(self.output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def modify_data(self, data: list) -> list:
        logging.info("Modifying data based on the new total purchase price.")
        header = data[0]
        purchase_price_idx = header.index("Purchase price")
        quantity_idx = header.index("Quantity")
        name_idx = header.index("Name")

        # Set non-float values in "Purchase price" to 0
        for row in data[1:]:
            try:
                float(row[purchase_price_idx])
            except ValueError:
                row[purchase_price_idx] = '0'

        total_sum = sum(float(row[purchase_price_idx]) * int(row[quantity_idx]) for row in data[1:])
        logging.info(f"Total sum of purchase prices (accounting for quantity): {total_sum}")

        if self.total_purchase_price == 0 or total_sum == 0:
            for row in data[1:]:
                row[purchase_price_idx] = '0'
        else:
            for row in data[1:]:
                original_price = float(row[purchase_price_idx])
                quantity = int(row[quantity_idx])
                name = row[name_idx]
                proportion = (original_price * quantity) / total_sum
                new_price = (proportion * self.total_purchase_price) / quantity
                row[purchase_price_idx] = f"{new_price:.2f}".rstrip('0').rstrip('.')
                proportion_percentage = proportion * 100
                logging.info(f"{name}, Original price: {original_price} * Quantity: {quantity} / Original Qty Sum: {total_sum} = Proportion: {proportion_percentage:.2f}% || {proportion_percentage:.2f}% * Actual total purchase price: {self.total_purchase_price} / Qty: {quantity} = New price: {row[purchase_price_idx]}")

        return data

    def process(self) -> bool:
        try:
            data = self.read_csv()
            modified_data = self.modify_data(data)
            self.write_csv(modified_data)
            logging.info("Conversion completed successfully!")
            return True
        except Exception as e:
            logging.error(f"An error occurred during conversion: {e}")
            messagebox.showerror("Error", f"An error occurred during conversion: {e}")
            return False

def select_input_file():
    global input_file
    input_file = filedialog.askopenfilename(title="Select input CSV file", filetypes=[("CSV files", "*.csv")])
    if input_file:
        input_label.config(text=f"Input File: {input_file}")
        logging.info(f"Selected input file: {input_file}")

def run_conversion():
    global output_file
    if not input_file:
        messagebox.showerror("Error", "Please select an input file.")
        return
    output_file = os.path.join(os.path.dirname(__file__), output_entry.get())
    if not output_file:
        messagebox.showerror("Error", "Please specify an output file.")
        return
    total_purchase_price_str = total_price_entry.get().strip()
    if not total_purchase_price_str:
        messagebox.showerror("Error", "Please enter a total purchase price.")
        return
    try:
        total_purchase_price = float(total_purchase_price_str)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid total purchase price.")
        return
    processor = CSVProcessor(input_file, output_file, total_purchase_price)
    if processor.process():
        messagebox.showinfo("Done", "Conversion completed successfully!")
        os.startfile(os.path.dirname(output_file))

if __name__ == "__main__":
    input_file = None

    root = Tk()
    root.title(APP_TITLE)

    input_button = Button(root, text="Select Input File", command=select_input_file)
    input_button.pack(pady=10)

    input_label = Label(root, text="Input File: None")
    input_label.pack(pady=5)

    output_label = Label(root, text="Output File:")
    output_label.pack(pady=5)

    output_entry = Entry(root, width=50)
    output_entry.insert(0, DEFAULT_OUTPUT_FILE)
    output_entry.pack(pady=5)

    total_price_label = Label(root, text="Total Purchase Price:")
    total_price_label.pack(pady=5)

    total_price_entry = Entry(root, width=50)
    total_price_entry.pack(pady=5)

    convert_button = Button(root, text="Run Conversion", command=run_conversion)
    convert_button.pack(pady=20)

    root.mainloop()