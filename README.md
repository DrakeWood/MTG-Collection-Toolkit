# MTG CSV Converters

A collection of tools for converting Magic: The Gathering (MTG) card data between different formats.

## Table of Contents

- [Converters](#converters)
  - [Manabox to Archidekt](#manabox-to-archidekt)
  - [Cardtrader to Manabox](#cardtrader-to-manabox)
  - [Deckcheck Trim assistant](#deckcheck-trim)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)

## Converters

### Manabox to Archidekt

Converts a Manabox collection export to an Archidekt import format. This tool specifically exports only binders and excludes lists and Italian Legends.

#### Usage

1. Ensure Python 3.x and the `pandas` library are installed.
2. Run the script using this command or launch in python from file explorer:

   ```sh
   python manabox_to_archidekt.py sample_manabox_export.csv output.csv
   ```

   - Optionally, specify an output file name.

### Cardtrader to Manabox

This tool imports a Cardtrader order into a Manabox collection. It adjusts column names, set codes, and other format-specific details to match Manabox requirements.

#### Usage

1. Ensure Python 3.x and the `pandas` library are installed.
2. Run the script using this command or launch in python from file explorer:

   ```sh
   python cardtrader_to_manabox.py
   ```

   - Optionally, specify an output file name.

### Deckcheck Trim Assistant

1. Ensure Python 3.x and the `pandas` library are installed.
2. Run the script using this command or launch in python from file explorer:

   ```sh
   python trim.py
   ```

3. Copy and paste your Deck list from the Archidekt import and the Trim List from Deckcheck into the GUI.
4. Copy and paste your updated list into Archidekt import, replacing everything existing.

## Requirements

- Python 3.x
- `pandas` library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/DrakeWood/MTG-CSV-Converters.git
   ```

2. **Navigate to the project directory:**

   ```sh
   cd MTG-CSV-Converters
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
