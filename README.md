# MTG Collection Toolkit

A collection of tools for converting Magic: The Gathering (MTG) card data between different formats.

## Table of Contents

- [Tools](#tools)
  - [Manabox to Archidekt](#manabox-to-archidekt)
  - [Cardtrader to Manabox](#cardtrader-to-manabox)
  - [Deckcheck Trim Assistant](#deckcheck-trim-assistant)
  - [Manabox Value Balancer](#manabox-value-balancer)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)

## Tools

### Manabox to Archidekt

Converts a Manabox collection export to an Archidekt import format. This tool specifically exports only binders and excludes lists and Italian Legends.

#### Usage

1. Ensure Python 3.x and the `pandas` library are installed.
2. Run the script using this command or launch in python from file explorer:

   ```sh
   python manabox_to_archidekt.py
   ```
3. Select your file to convert
4. Change output file if desired
5. Click run conversion
6. Upload output file to Archidekt
   
### Cardtrader to Manabox

This tool imports a Cardtrader order into a Manabox collection. It adjusts column names, set codes, and other format-specific details to match Manabox requirements.

#### Usage

1. Ensure Python 3.x and the `pandas` library are installed.
2. Run the script using this command or launch in python from file explorer:

   ```sh
   python cardtrader_to_manabox.py
   ```
3. Select your file to convert
4. Change output file if desired
5. Click run conversion
6. Import the output file to Manabox
   
### Deckcheck Trim Assistant

This tool helps remove cards from your deck the that Deckcheck Trim suggests to remove.

#### Usage

1. Ensure Python 3.x and the `pandas` library are installed.
2. Run the script using this command or launch in python from file explorer:

   ```sh
   python trim.py
   ```

3. Copy and paste your Deck list from the Archidekt import and the Trim List from Deckcheck into the GUI.
4. Copy and paste your updated list into Archidekt import, replacing everything existing.

### Manabox Value Balancer

ValueBalancer is a tool for assigning proportional prices to a group of cards based on their current values, making it especially useful when opening packs. Instead of dividing the cost evenly across all cards, ValueBalancer adjusts each card's price to reflect its share of the pack's total value.

For example (with easy numbers), if you open a $10 pack with 5 cards and pull:

3 cards worth $10 each
1 card worth $20
1 card worth $0

Value Balancer will set the "purchased prices" as follows:

$2 for each $10 card (3 x $2 = $6)
$4 for the $20 card (1 x $4 = $4)
$0 for the worthless card

This ensures the total cost ($10) is distributed fairly, reflecting each card's value rather than using a flat average. This approach provides more accurate tracking for trades, sales, or collection management.

Here is an example of a freshly scanned Foundations Starter Collection bundle scanned in with default pricing set, and then with the tool. 
![image](https://github.com/user-attachments/assets/2d7c4778-c157-4e41-94c8-d322ad26dc08)

#### Usage

1. Ensure Python 3.x and the `pandas` library are installed.
2. Run the script using this command or launch in python from file explorer:

   ```sh
   python value_balancer.py
   ```

3. Export your binder from Manabox as a CSV.
4. Load the CSV into the value balancer.
5. Enter the price that was paid for all of the cards in this binder total and click run conversion.
6. Import the new CSV with updated values into Manabox.
7. Delete the original binder. 

## Requirements

- Python 3.x
- `pandas` library

## Installation

### **For Windows Users Without Git Installation**

1. **Download the Repository from GitHub**
   - Go to the GitHub repository: [https://github.com/DrakeWood/MTG-CSV-Converters](https://github.com/DrakeWood/MTG-CSV-Converters).
   - Click the green **"Code"** button, then click **"Download ZIP"**.
   - Save the ZIP file to a folder on your computer.

2. **Extract the ZIP File**
   - Locate the downloaded ZIP file and right-click it.
   - Select **"Extract All"** and choose a location to extract the files.

3. **Install Python**
   - If you don’t already have Python installed, download it from the [Python website](https://www.python.org/downloads/).  
   - Run the installer and **check the box for "Add Python to PATH"** before proceeding with the installation.

4. **Install Dependencies**
   - Open a Command Prompt. Press `Win + R`, type `cmd`, and press Enter.  
   - Navigate to the extracted project folder. For example:
     ```sh
     cd C:\Users\YourUsername\Downloads\MTG-CSV-Converters-main
     ```
     Replace `YourUsername` with your Windows username and the folder path where you extracted the files.
   - Run the following command to install the necessary libraries:
     ```sh
     pip install -r requirements.txt
     ```
     
### **For Linux Users**

1. **Install Python**  
   - Most Linux distributions come with Python pre-installed. To check, run:  
     ```sh
     python3 --version
     ```  
     If not installed, you can install it using your package manager:  
     ```sh
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Install Git (if not installed)**  
   - Check if Git is installed:  
     ```sh
     git --version
     ```  
     If not, install it using your package manager:  
     ```sh
     sudo apt install git
     ```

3. **Clone the Repository**  
   - Open your terminal and run:  
     ```sh
     git clone https://github.com/DrakeWood/MTG-CSV-Converters.git
     ```  
   - Navigate into the project folder:  
     ```sh
     cd MTG-CSV-Converters
     ```

4. **Install Dependencies**  
   - Use pip to install the required libraries:  
     ```sh
     pip install -r requirements.txt
     ```

5. **Run the Script**  
   - Run the desired script with Python:  
     ```sh
     python3 script_name.py
     ```  
     Replace `script_name.py` with the name of the script you want to execute.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
