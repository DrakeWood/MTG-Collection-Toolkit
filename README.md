# MTG CSV Converters

A collection of tools for converting Magic: The Gathering (MTG) card data between different formats.

## Table of Contents

- [Converters](#converters)
  - [Manabox to Archidekt](#manabox-to-archidekt)
  - [Cardtrader to Manabox](#cardtrader-to-manabox)
- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)

## Converters

### Manabox to Archidekt

Converts a Manabox collection export to an Archidekt import format. This tool specifically exports only binders and excludes lists and Italian Legends.

#### Usage

1. Ensure Python 3.x and the `pandas` library are installed.
2. Run the script using:

   ```sh
   python manabox_to_archidekt.py sample_manabox_export.csv output.csv
   ```

   - Optionally, specify an output file name.

### Cardtrader to Manabox

This tool imports a Cardtrader order into a Manabox collection. It adjusts column names, set codes, and other format-specific details to match Manabox requirements.

#### Usage

1. Ensure Python 3.x and the `pandas` library are installed.
2. Run the script using:

   ```sh
   python cardtrader_to_manabox.py sample_cardtrader_to_manabox.csv output.csv
   ```

   - Optionally, specify an output file name.

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
