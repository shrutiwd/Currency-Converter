# Currency Converter

This Python program is designed to perform currency conversion between a particular country's currency and other foreign currencies. It operates on the basic concepts of Python and allows users to convert currencies using exchange rates stored in a data file.

## Overview

The program reads exchange rate data from a file named `currexchangedata.txt` and stores it in a dictionary. It provides three conversion options:

1. Convert INR currency into foreign currency.
2. Convert foreign currency into INR.
3. Convert between two foreign currencies.

## Usage

1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/shrutiwd/Currency-Converter.git
    cd Currency-Converter
    ```

2. Ensure you have Python installed on your system.

3. Prepare the exchange rate data file (`currexchangedata.txt`) with the following format:

    ```
    Currency1 \t INR_Value \t Foreign_Value
    Currency2 \t INR_Value \t Foreign_Value
    ...
    ```

4. Run the program:

    ```bash
    python currconverter.py
    ```

5. Choose the conversion option as prompted.

## File Structure

- `currconverter.py`: The main Python script for currency conversion.
- `currexchangedata.txt`: Data file containing exchange rates.
- `requirements.txt`: File specifying the dependencies for the program.

## Note

- Make sure the exchange rate data file (`currexchangedata.txt`) is properly formatted.

Feel free to customize the program or exchange rate data according to your specific needs.

Happy currency converting!
