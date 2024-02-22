#!/usr/bin/python3
import csv
import os
import sys

def escape_formulae(data):
    """Check if data starts with =,+,-,@ or contains tabs or carriage returns.
    Prefix a single quotation mark if needed to ensure text is handled correctly."""
    if data.startswith(('=', '+', '-', '@')) or '\t' in data or '\r' in data:
        return "'" + data
    return data

def remove_cmd_string(field):
    """Remove all instances of 'cmd' strings in the field."""
    return field.replace('cmd', '')

def process_csv(input_csv_filename, output_csv_filename):
    """Read a CSV file and apply data cleansing and escaping rules to each field.
    Then, write the sanitized data into a new CSV file."""
    with open(input_csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        with open(output_csv_filename, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, quotechar='"', quoting=csv.QUOTE_ALL)

            for row in reader:
                sanitized_row = [
                    escape_formulae(remove_cmd_string(field)) for field in row
                ]
                writer.writerow(sanitized_row)

def main(input_csv_filename):
    """Main function to check if the input CSV file exists and process it."""
    if not os.path.exists(input_csv_filename):
        print("Error: The file does not exist.")
        return

    output_csv_filename = 'sanitized_' + os.path.basename(input_csv_filename)
    process_csv(input_csv_filename, output_csv_filename)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_csv_filename>")
    else:
        main(sys.argv[1])
