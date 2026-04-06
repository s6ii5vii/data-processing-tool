import csv
import json
import argparse
from pathlib import Path


def load_csv(file_path):
    data = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def load_json(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("JSON file must contain a list of records.")

    return data


def load_data(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() == ".csv":
        return load_csv(file_path)

    if path.suffix.lower() == ".json":
        return load_json(file_path)

    raise ValueError("Unsupported file format. Use .csv or .json")


def clean_data(data):
    cleaned = []

    for row in data:
        clean_row = {}
        for key, value in row.items():
            if isinstance(value, str):
                value = value.strip()
                if value == "":
                    value = None
            clean_row[key] = value
        cleaned.append(clean_row)

    return cleaned


def filter_data(data, filter_condition):
    if "=" not in filter_condition:
        raise ValueError("Filter must be in the format column=value")

    key, value = filter_condition.split("=", 1)
    key = key.strip()
    value = value.strip()

    return [row for row in data if str(row.get(key)) == value]


def select_columns(data, columns):
    cols = [col.strip() for col in columns.split(",")]
    return [{col: row.get(col) for col in cols} for row in data]


def summarize_data(data):
    if not data:
        print("No data to summarize.")
        return

    print("\n=== DATA SUMMARY ===")
    print(f"Total rows: {len(data)}")
    print(f"Columns: {list(data[0].keys())}")

    missing_counts = {}
    for key in data[0].keys():
        missing_counts[key] = sum(1 for row in data if row.get(key) in [None, ""])

    print("\nMissing values by column:")
    for key, count in missing_counts.items():
        print(f"- {key}: {count}")


def save_cleaned_data(data, output_file):
    path = Path(output_file)

    if path.suffix.lower() == ".csv":
        if not data:
            raise ValueError("No data to save.")

        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    elif path.suffix.lower() == ".json":
        with open(output_file, mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

    else:
        raise ValueError("Output file must end in .csv or .json")


def main():
    parser = argparse.ArgumentParser(description="Data Processing Tool")
    parser.add_argument("--file", required=True, help="Path to input CSV or JSON file")
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Only display dataset summary without saving cleaned output"
    )
    parser.add_argument(
        "--output",
        help="Path to save cleaned data (.csv or .json)"
    )
    parser.add_argument(
        "--filter",
        help="Filter rows using column=value format (example: age=25)"
    )
    parser.add_argument(
        "--columns",
        help="Comma-separated list of columns to keep (example: name,age)"
    )

    args = parser.parse_args()

    try:
        raw_data = load_data(args.file)
        cleaned_data = clean_data(raw_data)

        if args.filter:
            cleaned_data = filter_data(cleaned_data, args.filter)

        if args.columns:
            cleaned_data = select_columns(cleaned_data, args.columns)

        summarize_data(cleaned_data)

        if not args.summary_only:
            if args.output:
                save_cleaned_data(cleaned_data, args.output)
                print(f"\nCleaned data saved to: {args.output}")
            else:
                print("\nNo output file provided. Use --output to save cleaned data.")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()