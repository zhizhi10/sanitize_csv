#!/usr/bin/python3
import argparse
import csv
import os
from datetime import datetime

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
    log(f"CSV processing completed. Output saved to: {output_csv_filename}")

def log(message):
    """Print a log message with a timestamp."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {message}")

def main(user_args):
    input_csv_filename = os.path.abspath(user_args.input_csv)
    output_dir = os.path.abspath(user_args.output_directory)

    log(f"Input CSV file path: {input_csv_filename}")
    log(f"Output directory: {output_dir}")

    if not os.path.exists(input_csv_filename):
        log("Error: The input CSV file does not exist.")
        return

    if output_dir and not os.path.exists(output_dir):
        log("Error: The output directory does not exist.")
        return

    input_base_name = os.path.basename(input_csv_filename)
    output_csv_filename = os.path.join(output_dir, 'clean_' + input_base_name)
    process_csv(input_csv_filename, output_csv_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process and sanitize a CSV file.')
    parser.add_argument('input_csv', help='The input CSV file')
    parser.add_argument('-o', '--output_directory', help='The output directory to save the cleaned CSV file', default='.')

    args = parser.parse_args()

    main(args)